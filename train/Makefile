all: build run

build:
	@docker build -t learn:tensorflow .

# run as non-root in container to avoid file permission issues
run:
	@docker run -it \
		--rm \
		-u $(id -u):$(id -g) \
		-v $(realpath ./src):/src \
		-v $(realpath ./data):/data \
		-p 8888:8888 \
		--name tensorflowc \
		learn:tensorflow \
		/bin/bash

gpu:
	@docker run -it --rm --runtime=nvidia tensorflow/tensorflow:latest-gpu-py3 /bin/bash