# Running INetwork.py on Mac

## Setup
```bash
$ python3.9 -m venv ~/DEV/pythonenvs/nst-doodle
$ . ~/DEV/pythonenvs/nst-doodle/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements_tf.txt
$ pip install tensorflow_probability
$ pip install imageio
$ pip install skikit-image
$ pip install keras
$ pip install tensorflow
```

comment out line in INetwork.py
```bash
# from keras.utils.layer_utils import convert_all_kernels_in_model
```

fix syntax warnings in INetwork.py
```bash
    # if improvement_threshold is not 0.0:
    #     if improvement < improvement_threshold and improvement is not 0.0:
    if improvement_threshold != 0.0:
        if improvement < improvement_threshold and improvement != 0.0:
```

## Running
### Usage

```bash
(nst-doodle) (base) brucemoxon@tigrisbrucis Neural-Style-Transfer % python3 INetwork.py
2022-12-01 20:21:52.554360: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
usage: INetwork.py [-h] [--style_masks STYLE_MASKS [STYLE_MASKS ...]] [--content_mask CONTENT_MASK]
                   [--color_mask COLOR_MASK] [--image_size IMG_SIZE] [--content_weight CONTENT_WEIGHT]
                   [--style_weight STYLE_WEIGHT [STYLE_WEIGHT ...]] [--style_scale STYLE_SCALE]
                   [--total_variation_weight TV_WEIGHT] [--num_iter NUM_ITER] [--model MODEL]
                   [--content_loss_type CONTENT_LOSS_TYPE] [--rescale_image RESCALE_IMAGE]
                   [--rescale_method RESCALE_METHOD] [--maintain_aspect_ratio MAINTAIN_ASPECT_RATIO]
                   [--content_layer CONTENT_LAYER] [--init_image INIT_IMAGE] [--pool_type POOL]
                   [--preserve_color COLOR] [--min_improvement MIN_IMPROVEMENT]
                   base ref [ref ...] res_prefix
INetwork.py: error: the following arguments are required: base, ref, res_prefix
```

### Example
content: images/inputs/content/Dipping-Sun.jpg
style:   images/inputs/style/starry_night.jpg

#### Issues, Debugging

(1) First try ...

```bash
(nst-doodle) (base) brucemoxon@tigrisbrucis Neural-Style-Transfer % python3 INetwork.py ./images/inputs/content/Dipping-Sun.jpg ./images/inputs/style/starry_night.jpg bcmtest
2022-12-01 20:25:27.367985: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-01 20:25:29.616192: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING:tensorflow:The following Variables were used in a Lambda layer's call (tf.concat), but are not present in its tracked objects:   <tf.Variable 'Variable:0' shape=(1, 400, 713, 3) dtype=float32>
  <tf.Variable 'Variable:0' shape=(1, 400, 713, 3) dtype=float32>. This is a strong indication that the Lambda layer should be rewritten as a subclassed Layer.
Downloading data from https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5
58889256/58889256 [==============================] - 3s 0us/step
Model loaded.
Traceback (most recent call last):
  File "/Users/brucemoxon/DEV/workspace/Neural-Style-Transfer/INetwork.py", line 524, in <module>
    grads = K.gradients(loss, combination_image)
  File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/keras/backend.py", line 4667, in gradients
    return tf.compat.v1.gradients(
  File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/tensorflow/python/ops/gradients_impl.py", line 165, in gradients
    return gradients_util._GradientsHelper(
  File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/tensorflow/python/ops/gradients_util.py", line 480, in _GradientsHelper
    raise RuntimeError("tf.gradients is not supported when eager execution "
RuntimeError: tf.gradients is not supported when eager execution is enabled. Use tf.GradientTape instead.
```

(2) Attempted fix 1 ...
See
https://stackoverflow.com/questions/66221788/tf-gradients-is-not-supported-when-eager-execution-is-enabled-use-tf-gradientta

Add
```
K.tf.compat.v1.disable_eager_execution()
```

```bash
(nst-doodle) (base) brucemoxon@tigrisbrucis Neural-Style-Transfer % python3 INetwork.py ./images/inputs/content/Dipping-Sun.jpg ./images/inputs/style/starry_night.jpg bcmtest
...
File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/keras/engine/keras_tensor.py", line 284, in __array__
    f"You are passing {self}, an intermediate Keras symbolic "
  File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/keras/engine/keras_tensor.py", line 329, in __str__
    return "KerasTensor(type_spec=%s%s%s%s)" % (
RecursionError: maximum recursion depth exceeded while calling a Python object
```

