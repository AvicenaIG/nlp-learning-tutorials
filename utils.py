import numpy as np
import datetime
import os
import requests
import pandas as pd
import re
import itertools

PAD_ID = 0


class DateData:
    pass  # TODO: implement
    def __init__(self, n):
        pass  # TODO: implement

    def sample(self, n=64):
        pass  # TODO: implement

    def idx2str(self, idx):
        pass  # TODO: implement

    def num_word(self):
        pass  # TODO: implement


def pad_zero(seqs, max_len):
    pass  # TODO: implement


def maybe_download_mrpc(save_dir="./MRPC/", proxy=None):
    pass  # TODO: implement


def _text_standardize(text):
    pass  # TODO: implement


def _process_mrpc(dir="./MRPC", rows=None):
    pass  # TODO: implement


class MRPCData:
    pass  # TODO: implement

    def __init__(self, data_dir="./MRPC/", rows=None, proxy=None):
        pass  # TODO: implement




    def sample(self, n):
        pass  # TODO: implement

    def num_word(self):
        pass  # TODO: implement

    def mask_id(self):
        pass  # TODO: implement


class MRPCSingle:
    pass  # TODO: implement

    def __init__(self, data_dir="./MRPC/", rows=None, proxy=None):
        pass  # TODO: implement


    def sample(self, n):
        pass  # TODO: implement

    def num_word(self):
        pass  # TODO: implement


class Dataset:
    pass  # TODO: implement
    def __init__(self, x, y, v2i, i2v):
        pass  # TODO: implement

    def sample(self, n):
        pass  # TODO: implement

    def num_word(self):
        pass  # TODO: implement


def process_w2v_data(corpus, skip_window=2, method="skip_gram"):
    pass  # TODO: implement





def set_soft_gpu(soft_gpu):
    pass  # TODO: implement
