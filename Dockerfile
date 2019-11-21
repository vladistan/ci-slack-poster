FROM python:3.7-alpine
RUN mkdir -p /build
COPY . /build
WORKDIR /build
RUN pip install -e .
ENTRYPOINT ["/usr/local/bin/slack_post"]
