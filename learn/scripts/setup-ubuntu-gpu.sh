#!/bin/bash -x

# commands to verify the OS is GPU suported and also checking GPU exists

# assert there is a graphics card
lspci | grep -i nvidia

# todo assert here to make sure ubuntu 18.04
uname -m && cat /etc/*release

gcc --version
uname -r

sudo apt-get install linux-headers-$(uname -r)

# only works for ubuntu 18.04
wget https://developer.download.nvidia.com/compute/cuda/11.0.3/local_installers/cuda_11.0.3_450.51.06_linux.run
sudo sh cuda_11.0.3_450.51.06_linux.run && rm -rf cuda_11.0.3_450.51.06_linux.run

# follow the rest from this 2020 post:
# https://towardsdatascience.com/how-to-properly-use-the-gpu-within-a-docker-container-4c699c78c6d1