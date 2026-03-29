#!/bin/bash

INSTANCE_NAME="autoscale-vm-$(date +%s)"

echo "Starting cloud scaling..."

gcloud compute instance create $INSTANCE_NAME \
  --zone=asia-south1-c \
  --machine-type=e2-medium \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud
