#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 11:54:27 2017
@author: utkrist
"""

"""
TODO:    
    (*) Model embedding for unk
    (*) learning rate decay
"""
#%reload_ext autoreload
#%autoreload 2

import os
import sys
import math
import time
import argparse
import numpy as np
from random import shuffle

cluster   = "/home/IAIS/uadhikari/projects/thesis_clean"
alienware = "/home/utkrist/Desktop/thesis_clean"

base_path = cluster
checkpoint_dir = base_path + '/results/checkpoint'
data_path = base_path + "/data/conlldata/processed_data"

train_file_pattern = None
dev_file_pattern = None
emb_file = None
map_file = None
rand_vec_file = None
IS_CHIEF = None
CHKPT_DIR = None
DATA_SOURCES = {}
SAVER = None
LOAD_EPOCH = 0
LOAD_BATCH = 0
LOAD_GLOBAL_STEP = 0
LOAD_HIST_FILE = None

parser = argparse.ArgumentParser()
# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
parser.register('type','bool', (lambda x:x.lower() in ('yes', 'true', 't', '1')))

# Architecture related options
parser.add_argument("--model_type", type=str)
parser.add_argument("--num_layers", type=int)
parser.add_argument("--num_uni_layers",   default=1, type=int)
parser.add_argument("--num_bi_layers",   default=1, type=int)
parser.add_argument("--num_hidden", type=int)
parser.add_argument("--out_dim",    default= 129,    type=int)
parser.add_argument("--residual_connection", type='bool', default=False)
parser.add_argument("--dropout", default=0, type=float)

# Optimizer relate options
parser.add_argument("--loss", default='softmax', type=str)
parser.add_argument("--lr",   default= 0.001,   type=float)
parser.add_argument("--optimizer", default='adam', type=str)
parser.add_argument("--epsilon", type=float, default=1e-6)
parser.add_argument("--rho",     type=float, default=0.95)

# Gradient related options
parser.add_argument("--clip_gradient", type='bool', default=False)
parser.add_argument("--grad_norm_thresh", type=float, default=1.0)

# Model running options
parser.add_argument("--num_epochs",  default= 101,     type=int)
parser.add_argument("--batch_size", default= 128,    type=int)
parser.add_argument("--mode",       default='train', type=str, help='train')

# Checkpointing and reporting
parser.add_argument("--model_name",      default='', type=str, help='name of the model')
parser.add_argument("--report_every_batch", default=100, type=int)
parser.add_argument("--checkpoint_dir",  default=checkpoint_dir, type=str)
parser.add_argument("--checkpoint_freq",  default=2, type=int)
parser.add_argument("--resume_training", type='bool', default=False)
parser.add_argument("--load_checkpoint_filename", default="", type=str)

# Embeddings aand input related options
parser.add_argument("--embedding_trainable", type='bool', default=False)
parser.add_argument("--embedding_name",  type=str)
parser.add_argument("--emb_dim", type=int)
parser.add_argument("--input_file_suffix",  type=str)

# Extra Options
parser.add_argument("--gpu_id",   default= 0, type=int)
parser.add_argument("--cpu_only", type='bool', default=False)
parser.add_argument("--debug",  type='bool', default=False)
parser.add_argument('--only_words', type='bool', default=False)

FLAGS = parser.parse_args()