(3) Attempted fix 2 ...

Try adding the gradient tape

```bash
(nst-doodle) (base) brucemoxon@tigrisbrucis Neural-Style-Transfer % python3 INetwork.py ./images/inputs/content/Dipping-Sun.jpg ./images/inputs/style/starry_night.jpg bcmtest
...
Traceback (most recent call last):
  File "/Users/brucemoxon/DEV/workspace/Neural-Style-Transfer/INetwork.py", line 534, in <module>
    grads = tape.gradient(loss, combination_image)
  File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/tensorflow/python/eager/backprop.py", line 1112, in gradient
    flat_grad = imperative_grad.imperative_grad(
  File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/tensorflow/python/eager/imperative_grad.py", line 67, in imperative_grad
    return pywrap_tfe.TFE_Py_TapeGradient(
AttributeError: 'KerasTensor' object has no attribute '_id'
```

(4) Back to original gradient computation, with eager execution disabled up at the top (before
first Keras call)

```bash
# bcm
# for eager execution disabling in TF2
# https://github.com/tensorflow/tensorflow/issues/33135
# doesnt seem to work ... recursion depth/infinite recursion??
K.tf.compat.v1.disable_eager_execution()
```

```bash
(nst-doodle) (base) brucemoxon@tigrisbrucis Neural-Style-Transfer % python3 INetwork.py ./images/inputs/content/Dipping-Sun.jpg ./images/inputs/style/starry_night.jpg bcmtest
2022-12-02 11:38:05.021345: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-02 11:38:09.483907: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-02 11:38:09.506274: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:357] MLIR V1 optimization pass is not enabled
2022-12-02 11:38:09.602273: W tensorflow/c/c_api.cc:291] Operation '{name:'conv4_2/bias/Assign' id:229 op device:{requested: '', assigned: ''} def:{{{node conv4_2/bias/Assign}} = AssignVariableOp[_has_manual_control_dependencies=true, dtype=DT_FLOAT, validate_shape=false](conv4_2/bias, conv4_2/bias/Initializer/zeros)}}' was changed by setting attribute after it was run by a session. This mutation will have no effect, and will trigger an error in the future. Either don't modify nodes after running them or create a new session.
Model loaded.
Starting iteration 1 of 10
2022-12-02 11:38:12.866224: W tensorflow/c/c_api.cc:291] Operation '{name:'Variable_2/Assign' id:444 op device:{requested: '', assigned: ''} def:{{{node Variable_2/Assign}} = AssignVariableOp[_has_manual_control_dependencies=true, dtype=DT_FLOAT, validate_shape=false](Variable_2, Variable_2/Initializer/initial_value)}}' was changed by setting attribute after it was run by a session. This mutation will have no effect, and will trigger an error in the future. Either don't modify nodes after running them or create a new session.
Current loss value: 209525980.0  Improvement : 0.000 %
Rescaling Image to (400, 713)
Image saved as bcmtest_at_iteration_1.png
Iteration 1 completed in 125s
Starting iteration 2 of 10
...
```
Success!

~ 2 min 1 iteration ...

### Example runs and results

#### ex 1

content: images/inputs/content/Dipping-Sun.jpg, w=1920, h=1076
style:   images/inputs/style/starry_night.jpg, w=1024, h=640
out:     images/outputs/bcmtests/ex1/Dipping-starry*, w=713, h=400

```bash
$ python3 INetwork.py ./images/inputs/content/Dipping-Sun.jpg ./images/inputs/style/starry_night.jpg images/output/bcmtests/ex1/Dipping-starry
...
Iteration 10 completed in 126s
```
images
* content: [Dipping-sun](images/inputs/content/Dipping-Sun.jpg)
* style: [starry_night](images/inputs/style/starry_night.jpg)
* [Dipping-starry_1](images/output/bcmtests/ex1/Dipping-starry_at_iteration_1.png)
* [Dipping-starry_5](images/output/bcmtests/ex1/Dipping-starry_at_iteration_5.png)
* [Dipping-starry_10](images/output/bcmtests/ex1/Dipping-starry_at_iteration_10.png)

#### ex 2

content: images/bcmNST/content/flowers/IMG_9610.jpg, w=768, h=768
style:   images/bcmNST/style/style-flowers-various/abstract-flowers-tint.jpg, w=719, h=720
out: images/outputs/bcmtests/ex2/flowers-9610-tint*, w=400, h=400

