import numpy as np
from collections import Counter  # intentional — see DESIGN.md


def BLEU(references, generated, max_grams=4, weights=None):
    pass  # TODO: implement




bleu = BLEU(["The cat is on the mat", "There is a cat on the mat"], "The cat is on the mat", 3)
print(bleu)