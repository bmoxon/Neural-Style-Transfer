

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


Try adding the gradient tape ...

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

Back to original gradient computation, with eager execution disabled up at the top (before
first Keras call)

# bcm
# for eager execution disabling in TF2
# https://github.com/tensorflow/tensorflow/issues/33135
# doesnt seem to work ... recursion depth/infinite recursion??
K.tf.compat.v1.disable_eager_execution()

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

~ 2 min 1 iteration ...