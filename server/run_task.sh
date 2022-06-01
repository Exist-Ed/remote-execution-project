#!/bin/bash

docker run \
  -v /tmp/rep_data:/rep_data \
  rep_worker:v1

docker rm $(docker ps -aq)
