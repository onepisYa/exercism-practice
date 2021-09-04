# from collections import defaultdict
from collections import Counter
import re

# import string
# >>> string.punctuation
# output '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# \b  boundary


def count_words(sentence):
    word_list = [
        i.strip("\'\"").lower() for i in re.findall(r"[\da-zA-Z']+", sentence)
    ]
    # word_count = defaultdict(int)
    # for i in word_list:
    #     word_count[i] += 1
    # return dict(word_count)
    return dict(Counter(word_list))
