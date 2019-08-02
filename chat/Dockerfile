FROM python:3.6-stretch

RUN pip install pyyaml slackclient

# for python keras image manipulation
# RUN pip install pillow sentencepiece
RUN apt-get install -y wget tar bash

WORKDIR /src

# ENV abc=hello
# ENV abc=bye def=$abc

# RUN apk --update add wget tar bash
# RUN apt-get install -y git