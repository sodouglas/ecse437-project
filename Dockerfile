# get base ubuntu image
FROM ubuntu:latest

# install python
RUN apt-get update
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip

# install package core
RUN python3.9 -m pip install --upgrade pip
RUN pip3 install packagecore

#install fpm and dependencies
RUN apt-get install -y ruby-dev build-essential
RUN gem install fpm
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y rpm
RUN apt install -y libarchive-tools

# install pytest, coveralls
RUN pip3 install pytest
RUN pip3 install coverage
RUN pip3 install pytest-cov
RUN pip3 install coveralls

# install stylecheck
RUN pip3 install black

# install git
RUN apt install -y git-all

# change directory
WORKDIR /ecse437-project

# copy entire repository over
COPY . .
