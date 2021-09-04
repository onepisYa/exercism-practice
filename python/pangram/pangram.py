from collections import Counter
import numpy as np
import string
def is_pangram(sentence):
    ct=Counter(sentence.lower()).keys()
    return bool(np.in1d(np.array(list(string.ascii_lowercase)),np.array(list(ct))).all())