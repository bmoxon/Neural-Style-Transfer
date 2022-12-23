#!/bin/bash

# copy in up-to-date source files
cp ../../INetwork.py .
cp ../../utils.py .
cp ../../tf_bfgs.py .

# not needed for Dockerfile_tf??
# cp ../../requirements_tf.txt .

# and build the docker image
docker build -t bmoxon/nst -f Dockerfile_tf .
