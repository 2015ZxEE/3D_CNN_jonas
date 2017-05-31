# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# #############################################################################
# This is an implementaion of Convolutional Neural Netwroks for 3D volumes.
# The code is a modification of the code provided in TensorFlow tutorials for
# CIFAR-10 dataset.
# For help, please refer to the 'readme' file
# The code is modifed by: Mohamed ElMikaty
# Last update: 14 Dec 16
################################################################################
""" This module contains configurations for the dataset, training and evaluation
    procedures.
"""

cfg = {'batch_size'    : 10,    # number of examples in a batch
        'height'       : 8,    # height of the 3D volume
        'width'        : 12,    # width of the 3D volume
        'depth'        : 100,    # depth of the 3D volume
        'nChan'        : 2,     # number of colour channels
        'nClass'       : 8,    # number of classes
        'nTrain'       : 280, # number of training examples
        'nEval'        : 10896, # number of evaluation examples
        'nBatchBin'    : 8,     # number of binary files for training data
        'data_dir'     : '3D',   # please specify full path
        'train_ckpt_dir' : 'train', # please specify full path
        'eval_ckpt_dir'  : 'eval', # please specify full path
        'MOVING_AVERAGE_DECAY'       : 0.9999, # The decay to use for the moving average.
        'NUM_EPOCHS_PER_DECAY'       : 350.0,  # Epochs after which learning rate decays.
        'LEARNING_RATE_DECAY_FACTOR' : 0.1,    # Learning rate decay factor.
        'INITIAL_LEARNING_RATE'      : 0.1,    # Initial learning rate.
        'max_steps'                  : 2000,
        'eval_interval_secs'         : 60 * 5
        }
