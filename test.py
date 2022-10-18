# # import os
# # os.environ["PATH"] += os.pathsep + 'D:/compiler/Graphviz/bin'
#
# import tensorflow as tf
# # sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
#
# import os
#
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
#
# gpu_options = tf.GPUOptions(allow_growth=True)
# sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
#
# import tensorflow as tf
# print(tf.__version__)
# import tensorflow-gpu


from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

