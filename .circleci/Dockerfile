#
# Build
#

FROM python:3.6.3-alpine3.6 as PY_SDK_BUILDER
# don't cache any pip downloads
ENV PIP_NO_CACHE_DIR=false
# pipenv puts new virtual env in current working directory
ENV PIPENV_VENV_IN_PROJECT=true

# set the working directory (explicit mkdir needed for docker <= 1.9.1 i.e. circleci)
RUN mkdir -p /build
WORKDIR /build

# install system-level dependencies
RUN apk update
RUN apk --no-cache add git
RUN python -m pip install --no-cache-dir -U setuptools pip==9.0.3 pipenv==11.9.0

# add bare minimum files to survive a pip install
ADD scripts/dvcs_version.py scripts/dvcs_version.py
ADD src/mbed_cloud/_version.py src/mbed_cloud/_version.py
ADD setup* ./
ADD README.rst ./
ADD requirements.txt ./
ADD Pip* ./

# install the project (with dev dependencies)
RUN pipenv install --dev

# load the entire project from local checkout as build context
ADD . .

# version the codebase
RUN pipenv run python scripts/dvcs_version.py
RUN pipenv run python -c "import mbed_cloud; print(mbed_cloud.__version__)"

# run smoke tests
RUN pipenv run pytest --durations=3 tests/unit

# generate a package
RUN pipenv run python setup.py clean --all bdist_wheel


#
# Minimal
#

# minimal image for future work. this should come out 'smallish' ~ 160MB
FROM python:3.6.3-alpine3.6 as PY_SDK_LITE
# working dir
WORKDIR /build

COPY --from=PY_SDK_BUILDER build/dist dist
COPY --from=PY_SDK_BUILDER build/.venv .venv
COPY --from=PY_SDK_BUILDER build/tests tests
# previously, next line also had --no-deps, but we can sanity-check that the venv has everything we need:
RUN source .venv/bin/activate && pip install --no-cache-dir --no-index --find-links dist mbed_cloud_sdk

CMD source .venv/bin/activate && python -c "import mbed_cloud; print(mbed_cloud.__version__)"
