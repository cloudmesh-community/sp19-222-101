FROM ubuntu:latest

RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install git-core -y
RUN python -m pip install -y

RUN git clone https://github.com/cloudmesh-community/sp19-222-101.git

WORKDIR /sp19-222-101

