import numpy as np
from collections import Counter
import itertools
from visual import show_tfidf   # this refers to visual.py in my [repo](https://github.com/AvicenaIG/NLP-Tutorials/)

docs = [
]

docs_words = [d.replace(",", "").split(" ") for d in docs]
vocab = set(itertools.chain(*docs_words))
v2i = {v: i for i, v in enumerate(vocab)}
i2v = {i: v for v, i in v2i.items()}


def safe_log(x):
    pass  # TODO: implement


tf_methods = {
idf_methods = {


def get_tf(method="log"):
    pass  # TODO: implement



def get_idf(method="log"):
    pass  # TODO: implement



def cosine_similarity(q, _tf_idf):
    pass  # TODO: implement


def docs_score(q, len_norm=False):
    pass  # TODO: implement





def get_keywords(n=2):
    pass  # TODO: implement


tf = get_tf()           # [n_vocab, n_doc]
idf = get_idf()         # [n_vocab, 1]
tf_idf = tf * idf       # [n_vocab, n_doc]
print("tf shape(vecb in each docs): ", tf.shape)
print("\ntf samples:\n", tf[:2])
print("\nidf shape(vecb in all docs): ", idf.shape)
print("\nidf samples:\n", idf[:2])
print("\ntf_idf shape: ", tf_idf.shape)
print("\ntf_idf sample:\n", tf_idf[:2])


# test
get_keywords()
q = "I get a coffee cup"
scores = docs_score(q)
d_ids = scores.argsort()[-3:][::-1]
print("\ntop 3 docs for '{}':\n{}".format(q, [docs[i] for i in d_ids]))

show_tfidf(tf_idf.T, [i2v[i] for i in range(tf_idf.shape[0])], "tfidf_matrix")