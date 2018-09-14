# This Docker container will generate new SDK endpoints
FROM python:3.6.3-alpine3.6

ADD scripts scripts
RUN ls -lah
RUN pip install scripts/generate

# When running, repo will be mounted at /repo

# This container will always run the generation tool
ENTRYPOINT ["python",  "-m", "generate"]

# The default arguments for ENTRYPOINT
CMD ["--output", "/repo/src/mbed_cloud/core", "--source", "/config/config.yaml"]
