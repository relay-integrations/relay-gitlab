FROM relaysh/core:latest-python
COPY "./handler.py" "/handler.py"
ENTRYPOINT []
CMD ["python3", "/handler.py"]

LABEL "org.opencontainers.image.title"="GitLab merge request merged"
LABEL "org.opencontainers.image.description"="This trigger fires when a GitLab merge request is merged."
LABEL "sh.relay.sdk.version"="v1"
