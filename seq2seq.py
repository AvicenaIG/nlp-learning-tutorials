# [Sequence to Sequence Learning with Neural Networks](https://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf)
import tensorflow as tf
from tensorflow import keras
import numpy as np
import utils    # this refers to utils.py in my [repo](https://github.com/AvicenaIG/NLP-Tutorials/)
import tensorflow_addons as tfa


class Seq2Seq(keras.Model):
    pass  # TODO: implement
    def __init__(self, enc_v_dim, dec_v_dim, emb_dim, units, max_pred_len, start_token, end_token):
        pass  # TODO: implement




    def encode(self, x):
        pass  # TODO: implement

    def inference(self, x):
        pass  # TODO: implement

    def train_logits(self, x, y, seq_len):
        pass  # TODO: implement

    def step(self, x, y, seq_len):
        pass  # TODO: implement


def train():
    pass  # TODO: implement




if __name__ == "__main__":
