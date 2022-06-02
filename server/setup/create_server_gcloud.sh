#!/bin/bash

gcloud dataproc clusters create repserver --region us-central1 --zone us-central1-b \
--single-node --master-machine-type n1-standard-4 --master-boot-disk-size 50 --image-version 2.0-debian10 \
 --optional-components DOCKER --project task5-346818