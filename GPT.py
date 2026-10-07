# [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
import tensorflow as tf
from tensorflow import keras
import utils    # this refers to utils.py in my [repo](https://github.com/AvicenaIG/NLP-Tutorials/)
import time
from transformer import Encoder
import pickle
import os


class GPT(keras.Model):
    pass  # TODO: implement
    def __init__(self, model_dim, max_len, n_layer, n_head, n_vocab, lr, max_seg=3, drop_rate=0.1, padding_idx=0):
        pass  # TODO: implement





    def call(self, seqs, segs, training=False):
        pass  # TODO: implement

    def step(self, seqs, segs, seqs_, nsp_labels):
        pass  # TODO: implement

    def input_emb(self, seqs, segs):
        pass  # TODO: implement

    def mask(self, seqs):
        pass  # TODO: implement


    def attentions(self):
        pass  # TODO: implement


def train(model, data, step=10000, name="gpt"):
    pass  # TODO: implement


def export_attention(model, data, name="gpt"):
    pass  # TODO: implement



if __name__ == "__main__":


