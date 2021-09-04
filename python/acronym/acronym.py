import re


def abbreviate(words):
    words_list = [
        i.strip("\'\"").upper()[0] for i in re.findall(r"[\da-zA-Z']+", words)
    ]
    return "".join(words_list)
