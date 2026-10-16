# nlp-learning-tutorials — Hands-On AI Education for NLP & Deep Learning Models

![License](https://img.shields.io/badge/license-MIT-blue) ![Version](https://img.shields.io/badge/version-0.1.0-green) ![Language](https://img.shields.io/badge/language-Python-yellow)

Learn natural language processing by building it yourself — from word embeddings to Transformer, BERT, GPT, and ELMo, with clear, minimal, classroom-ready implementations in both TensorFlow and PyTorch.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Model Configuration](#model-configuration)
- [Repository Layout](#repository-layout)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Learn Word2Vec from scratch** — train Continuous Bag of Words (`CBOW`) and Skip-Gram (`SkipGram`) models to understand how words become vectors.
- **Study sequence-to-sequence learning** — implement `Seq2Seq` with and without attention (`seq2seq.py`, `seq2seq_attention.py`) for translation-style tasks, plus a CNN language model (`CNNTranslation`).
- **Build the Transformer block by block** — every component is exposed for teaching: `MultiHead` attention, `PositionWiseFFN`, `PositionEmbedding`, `EncoderLayer`/`DecoderLayer`, and the full `Encoder`/`Decoder`/`Transformer`.
- **Explore pretraining objectives** — run BERT-style masked language modeling with interchangeable masking strategies (`do_mask`, `do_replace`, `do_nothing`, `random_mask_or_replace`) plus next-sentence prediction, and GPT-style autoregressive pretraining.
- **Visualize what the models learn** — export attention weights with `export_attention`, plot word vectors with `show_w2v_word_embedding`, and inspect TensorBoard graphs via `myTensorboard` in the simplified implementations.
- **Compare frameworks side by side** — every core model ships in TensorFlow (`BERT.py`, `GPT.py`, `ELMo.py`, ...) and PyTorch (`pytorch/`), with simplified Keras versions in `simple_realize/` for gentler onboarding.

## Installation

```shell script
git clone https://github.com/AvicenaIG/NLP-Tutorials
cd NLP-Tutorials/
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Quick Start

Train a CBOW word-embedding model — the classic first lesson in any NLP curriculum:

```python
from CBOW import CBOW, train

model = CBOW(
    n_vocab=...,     # vocabulary size
    n_emb=...,       # embedding dimension
    n_hidden=...,    # hidden layer size
    lr=...,          # learning rate
    window=...,      # context window size
)
train(model)
```

## Usage

### Word embeddings for a vocabulary lesson

Train a Skip-Gram model in the PyTorch track and visualize the learned word vectors:

```python
from pytorch.skip_gram import SkipGram, train
from pytorch.visual import show_w2v_word_embedding

model = SkipGram(n_vocab, n_emb, lr, window)
train(model)
show_w2v_word_embedding(model, ...)
```

### Pretraining a BERT-style model

The `BERT` class (in `BERT.py` and `pytorch/BERT.py`) supports masked language modeling with multiple masking strategies and next-sentence prediction:

```python
from BERT import BERT

model = BERT(
    model_dim=...,
    max_len=...,
    n_layer=...,
    n_head=...,
    n_vocab=...,
    lr=...,
)
model.train(...)
```

### Building a Transformer from its parts

The PyTorch Transformer tutorial exposes each layer so students can assemble the architecture themselves:

```python
from pytorch.transformer import (
    MultiHead, PositionWiseFFN, PositionEmbedding,
    EncoderLayer, DecoderLayer, Encoder, Decoder, Transformer, train,
)
```

## Model Configuration

Model constructors accept the following parameters (shown for `BERT` / `GPT`):

| Option | Type | Default | Description |
|---|---|---|---|
| `model_dim` | int | — | Dimensionality of token embeddings and hidden states |
| `max_len` | int | — | Maximum sequence length |
| `n_layer` | int | — | Number of encoder/decoder layers |
| `n_head` | int | — | Number of attention heads |
| `n_vocab` | int | — | Vocabulary size |
| `lr` | float | — | Learning rate |
| `max_seg` | int | `3` | Maximum number of segments |
| `drop_rate` | float | `0.1` | Dropout rate |
| `padding_idx` | int | `0` | Index used for padding tokens |

## Repository Layout

| Path | Contents |
|---|---|
| `CBOW.py`, `skip-gram.py`, `tf_idf.py`, `tf_idf_sklearn.py` | Word-level and search-engine fundamentals |
| `seq2seq.py`, `seq2seq_attention.py`, `cnn-lm.py` | Sequence models and attention |
| `transformer.py`, `GPT.py`, `ELMo.py`, `BERT.py`, `BERT_window_mask.py`, `BLEU.py` | Transformer, pretraining, and evaluation |
| `pytorch/` | PyTorch versions of the above, plus `utils.py` (data helpers like `MRPCData`, `DateData`, `process_w2v_data`) and `visual.py` |
| `simple_realize/` | Simplified Keras implementations (`myTensorboard`, `nce_loss`, `Attention`) for gentler learning |

## Contributing

Contributions that make these tutorials clearer for learners are welcome — whether that's improving explanations, adding visualizations, or polishing existing model implementations. Please keep new examples minimal and consistent with the educational style of the repository.

## License

This project is licensed under the MIT License — © 2026 nlp-learning-tutorials contributors.