# --------------------------------------------------------------------------
# Pelion Device Management Python SDK
# (C) COPYRIGHT 2017,2019 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""Part of the CI process"""

from collections import namedtuple
from collections import OrderedDict
import copy
import logging
import os
import unittest

# networkx: graph library for generating workflow
import networkx

import yaml

from tag_and_release import ReleaseTarget
from tag_and_release import release_target_map

LOG = logging.getLogger(__name__)
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
container_config_root = os.path.join(PROJECT_ROOT, 'container')
script_templates_root = os.path.join(PROJECT_ROOT, 'scripts', 'templates')
author_file = os.path.relpath(__file__, PROJECT_ROOT)
cache_dir = f'~/caches'
testrunner_cache = f'testrunner.tar'

base_structure = OrderedDict(
    version=2,
    jobs=dict(),
    workflows=dict(
        version=2,
        python_sdk_workflow=dict(
            jobs=[],
        ),
    ),
)

CloudHost = namedtuple('CloudHost', [
    'name',
    'public_name',
    'envvar_host',
    'envvar_key'
])

mbed_cloud_hosts = dict(
    osii=CloudHost('OS2', 'staging', 'MBED_CLOUD_API_HOST_OS2', 'MBED_CLOUD_API_KEY_OS2'),
    production=CloudHost('PROD', 'production', 'MBED_CLOUD_API_HOST_PROD', 'MBED_CLOUD_API_KEY_PROD'),
)

py2_openssl_install = """
# openssl install
RUN apk add g++
RUN apk add libffi-dev
RUN apk add openssl-dev
RUN apk add openssl
"""

py2_openssl_cp = """
# openssl install
COPY --from=PY_SDK_BUILDER /usr/bin/openssl /usr/bin/openssl
COPY --from=PY_SDK_BUILDER /etc/ssl/ /etc/ssl/
COPY --from=PY_SDK_BUILDER /lib/ /lib/
"""

PyVer = namedtuple('PyVer', [
    'name',
    'docker_base',
    'tag',
    'docker_file',
    'compose_file',
    'py2_pre',
    'py2_post'
])
python_versions = dict(
    two=PyVer(
        'py2',
        'python:2.7.14-alpine3.6',
        'mbed_sdk_py2:latest',
        'py2.Dockerfile',
        'py2-compose.yml',
        py2_openssl_install,
        py2_openssl_cp,
    ),
    three=PyVer(
        'py3',
        'python:3.7.0-alpine3.8',
        'mbed_sdk_py3:latest',
        'py3.Dockerfile',
        'py3-compose.yml',
        '',
        '',
    ),
)


def get_testrunner_image():
    """Load testrunner image from docker compose"""
    with open(os.path.join(PROJECT_ROOT, 'scripts', 'templates', 'docker-compose.yml')) as fh:
        docker_compose_spec = yaml.safe_load(fh)
    return docker_compose_spec['services']['testrunner']['image']


def new_base():
    """The high level structure of circle's config"""
    return copy.deepcopy(base_structure)


def new_preload():
    """Job running prior to builds - fetches TestRunner image

    This attempts to pull an image for the TestRunner with the same name as the branch which is being built for the
    Python SDK. If that cannot be found it falls back to the master build of TestRunner. Whichever is pulled is renamed
    with the tag `latest` which will be used by the docker compose.
    """
    branched_testrunner_image = '104059736540.dkr.ecr.us-west-2.amazonaws.com/mbed/sdk-testrunner:${CIRCLE_BRANCH}'
    master_testrunner_image = '104059736540.dkr.ecr.us-west-2.amazonaws.com/mbed/sdk-testrunner:master'
    testrunner_image = get_testrunner_image()
    local_image = testrunner_image.rsplit(':')[-2].rsplit('/')[-1]
    version_file = 'testrunner_version.txt'
    template = yaml.safe_load(f"""
    machine:
      image: 'circleci/classic:201710-02'
    steps:
      - run:
          name: AWS login
          command: |-
            login="$(aws ecr get-login --no-include-email)"
            ${{login}}
      - run:
          name: Pull TestRunner Image for branch and fullback to master
          command: |-
            (docker pull {branched_testrunner_image} && docker tag {branched_testrunner_image} {testrunner_image}) || (docker pull {master_testrunner_image} && docker tag {master_testrunner_image} {testrunner_image})
      - run:
          name: Make cache directory
          command: mkdir -p {cache_dir}
      - run:
          name: Obtain Testrunner Version
          command: echo $(docker run {testrunner_image} python -m trunner --version) > {cache_dir}/{version_file}
      - run:
          name: Export docker image layer cache
          command: docker save -o {cache_dir}/{testrunner_cache} {testrunner_image}
      - persist_to_workspace: # workspace is used later in this same build
          root: {cache_dir}
          paths: '{testrunner_cache}'
      - persist_to_workspace: # workspace is used later in this same build
          root: {cache_dir}
          paths: '{version_file}'
      - store_artifacts:
          path: {version_file}
    """)
    return 'preload', template


