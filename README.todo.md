# ToDo

2 paths to containerized build/deploy/run
(1) bicep-based (vm sku tbd, filepath, blob via fuse, container from acr)
(2) shipyard-based
    (a) read-direct http, write-to-file, upload back (azcopy)
    (b) use standard task file staging/destaging (see recipes)
    (c) all fuse-based (r/w)

iNetwork.py work
(1) containerization, Dockerfile
(2) update INetwork.py to read from either file or http service (blob)
(3) update iNetwork.py to use a yaml-based config file to parameterize with
    yaml resource file
(4) set up auto-deploy-execute-uploadresults "submit" script
  * possibly through simple batch shipyard?
  * alternatively, just bicep created node

