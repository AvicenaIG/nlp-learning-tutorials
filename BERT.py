# [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)
import numpy as np
import tensorflow as tf
import utils    # this refers to utils.py in my [repo](https://github.com/AvicenaIG/NLP-Tutorials/)
import time
from GPT import GPT
import os
import pickle


class BERT(GPT):
    pass  # TODO: implement
    def __init__(self, model_dim, max_len, n_layer, n_head, n_vocab, lr, max_seg=3, drop_rate=0.1, padding_idx=0):
        pass  # TODO: implement


    def step(self, seqs, segs, seqs_, loss_mask, nsp_labels):
        pass  # TODO: implement

    def mask(self, seqs):
        pass  # TODO: implement


def _get_loss_mask(len_arange, seq, pad_id):
    pass  # TODO: implement


def do_mask(seq, len_arange, pad_id, mask_id):
    pass  # TODO: implement


def do_replace(seq, len_arange, pad_id, word_ids):
    pass  # TODO: implement


def do_nothing(seq, len_arange, pad_id):
    pass  # TODO: implement


def random_mask_or_replace(data, arange, batch_size):
    pass  # TODO: implement


def train(model, data, step=10000, name="bert"):
    pass  # TODO: implement


def export_attention(model, data, name="bert"):
    pass  # TODO: implement



if __name__ == "__main__":