```bash
$ python3 INetwork.py ./images/bcmNST/content/flowers/IMG_9610.jpg ./images/bcmNST/style/style-flowers-various/abstract-flowers-tint.jpg images/output/bcmtests/ex2/flowers-9610-tint
...
Iteration 10 completed in 72s
```
images
* content: [flowers-9610](images/bcmNST/content/flowers/IMG_9610.jpg)
* style: [abstract_flowers_tint](images/bcmNST/style/style-flowers-various/abstract-flowers-tint.jpg)
* [flowers-9610-tint_1](images/output/bcmtests/ex2/flowers-9610-tint_at_iteration_1.png)
* [flowers-9610-tint_5](images/output/bcmtests/ex2/flowers-9610-tint_at_iteration_5.png)
* [flowers-9610-tint_10](images/output/bcmtests/ex2/flowers-9610-tint_at_iteration_10.png)

##### ex 2_1
flowers with watercolor style

$ python3 INetwork.py ./images/bcmNST/content/flowers/IMG_9610.jpg ./images/bcmNST/style/style-watercolor/treelined-street.png images/output/bcmtests/ex2/flowers-9610-watercolor

### Example runs and results with parameter exploration

* --num_iter # control iterations for quicker testing
* --image_size
* --style_wieght
* --total_variation_weight
* --content_loss_type [0, 1, 2]
* --rescale_image
* --rescale_method
* --maintain_aspect_ratio
* --pool_type [max, avg]
* --preserve_color

#### ex 3

##### ex3_1:
default args

* content: [santafe-9429](images/bcmNST/content/nmpics/IMG_9429.jpg), w=5472, h=3648
* style:   [monet-magpie](images/bcmNST/style/style-monet/style-monetmagpie-400x267.jpg), w=400, h=267
* out:     images/output/bcmtests/ex3/santafe-9429-monetmagpie_1*, , w=600, h=400

```bash
$ python3 INetwork.py ./images/bcmNST/content/nmpics/IMG_9429.jpg images/bcmNST/style/style-monet/style-monetmagpie-400x267.jpg images/output/bcmtests/ex3/santafe-9429-monetmagpie_1
...
Iteration 1 completed in 106s
```

output images
* [santafe-9429-monetmagpie_1](images/output/bcmtests/ex3/santafe-9429-monetmagpie_1_at_iteration_1.png)
* [santafe-9429-monetmagpie_5](images/output/bcmtests/ex3/santafe-9429-monetmagpie_1_at_iteration_.png)
* [santafe-9429-monetmagpie_10](images/output/bcmtests/ex3/santafe-9429-monetmagpie_1_at_iteration_10.png)

##### ex4: 
default args

* content: [santafe-9429](images/bcmNST/content/nmpics/IMG_9429.jpg), w=5472, h=3648
* style:   [watercolor-treelinedstreet](ls images/bcmNST/s
tyle/style-watercolor/treelined-street.png), w=400, h=600
* out:     images/output/bcmtests/ex4/santafe-9429-watercolor*, w=600, 400

```bash
$ python3 INetwork.py ./images/bcmNST/content/nmpics/IMG_9429.jpg images/bcmNST/style/style-watercolor/treelined-street.png images/output/bcmtests/ex4/santafe-9429-watercolor
...
Iteration 1 completed in 109s
```

output images
* [santafe-9429-watercolor_1](images/output/bcmtests/ex4/santafe-9429-watercolor_at_iteration_1.png)
* [santafe-9429-watercolor_5](images/output/bcmtests/ex4/santafe-9429-watercolor_at_iteration_.png)
* [santafe-9429-watercolor_10](images/output/bcmtests/ex4/santafe-9429-watercolor_at_iteration_10.png)

##### ex5: 
default args

* content: [santafe-9429](images/bcmNST/content/nmpics/IMG_8622.jpg), w=5472, h=2605
* style:   [watercolor-treelinedstreet](ls images/bcmNST/s
tyle/style-watercolor/treelined-street.png), w=400, h=600
* out:     images/output/bcmtests/ex4/santafe-8622-watercolor* w=840, h=400

```bash
$ python3 INetwork.py ./images/bcmNST/content/nmpics/IMG_8622.jpg images/bcmNST/style/style-watercolor/treelined-street.png images/output/bcmtests/ex5/santafe-8622-watercolor
...
Iteration 1 completed in 143s
```

Terminated early (6 images)
output images
* [santafe-8622-watercolor_1](images/output/bcmtests/ex5/santafe-8622-watercolor_at_iteration_1.png)
* [santafe-8622-watercolor_5](images/output/bcmtests/ex5/santafe-8622-watercolor_at_iteration_5.png)

try the above with some params ... 
* --num_iter # control iterations for quicker testing
* --image_size
* --style_weight
* --total_variation_weight
* --content_loss_type [0, 1, 2]
* --rescale_image
* --rescale_method
* --maintain_aspect_ratio
* --pool_type [max, avg]
* --preserve_color

ex 5_2:
First, preserve color

$ python3 INetwork.py ./images/bcmNST/content/nmpics/IMG_8622.jpg images/bcmNST/style/style-watercolor/treelined-street.png images/output/bcmtests/ex5/santafe-8622-watercolor-preservecolor --preserve_color ./images/bcmNST/content/nmpics/IMG_8622.jpg
...
Iteration 1 completed in 141s

output images
* [santafe-8622-watercolor-preservecolor_1](images/output/bcmtests/ex5/santafe-8622-watercolor-preservecolor_at_iteration_1.png)
* [santafe-8622-watercolor-preservecolor_5](images/output/bcmtests/ex5/santafe-8622-watercolor-preservecolor_at_iteration_5.png)
* [santafe-8622-watercolor-preservecolor_10](images/output/bcmtests/ex5/santafe-8622-watercolor-preservecolor_at_iteration_10.png)

ex5_3:
rescale to original content size

$ python3 INetwork.py ./images/bcmNST/content/nmpics/IMG_8622.jpg images/bcmNST/style/style-watercolor/treelined-street.png images/output/bcmtests/ex5/santafe-8622-watercolor-resize --rescale_image true
...
Rescaling Image to (2605, 5472)
...
Iteration 1 completed in 232s

Terminated Early (2 images)
output images
* [santafe-8622-watercolor-resize_1](images/output/bcmtests/ex5/santafe-8622-watercolor-resize_at_iteration_1.png)
* [santafe-8622-watercolor-resize_2](images/output/bcmtests/ex5/santafe-8622-watercolor-resize_at_iteration_2.png)

ex5_4:
vgg19 model, 3 iterations

$ python3 INetwork.py ./images/bcmNST/content/nmpics/IMG_8622.jpg images/bcmNST/style/style-watercolor/treelined-street.png images/output/bcmtests/ex5/santafe-8622-watercolor-vgg19 --model vgg19 --num_iter 10
...
Iteration 1 completed in 167s

output images
* [santafe-8622-watercolor-vgg19_1](images/output/bcmtests/ex5/santafe-8622-watercolor-vgg19_at_iteration_1.png)
* [santafe-8622-watercolor-vgg19_5](images/output/bcmtests/ex5/santafe-8622-watercolor-vgg19_at_iteration_5.png)
* [santafe-8622-watercolor-vgg19_10](images/output/bcmtests/ex5/santafe-8622-watercolor-vgg19_at_iteration_10.png)

ex5_5:
vgg19 model, conv5_1 content layer, 3 iterations

$ python3 INetwork.py ./images/bcmNST/content/nmpics/IMG_8622.jpg images/bcmNST/style/style-watercolor/treelined-street.png images/output/bcmtests/ex5/santafe-8622-watercolor-vgg19-conv51 --model vgg19 --content_layer conv5_1 --num_iter 3
...
Iteration 1 completed in 166s

output images
* [santafe-8622-watercolor-vgg19-conv51_1](images/output/bcmtests/ex5/santafe-8622-watercolor-vgg19-conv51_at_iteration_1.png)
* [santafe-8622-watercolor-vgg19-conv51_5](images/output/bcmtests/ex5/santafe-8622-watercolor-vgg19-conv51_at_iteration_5.png)
* [santafe-8622-watercolor-vgg19-conv51_10](images/output/bcmtests/ex5/santafe-8622-watercolor-vgg19-conv51_at_iteration_10.png)

Look deeper into this with background:
https://towardsdatascience.com/extract-features-visualize-filters-and-feature-maps-in-vgg16-and-vgg19-cnn-models-d2da6333edd0

ex 5_6:
vgg16 model 3 iterations
with xxx style

$ python3 INetwork.py ./images/bcmNST/content/nmpics/IMG_8622.jpg images/inputs/style/japanese_painting.jpg images/output/bcmtests/ex5/santafe-8622-japanese --num_iter 3
...
Iteration 1 completed in 141s

output images
* [santafe-8622-japanese_1](images/output/bcmtests/ex5/santafe-8622-japanese_at_iteration_1.png)
* [santafe-8622-japanese_3](images/output/bcmtests/ex5/santafe-8622-japanese_at_iteration_3.png)