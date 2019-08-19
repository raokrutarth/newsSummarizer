FROM python:3.6-stretch

RUN pip install pyyaml slackclient

# for python keras image manipulation
# RUN pip install pillow sentencepiece
RUN apt-get install -y wget tar bash

RUN mkdir /logs
RUN echo $(date) > /logs/chat.log

# # forward request and error logs to docker log collector
# RUN ln -sf /dev/stdout /logs/chat.log \
#     && ln -sf /dev/stderr /logs/chat.log

ADD . /src
WORKDIR /src
# ENTRYPOINT ["python", "chat.py"]