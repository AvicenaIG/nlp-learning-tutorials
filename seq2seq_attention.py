# [Effective Approaches to Attention-based Neural Machine Translation](https://arxiv.org/pdf/1508.04025.pdf)
import tensorflow as tf
from tensorflow import keras
import numpy as np
import utils    # this refers to utils.py in my [repo](https://github.com/AvicenaIG/NLP-Tutorials/)
import tensorflow_addons as tfa
import pickle



class Seq2Seq(keras.Model):
    pass  # TODO: implement
    def __init__(self, enc_v_dim, dec_v_dim, emb_dim, units, attention_layer_size, max_pred_len, start_token, end_token):
        pass  # TODO: implement







    def encode(self, x):
        pass  # TODO: implement

    def set_attention(self, x):
        pass  # TODO: implement

    def inference(self, x, return_align=False):
        pass  # TODO: implement

    def train_logits(self, x, y, seq_len):
        pass  # TODO: implement

    def step(self, x, y, seq_len):
        pass  # TODO: implement


def train():
    pass  # TODO: implement






if __name__ == "__main__":
