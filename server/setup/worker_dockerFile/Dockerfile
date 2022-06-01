FROM ubuntu:22.04

RUN apt update && \
apt install -y python3-pip

WORKDIR /rep_data

SHELL ["/bin/bash", "-c"]

CMD source rep_orchestration_script.sh > rep_output.txt 2>&1