def new_tpip():
    """Job for third party IP report generation"""
    template = yaml.safe_load("""
    steps:
      - checkout
      - run: sudo pip install -e .
      - run: python scripts/tpip.py python_tpip.csv
      - store_artifacts:
          path: python_tpip.csv
    docker:
      - image: circleci/python:3.6.1
    """)
    return 'tpip_report', template


def new_foundation_gen():
    """Job to generate the Foundation interface.

    If there are file changes caused by the generation then these are submitted back to github (which will trigger
    another build). The current build is then cancelled to avoid unnecessary builds and misleading test results (
    which would be with a pre-render code version).
    """
    template = yaml.safe_load("""
    steps:
      - checkout
      - run:
          name: Install pipenv
          command: sudo pip install pipenv
      - run:
          name: Install beta version of black for Python formatting
          command: pipenv install --pre black
      - run:
          name: Install SDK with dev dependencies
          command: pipenv install --dev . 
      - run:
          name: Generate the Foundation interface code
          command: pipenv run python scripts/foundation/render_sdk.py 
            api_specifications/public/sdk_foundation_definition.yaml  -vv
            -p python_definition.yaml 
            -o src/mbed_cloud/sdk
      - run:
          name: Commit code changes (cancel this build if commit made)
          command: |-
              git add -v src/mbed_cloud/foundation/entities/\*.py
              git add -v src/mbed_cloud/foundation/enums/\*.py
              git add -v src/mbed_cloud/foundation/__init__.py
              git commit --message "Auto-generated code" || FILES_CHANGED=True
              git push -q https://${GITHUB_TOKEN}@github.com/ARMmbed/${CIRCLE_PROJECT_REPONAME}.git ${CIRCLE_BRANCH}
              if [ -z "$FILES_CHANGED" ]; then curl -X POST https://circleci.com/api/v1.1/project/github/ARMmbed/${CIRCLE_PROJECT_REPONAME}/${CIRCLE_BUILD_NUM}/cancel?circle-token=${DOCS_CIRCLE_CI_TOKEN}; fi
      - store_artifacts:
          path: python_definition.yaml
          when: always
    docker:
      - image: circleci/python:3.6.3
    """)
    return 'foundation_gen', template


def new_newscheck():
    """Job for checking newsfile existence"""
    template = yaml.safe_load("""
    steps:
      - checkout
      - run: python scripts/assert_news.py
    docker:
      - image: circleci/python:3.6.1
    """)
    return 'news_check', template


def new_build_documentation():
    """Job for checking updating SDK documentation"""
    template = yaml.safe_load("""
    steps:
      - run:
          name: Trigger documentation build
          command: >-
              curl -X POST --header "Content-Type:application/json"
              -d '{"branch":"master"}' 
              https://circleci.com/api/v1.1/project/github/${GITHUB_DOCS_ORGANISATION}/${GITHUB_DOCS_PROJECT}/build?circle-token=${DOCS_CIRCLE_CI_TOKEN}
    docker:
      - image: circleci/node:jessie-browsers
    """)
    return 'build_documentation', template


