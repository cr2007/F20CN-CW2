# Reference: https://github.com/devcontainers/images/tree/main/src/python

FROM mcr.microsoft.com/devcontainers/python:3

RUN apt upgrade

# Install Git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs
