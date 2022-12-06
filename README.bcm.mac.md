

$ python3.9 -m venv ~/DEV/pythonenvs/nst-doodle
$ . ~/DEV/pythonenvs/nst-doodle/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements_tf.txt
$ pip install tensorflow_probability
$ pip install imageio
$ pip install skikit-image
$ pip install keras
$ pip install tensorflow

comment out line in INetwork.py

# from keras.utils.layer_utils import convert_all_kernels_in_model

fix syntax warnings in INetwork.py

    # if improvement_threshold is not 0.0:
    #     if improvement < improvement_threshold and improvement is not 0.0:
    if improvement_threshold != 0.0:
        if improvement < improvement_threshold and improvement != 0.0:

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

See
https://stackoverflow.com/questions/66221788/tf-gradients-is-not-supported-when-eager-execution-is-enabled-use-tf-gradientta

Add
K.tf.compat.v1.disable_eager_execution()

(nst-doodle) (base) brucemoxon@tigrisbrucis Neural-Style-Transfer % python3 INetwork.py ./images/inputs/content/Dipping-Sun.jpg ./images/inputs/style/starry_night.jpg bcmtest
...
File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/keras/engine/keras_tensor.py", line 284, in __array__
    f"You are passing {self}, an intermediate Keras symbolic "
  File "/Users/brucemoxon/DEV/pythonenvs/nst-doodle/lib/python3.9/site-packages/keras/engine/keras_tensor.py", line 329, in __str__
    return "KerasTensor(type_spec=%s%s%s%s)" % (
RecursionError: maximum recursion depth exceeded while calling a Python object