def upload_reference_documentation():
    """Job for uploading reference documentation to S3"""

    # Build the documentation using python 3
    py_ver = python_versions["three"]

    cache_file = f'app_{py_ver.name}.tar'
    template = yaml.safe_load(f"""
    machine:
      image: circleci/classic:201710-02
    steps:
      - attach_workspace:
          at: {cache_dir}
      - checkout
      - run:
          name: Install prerequisites
          command: sudo pip install awscli
      - run:
          name: Load docker image layer cache
          command: docker load -i {cache_dir}/{cache_file}
      - run:
          name: Start a named container
          command: docker run --name=SDK {py_ver.tag}
      - run:
          name: Extract the documentation
          command: 'docker cp SDK:/build/built_docs ./built_docs'
      - run:
          name: Upload the documentation
          command: >-
            aws s3 sync --delete --cache-control
            max-age=3600 built_docs s3://mbed-cloud-sdk-python/${{CIRCLE_BRANCH}}-branch
    """)
    return 'reference_documentation', template


def build_name(py_ver: PyVer):
    """Name"""
    return f'build_{py_ver.name}'


def new_build(py_ver: PyVer):
    """Job for building/caching different docker images"""
    cache_file = f'app_{py_ver.name}.tar'
    cache_path = f'{cache_dir}/{cache_file}'
    cache_key = f'v3-{py_ver.name}-{{{{ .Branch }}}}'
    template = yaml.safe_load(f"""
    machine:
      image: 'circleci/classic:201710-02'
      docker_layer_caching: true
    steps:
      - checkout
      - restore_cache:
          keys: ['{cache_key}']
          paths: ['{cache_path}']
      - attach_workspace:
          at: {cache_dir}
      - run:
          name: Load docker image for TestRunner
          command: docker load -i {cache_dir}/{testrunner_cache}
      - run:
          name: Load docker image layer cache
          command: docker load -i {cache_path} || true  # silent failure if missing cache
      - run:
          name: Build application docker image
          command: >-
            docker build --cache-from={py_ver.tag}
            -t {py_ver.tag}
            --build-arg TESTRUNNER_VERSION=$(cat {cache_dir}/testrunner_version.txt)
            -f container/{py_ver.docker_file} .
      - run:
          name: Make cache directory
          command: mkdir -p {cache_dir}
      - run:
          name: Export docker image layer cache
          command: docker save -o {cache_path} {py_ver.tag}
      - save_cache: # cache is used between builds
          key: '{cache_key}'
          paths: ['{cache_path}']
      - persist_to_workspace: # workspace is used later in this same build
          root: {cache_dir}
          paths: '{cache_file}'
      
      # extracting documentation for review:
      - run:
          name: Start a named container
          command: docker run --name=SDK {py_ver.tag}
      - run:
          name: Extract the documentation
          command: 'docker cp SDK:/build/built_docs ./built_docs'
      - store_artifacts:
          path: built_docs
    """)
    return build_name(py_ver), template


def test_name(py_ver: PyVer, cloud_host: CloudHost):
    """Name"""
    return f'test_{py_ver.name}_{cloud_host.name}'


def new_test(py_ver: PyVer, cloud_host: CloudHost):
    """Job for running integration/coverage tests"""
    sdk_docker_cache = f'app_{py_ver.name}.tar'
    template = yaml.safe_load(f"""
    machine:
      image: circleci/classic:201710-02
    steps:
      - checkout
      - attach_workspace:
          at: {cache_dir}
      - run:
          name: Load docker image for SDK
          command: docker load -i {cache_dir}/{sdk_docker_cache}
      - run:
          name: Load docker image for TestRunner
          command: docker load -i {cache_dir}/{testrunner_cache}
      - run:
          name: Get docker-compose
          command: pip install docker-compose==1.21.0
      - run:
          name: Set testrunner parameters
          command: |-
            echo 'export TEST_RUNNER_DEFAULT_API_HOST=${{{cloud_host.envvar_host}}}' >> $BASH_ENV
            echo 'export TEST_RUNNER_DEFAULT_API_KEY=${{{cloud_host.envvar_key}}}' >> $BASH_ENV
      - run:
          name: Run all tests
          no_output_timeout: 15m
          command: >-
            docker-compose
            -f {os.path.relpath(container_config_root, PROJECT_ROOT)}/{py_ver.compose_file}
            up
            --exit-code-from=sdk_test_server
      - run:
          name: Generate summary
          command: sudo python scripts/ci_summary.py --noblock
          when: always
      - store_artifacts:
          path: results
      - run:
          name: Install codecov
          command: sudo pip install codecov
      - run: 
          command: codecov --file=results/coverage.xml --flags {py_ver.name} {cloud_host.public_name}
          name: Upload code coverage results
    """)
    return test_name(py_ver, cloud_host), template


