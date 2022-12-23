# Pull base image.
FROM ubuntu:18.04
 
LABEL maintainer="Bruce Moxon <brucemoxon@microsoft.com>"

WORKDIR = /root
COPY requirements_tf.txt .
COPY INetwork.py .

# Install updates to base image
RUN apt-get update -y && apt-get install -y --no-install-recommends \
  apt-utils apt-transport-https ca-certificates gnupg software-properties-common lsb-release wget \
  python3.8 python3-pip \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# install cmake
RUN \
wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | apt-key add - && \
apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main' && \
apt-get update -y && \
apt-get install -y cmake

#  ln -s /usr/bin/python3.8 /usr/bin/python3 && \

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements_tf.txt && \
    python3 -m pip install --no-cache-dir tensorflow_probability imageio scikit-image keras tensorflow

CMD ["INetwork.py", "--help"]
