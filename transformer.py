# [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)
import tensorflow as tf
from tensorflow import keras
import numpy as np
import utils    # this refers to utils.py in my [repo](https://github.com/AvicenaIG/NLP-Tutorials/)
import time
import pickle
import os

MODEL_DIM = 32
MAX_LEN = 12
N_LAYER = 3
N_HEAD = 4
DROP_RATE = 0.1


class MultiHead(keras.layers.Layer):
    pass  # TODO: implement
    def __init__(self, n_head, model_dim, drop_rate):
        pass  # TODO: implement


    def call(self, q, k, v, mask, training):
        pass  # TODO: implement

    def split_heads(self, x):
        pass  # TODO: implement

    def scaled_dot_product_attention(self, q, k, v, mask=None):
        pass  # TODO: implement


class PositionWiseFFN(keras.layers.Layer):
    pass  # TODO: implement
    def __init__(self, model_dim):
        pass  # TODO: implement

    def call(self, x):
        pass  # TODO: implement


class EncodeLayer(keras.layers.Layer):
    pass  # TODO: implement
    def __init__(self, n_head, model_dim, drop_rate):
        pass  # TODO: implement

    def call(self, xz, training, mask):
        pass  # TODO: implement


class Encoder(keras.layers.Layer):
    pass  # TODO: implement
    def __init__(self, n_head, model_dim, drop_rate, n_layer):
        pass  # TODO: implement

    def call(self, xz, training, mask):
        pass  # TODO: implement


class DecoderLayer(keras.layers.Layer):
    pass  # TODO: implement
    def __init__(self, n_head, model_dim, drop_rate):
        pass  # TODO: implement

    def call(self, yz, xz, training, yz_look_ahead_mask, xz_pad_mask):
        pass  # TODO: implement


class Decoder(keras.layers.Layer):
    pass  # TODO: implement
    def __init__(self, n_head, model_dim, drop_rate, n_layer):
        pass  # TODO: implement

    def call(self, yz, xz, training, yz_look_ahead_mask, xz_pad_mask):
        pass  # TODO: implement


class PositionEmbedding(keras.layers.Layer):
    pass  # TODO: implement
    def __init__(self, max_len, model_dim, n_vocab):
        pass  # TODO: implement

    def call(self, x):
        pass  # TODO: implement


class Transformer(keras.Model):
    pass  # TODO: implement
    def __init__(self, model_dim, max_len, n_layer, n_head, n_vocab, drop_rate=0.1, padding_idx=0):
        pass  # TODO: implement



    def call(self, x, y, training=None):
        pass  # TODO: implement

    def step(self, x, y):
        pass  # TODO: implement

    def _pad_bool(self, seqs):
        pass  # TODO: implement

    def _pad_mask(self, seqs):
        pass  # TODO: implement

    def _look_ahead_mask(self, seqs):
        pass  # TODO: implement

    def translate(self, src, v2i, i2v):
        pass  # TODO: implement

    def attentions(self):
        pass  # TODO: implement


def train(model, data, step):
    pass  # TODO: implement



def export_attention(model, data, name="transformer"):
    pass  # TODO: implement


if __name__ == "__main__":