def deploy_name(py_ver: PyVer, release_target: ReleaseTarget):
    """Name"""
    return f'deploy_{py_ver.name}_{release_target.name}'


def new_deploy(py_ver: PyVer, release_target: ReleaseTarget):
    """Job for deploying package to pypi"""
    cache_file = f'app_{py_ver.name}.tar'
    template = yaml.safe_load(f"""
    machine:
      image: circleci/classic:201710-02
    steps:
      - attach_workspace:
          at: {cache_dir}
      - checkout
      - run:
          name: Install prerequisites
          command: sudo pip install awscli
      - run:
          name: Load docker image layer cache
          command: docker load -i {cache_dir}/{cache_file}
      - run:
          name: Start a named container
          command: docker run --name=SDK {py_ver.tag}
      - run:
          name: Extract the documentation
          command: 'docker cp SDK:/build/built_docs ./built_docs'
      - run:
          name: Upload the documentation
          command: >-
            aws s3 sync --delete --cache-control
            max-age=3600 built_docs s3://mbed-cloud-sdk-python/${{CIRCLE_BRANCH}}-release
      - run:
          name: Tag and release
          command: >-
            docker run --env-file=scripts/templates/envvars.env
            -e TWINE_REPOSITORY={release_target.twine_repo}
            {py_ver.tag}
            sh -c "source .venv/bin/activate && python scripts/tag_and_release.py --mode={release_target.mode}"
      - run:
          name: Start the release party!
          command: >-
            docker run --env-file=scripts/templates/envvars.env
            {py_ver.tag}
            sh -c "source .venv/bin/activate && python scripts/notify.py"
    """)
    return deploy_name(py_ver, release_target), template


def release_name(release_target: ReleaseTarget):
    """Name"""
    return f'release_{release_target.name}'


def generate_circle_output():
    """Build sequence for Circle CI 2.0 config.yml

    builds the circleci structure
    also links individual jobs into a workflow graph
    """
    base = new_base()
    workflow = networkx.DiGraph()
    LOG.info('%s python versions', len(python_versions))
    LOG.info('%s Pelion Device Management hosts', len(mbed_cloud_hosts))

    job, content = new_tpip()
    base['jobs'].update({job: content})
    workflow.add_node(job)

    new_foundation_job, content = new_foundation_gen()
    base['jobs'].update({new_foundation_job: content})
    workflow.add_node(new_foundation_job)

    job, content = new_newscheck()
    base['jobs'].update({job: content})
    workflow.add_node(
        job,
        workflow=dict(
            filters=dict(
                branches=dict(
                    # we ignore this check for builds directly on the base branches
                    ignore=['master', 'integration']
                )
            )
        )
    )

    job, content = new_build_documentation()
    base['jobs'].update({job: content})
    workflow.add_node(
        job,
        workflow=dict(
            requires=['build_py2', 'build_py3'],
            filters=dict(
                branches=dict(
                    # Only update the documentation on release branches
                    only=['master', 'beta']
                )
            )
        )
    )

    job, content = upload_reference_documentation()
    base['jobs'].update({job: content})
    workflow.add_node(
        job,
        workflow=dict(
            requires=['build_py2', 'build_py3'],
            filters=dict(
                branches=dict(
                    # Only update the documentation on release branches
                    only=['master', 'beta']
                )
            )
        )
    )

    preload_job, content = new_preload()
    base['jobs'].update({preload_job: content})
    workflow.add_node(job)

    for py_ver in python_versions.values():
        build_job, build_content = new_build(py_ver=py_ver)
        base['jobs'].update({build_job: build_content})
        # Add requires to builds on preload and foundation_gen
        workflow.add_edge(preload_job, build_job)
        workflow.add_edge(new_foundation_job, build_job)

        for cloud_host in mbed_cloud_hosts.values():
            test_job, test_content = new_test(py_ver=py_ver, cloud_host=cloud_host)
            base['jobs'].update({test_job: test_content})
            workflow.add_edge(build_job, test_job)

    for release_target in release_target_map.values():
        deploy_job, deploy_content = new_deploy(
            py_ver=python_versions['three'],
            release_target=release_target
        )
        base['jobs'].update({deploy_job: deploy_content})

    # wire up the release gates (clicky buttons)
    workflow.add_edge(
        test_name(python_versions['three'], mbed_cloud_hosts['osii']),
        release_name(release_target_map['beta']),
        type='approval',
    )
    workflow.add_edge(
        test_name(python_versions['three'], mbed_cloud_hosts['production']),
        release_name(release_target_map['prod']),
        type='approval',
        filters=dict(branches=dict(only='master')),
    )
    workflow.add_edge(
        test_name(python_versions['two'], mbed_cloud_hosts['production']),
        release_name(release_target_map['prod']),
    )

    # we only want to deploy in certain conditions
    workflow.add_edge(
        release_name(release_target_map['beta']),
        deploy_name(python_versions['three'], release_target_map['beta'])
    )

    workflow.add_edge(
        release_name(release_target_map['prod']),
        deploy_name(python_versions['three'], release_target_map['prod'])
    )

    workflow_jobs = base['workflows']['python_sdk_workflow']['jobs']

    # build the workflow graph
    for job_name in networkx.topological_sort(workflow):
        job_config = {}
        per_node_config = workflow.nodes[job_name].get('workflow')
        if per_node_config:
            job_config.update(per_node_config)
        workflow_jobs.append({job_name: job_config})
        for edge in workflow.in_edges(job_name):
            job_config.update(workflow.get_edge_data(*edge))
            job_config.setdefault('requires', []).append(edge[0])

    LOG.info('%s circle jobs', len(base['jobs']))
    return dict(base)


