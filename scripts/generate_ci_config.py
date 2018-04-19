# --------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
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

# twine: python's package upload tool
from twine.utils import TEST_REPOSITORY, DEFAULT_REPOSITORY

# networkx: graph library for generating workflow
import networkx

import yaml

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
container_config_root = os.path.join(PROJECT_ROOT, 'container')
cache_dir = f'~/caches'

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

CloudHost = namedtuple('CloudHost', ['name', 'envvar_host', 'envvar_key'])
mbed_cloud_hosts = dict(
    osii=CloudHost('osii', 'MBED_CLOUD_API_HOST_OS2', 'MBED_CLOUD_API_KEY_OS2'),
    production=CloudHost('production', 'MBED_CLOUD_API_HOST_PROD', 'MBED_CLOUD_API_KEY_PROD'),
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

PyVer = namedtuple('PyVer', ['name', 'docker_base', 'tag', 'docker_file', 'compose_file', 'py2_pre', 'py2_post'])
python_versions = dict(
    two=PyVer(
        'python_two',
        'python:2.7.14-alpine3.6',
        'mbed_sdk_py2:latest',
        'py2.Dockerfile',
        'py2-compose.yml',
        py2_openssl_install,
        py2_openssl_cp,
    ),
    three=PyVer(
        'python_three',
        'python:3.6.3-alpine3.6',
        'mbed_sdk_py3:latest',
        'py3.Dockerfile',
        'py3-compose.yml',
        '',
        '',
    ),
)

# we have multiple release targets
ReleaseTarget = namedtuple('ReleaseTarget', ['name', 'twine_url'])
release_targets = dict(
    test=ReleaseTarget('test', TEST_REPOSITORY),
    live=ReleaseTarget('live', DEFAULT_REPOSITORY),
)


def new_base():
    # the high level structure of circle's config
    return copy.deepcopy(base_structure)


def new_tpip():
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


def build_name(py_ver: PyVer):
    return f'build_{py_ver.name}'


def new_build(py_ver: PyVer):
    cache_file = f'app_{py_ver.name}.tar'
    cache_path = f'{cache_dir}/{cache_file}'
    cache_key = f'v2-{py_ver.name}-{{{{ .Branch }}}}'
    template = yaml.safe_load(f"""
        machine:
          image: 'circleci/classic:201710-02'
        steps:
          - checkout
          - restore_cache:
              keys: ['{cache_key}']
              paths: ['{cache_path}']
          - run:
              name: Load docker image layer cache
              command: docker load -i {cache_path} || true  # silent failure if missing cache
          - run:
              name: Build application docker image
              command: docker build --cache-from={py_ver.tag} -t {py_ver.tag} -f container/{py_ver.docker_file} .
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
    """)
    return build_name(py_ver), template


def test_name(py_ver: PyVer, cloud_host: CloudHost):
    return f'test_{py_ver.name}_{cloud_host.name}'


def new_test(py_ver: PyVer, cloud_host: CloudHost):
    cache_file = f'app_{py_ver.name}.tar'
    cache_path = f'{cache_dir}/{cache_file}'
    template = yaml.safe_load(f"""
        machine:
          image: circleci/classic:201710-02
        steps:
          - checkout
          - attach_workspace:
              at: {cache_dir}
          - run:
              name: Load docker image layer cache
              command: docker load -i {cache_path}
          - run: |
                  export TEST_RUNNER_DEFAULT_API_HOST=${{{cloud_host.envvar_host}}}
                  export TEST_RUNNER_DEFAULT_API_KEY=${{{cloud_host.envvar_key}}}
                  login="$(aws ecr get-login --no-include-email)"
                  ${{login}}
          - run: pip install docker-compose==1.21.0
          - run:
              name: Run all tests
              command: docker-compose -f {os.path.relpath(container_config_root, PROJECT_ROOT)}/{py_ver.compose_file} up --exit-code-from=sdk_test_server
              no_output_timeout: 15m
          - run:
              name: Generate summary
              command: python scripts/ci_summary.py --noblock
          - store_artifacts:
              path: results
    """)
    return test_name(py_ver, cloud_host), template


def deploy_name(py_ver: PyVer, release_target: ReleaseTarget):
    return f'deploy_{py_ver.name}_{release_target.name}'


def new_deploy(py_ver: PyVer, release_target: ReleaseTarget):
    cache_file = f'app_{py_ver.name}.tar'
    cache_path = f'{cache_dir}/{cache_file}'
    template = yaml.safe_load(f"""
        machine:
          image: circleci/classic:201710-02
        steps:
          - attach_workspace:
              at: {cache_dir}
          - run:
              name: Load docker image layer cache
              command: docker load -i {cache_path}
          - run:
              name: Start a named container
              command: docker run --name=SDK {py_ver.tag}
          - run:
              name: Extract the documentation
              command: 'docker cp SDK:/build/built_docs /built_docs'
          - run:
              name: Upload the documentation
              command: 'sudo pip install awscli && aws s3 sync --delete --cache-control max-age=3600 built_docs s3://mbed-cloud-sdk-python'
          - run: 
              name: Tag and release
              command: docker run {py_ver.tag} sh -c "source .venv/bin/activate && python scripts/tag_and_release.py {release_target.twine_url}"
          - run:
              name: Start the release party!
              command: docker run --env SLACK_API_TOKEN=${{SLACK_API_TOKEN}} {py_ver.tag} sh -c "source .venv/bin/activate && python scripts/notify.py"
    """)
    return deploy_name(py_ver, release_target), template


def release_name(release_target: ReleaseTarget):
    return f'release_{release_target.name}'


def generate_circle_output():
    """
    builds the circleci structure
    also links individual jobs into a workflow graph
    """

    base = new_base()
    workflow = networkx.DiGraph()
    logging.info('%s python versions', len(python_versions))
    logging.info('%s mbed cloud hosts', len(mbed_cloud_hosts))

    tpip_job, tpip_content = new_tpip()
    base['jobs'].update({tpip_job: tpip_content})
    workflow.add_node(tpip_job)

    for py_ver in python_versions.values():
        build_job, build_content = new_build(py_ver=py_ver)
        base['jobs'].update({build_job: build_content})

        for cloud_host in mbed_cloud_hosts.values():
            test_job, test_content = new_test(py_ver=py_ver, cloud_host=cloud_host)
            base['jobs'].update({test_job: test_content})
            workflow.add_edge(build_job, test_job)

    for twine_target in release_targets.values():
        deploy_job, deploy_content = new_deploy(py_ver=python_versions['three'], release_target=twine_target)
        base['jobs'].update({deploy_job: deploy_content})

    # wire up the release gates (clicky buttons)
    workflow.add_edge(
        test_name(python_versions['three'], mbed_cloud_hosts['osii']),
        release_name(release_targets['test']),
        type='approval',
    )
    workflow.add_edge(
        test_name(python_versions['three'], mbed_cloud_hosts['production']),
        release_name(release_targets['live']),
        type='approval',
        filters=dict(branches=dict(only='master')),
    )
    workflow.add_edge(
        test_name(python_versions['two'], mbed_cloud_hosts['production']),
        release_name(release_targets['live']),
    )

    # we only want to deploy in certain conditions
    workflow.add_edge(
        release_name(release_targets['test']),
        deploy_name(python_versions['three'], release_targets['test'])
    )

    workflow.add_edge(
        release_name(release_targets['live']),
        deploy_name(python_versions['three'], release_targets['live'])
    )

    workflow_jobs = base['workflows']['python_sdk_workflow']['jobs']

    # build the workflow graph
    for job_name in networkx.topological_sort(workflow):
        job_config = {}
        workflow_jobs.append({job_name: job_config})
        for edge in workflow.in_edges(job_name):
            job_config.update(workflow.get_edge_data(*edge))
            job_config.setdefault('requires', []).append(edge[0])

    logging.info('%s circle jobs', len(base['jobs']))
    return dict(base)


def generate_docker_file(py_ver: PyVer):
    with open(os.path.join('templates', 'Dockerfile')) as fh:
        return fh.read().format(py_ver=py_ver, author=os.path.relpath(__file__, PROJECT_ROOT))


def generate_compose_file(py_ver: PyVer):
    with open(os.path.join('templates', 'docker-compose.yml')) as fh:
        return fh.read().format(py_ver=py_ver, author=os.path.relpath(__file__, PROJECT_ROOT))


def generate_docker_targets():
    output = {}
    for py_ver in python_versions.values():
        output[os.path.join(container_config_root, py_ver.docker_file)] = generate_docker_file(py_ver)
        output[os.path.join(container_config_root, py_ver.compose_file)] = generate_compose_file(py_ver)
    return output


def main(output_path=None):
    """Writes out new python build system

    This is needed because CircleCI does not support build matrices
    nor parameterisation of cache paths or other aspects of their
    config

    There's also the added bonus of validating the yaml as we go.
    """
    config_output = output_path or os.path.join(PROJECT_ROOT, '.circleci', 'config.yml')

    OUT = generate_circle_output()

    with open(config_output, 'w') as fh:
        yaml.safe_dump(data=OUT, stream=fh, default_flow_style=False)

    for path, content in generate_docker_targets().items():
        logging.info('writing %s', path)
        with open(path, 'w') as fh:
            fh.write(content)


class Test(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test(self):
        main()


if __name__ == '__main__':
    main()
