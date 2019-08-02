FROM tensorflow/tensorflow:latest-py3-jupyter

RUN pip install keras

# for python keras image manipulation
RUN pip install pillow sentencepiece
RUN apt-get install -y wget tar bash

WORKDIR /src
# RUN apk --update add wget tar bash
RUN apt-get install -y git
RUN git clone https://github.com/zihangdai/xlnet.git

ENV SQUAD_DIR=/data