def generate_docker_file(py_ver: PyVer):
    """Templated docker files"""
    with open(os.path.join(script_templates_root, 'Dockerfile')) as fh:
        return fh.read().format(py_ver=py_ver, author=author_file)


def generate_compose_file(py_ver: PyVer):
    """Templated docker-compose files"""
    with open(os.path.join(script_templates_root, 'docker-compose.yml')) as fh:
        return fh.read().format(py_ver=py_ver, author=author_file)


def generate_docker_targets():
    """Write all templated container engine files"""
    output = {}
    for py_ver in python_versions.values():
        filepath = os.path.join(container_config_root, py_ver.docker_file)
        output[filepath] = generate_docker_file(py_ver)
        filepath = os.path.join(container_config_root, py_ver.compose_file)
        output[filepath] = generate_compose_file(py_ver)
    return output


def main(output_path=None):
    """Writes out new python build system

    This is needed because CircleCI does not support build matrices
    nor parameterisation of cache paths or other aspects of their
    config

    There's also the added bonus of validating the yaml as we go.

    Additionally, we template and write Docker and docker-compose files
    for multiple python versions, as Docker `FROM` statements are also
    un-templatable using environment variables or similar.

    The bulk of the config structure is parsed templated yaml, which
    seems the most succinct way of building deeply nested dictionaries and lists,
    and also cleanly maps to the appearance of config.yml before & after templating.

    The main job blocks (build, test, deploy) are expanded as the product of python versions
    and Pelion Device Management environments, before being recombined into the job listing.

    Jobs are chained into a CircleCI workflow using a graph
    (in which nodes are job identifiers, and edges describe the dependencies
    and any additional parameters)
    """
    config_output_file = output_path or os.path.join(PROJECT_ROOT, '.circleci', 'config.yml')
    yaml_structure = generate_circle_output()
    with open(config_output_file, 'w') as fh:
        yaml_content = yaml.safe_dump(data=yaml_structure, default_flow_style=False)
        fh.write(
            f'#\n'
            f'# This file is autogenerated, do not modify manually. '
            f'See {author_file} for instructions.\n'
            f'#\n'
            f'{yaml_content}'
        )

    for path, content in generate_docker_targets().items():
        LOG.info('writing %s', path)
        with open(path, 'w') as fh:
            fh.write(content)


class Test(unittest.TestCase):
    """Test"""

    def setUp(self):
        """Make sure we have some logging running"""
        logging.basicConfig(level=logging.INFO)

    def test(self):
        """Runs build as if it were a test"""
        main()


if __name__ == '__main__':
    main()
