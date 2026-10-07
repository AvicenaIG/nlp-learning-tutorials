import tensorflow as tf
from GPT import GPT, train, export_attention
import utils    # this refers to utils.py in my [repo](https://github.com/AvicenaIG/NLP-Tutorials/)


class BERT(GPT):
    pass  # TODO: implement
    def __init__(self, model_dim, max_len, n_layer, n_head, n_vocab, lr, max_seg=3, drop_rate=0.1, padding_idx=0):
        pass  # TODO: implement

    def mask(self, seqs):
        pass  # TODO: implement



if __name__ == "__main__":

