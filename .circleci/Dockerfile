FROM python:3.6.3-alpine3.6 as BUILDER
#FROM {BASE_IMAGE}

ENV PYTHONPATH=~/bin
# don't cache any pip downloads
ENV PIP_NO_CACHE_DIR=false
ENV PIPENV_VENV_IN_PROJECT=true

# set the working directory (explicit mkdir needed for docker <= 1.9.1 i.e. circleci)
RUN mkdir -p /build
WORKDIR /build


# install system-level dependencies
RUN apk update
RUN apk --no-cache add git
RUN python -m pip install -U setuptools pip pipenv

# install all the python dependencies for our project
ADD Pip* ./
ADD requirements.txt ./
ADD setup* ./
ADD setup* ./
RUN pipenv install . --dev

# import the rest of our project
ADD . .

# version the image
RUN pipenv run python scripts/dvcs_version.py

# link local installation
RUN pipenv install '-e .' --skip-lock

# run smoke tests
RUN pipenv run pytest -v --duration=3 tests/unit
RUN pipenv run python -c "import mbed_cloud; print(mbed_cloud.__version__)"

# stage two, for reduced image size
FROM sdk:3
# working dir
COPY --from=BUILDER /build /build
# cached files (python)
COPY --from=BUILDER /root/.cache /root/.cache
# openssl install
COPY --from=BUILDER /usr/bin/openssl /usr/bin/openssl
COPY --from=BUILDER /etc/ssl/ /etc/ssl/
COPY --from=BUILDER /lib/ /lib/

WORKDIR /build
ADD . .
# pip uses the cache (e.g. wheels) from previous stage
RUN pip install --no-cache-dir -r requirements.txt

# set executable
CMD python -m trunner
