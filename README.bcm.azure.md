README.bcm.md

AML env mods ...
$ pip install --upgrade keras
$ pip install --upgrade tensorflow

Added ...
K.tf.compat.v1.disable_eager_execution()


On Azure ML compute instances ...

Standard_NC6 (6 cores, 56 GB RAM, 380 GB disk)
GPU - 1 x NVIDIA Tesla K80 (12 GB vRAM)
$0.90/hr
10.26.0.5

$ python3 INetwork.py images/inputs/content/Dipping-Sun.jpg images/inputs/style/starry_night.jpg foo
29s per iteration


Standard_NC6s_v2 (6 cores, 112 GB RAM, 336 GB disk)
GPU - 1 x NVIDIA Tesla P100 (16 GB vRAM)
$2.07/hr
10.26.0.xx

$ python3 INetwork.py images/inputs/content/Dipping-Sun.jpg images/inputs/style/starry_night.jpg foo
7s per iteration


NC6s_v3 (1x V100) no quota in uswest-2

Can I use multiple GPUs? how? parm space sweep?
pipeline/batch?
