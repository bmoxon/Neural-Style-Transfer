# README CI

Docker build and deploy directories, for both local and Azure Container Registry (ACR)

Start docker on my WSL instance if needed

(base) bmoxon@DESKTOP-2E881CO:~/work/Neural-Style-Transfer/ci/build$ sudo service docker start

## build.sh

wrapper script to copy appropriate source files from the source directory into
the build directory so they can be copied to the docker image as part of the
docker build

## docker build (done in build.sh)

based on tensorflow/tensorflow image, as in Dockerfile_tf

build.sh builds as follows
'''
$ docker build -t bmoxon/nst -f Dockerfile_tf .
'''

## docker run

Once done, run an instance of the image

'''
(base) bmoxon@DESKTOP-2E881CO:~/work/Neural-Style-Transfer/ci/build$ docker run -it bc6 bash

________                               _______________                
___  __/__________________________________  ____/__  /________      __
__  /  _  _ \_  __ \_  ___/  __ \_  ___/_  /_   __  /_  __ \_ | /| / /
_  /   /  __/  / / /(__  )/ /_/ /  /   _  __/   _  / / /_/ /_ |/ |/ / 
/_/    \___//_/ /_//____/ \____//_/    /_/      /_/  \____/____/|__/


WARNING: You are running this container as root, which can cause new files in
mounted volumes to be created as the root user on your host machine.

To avoid this, run the container by specifying your user's userid:

$ docker run -u $(id -u):$(id -g) args...

root@ab8552840210:/= /root# 

'''
root@ab8552840210:/= /root# wget "https://bcmnstpics.blob.core.windows.net/test/images/Blue%20Moon%20Lake.gif?sp=r&st=2022-12-19T18:43:01Z&se=2023-12-20T02:43:01Z&spr=https&sv=2021-06-08&sr=c&sig=HLfY4TKt5C0qkvPyvg09eNXNQxRdljtKvujl%2FauOkvs%3D" --output-document=content.xxx
--2022-12-19 23:13:53--  https://bcmnstpics.blob.core.windows.net/test/images/Blue%20Moon%20Lake.gif?sp=r&st=2022-12-19T18:43:01Z&se=2023-12-20T02:43:01Z&spr=https&sv=2021-06-08&sr=c&sig=HLfY4TKt5C0qkvPyvg09eNXNQxRdljtKvujl%2FauOkvs%3D
Resolving bcmnstpics.blob.core.windows.net (bcmnstpics.blob.core.windows.net)... 20.60.14.196
Connecting to bcmnstpics.blob.core.windows.net (bcmnstpics.blob.core.windows.net)|20.60.14.196|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10625386 (10M) [image/gif]
Saving to: ‘content.xxx’

content.xxx              100%[==================================>]  10.13M  14.9MB/s    in 0.7s    

2022-12-19 23:13:53 (14.9 MB/s) - ‘content.xxx’ saved [10625386/10625386]

root@ab8552840210:/= /root# ls -l
total 10420
-rw-r--r-- 1 root root    24774 Dec 19 22:50 INetwork.py
-rw-r--r-- 1 root root 10625386 Dec 18 00:05 content.xxx
-rw-r--r-- 1 root root     7800 Dec 19 22:50 tf_bfgs.py
-rw-r--r-- 1 root root     1112 Dec 19 22:50 utils.py
'''
