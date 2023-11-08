FROM mcr.microsoft.com/devcontainers/python:3

RUN apt upgrade

# Install Git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
RUN sudo apt-get install git-lfs
