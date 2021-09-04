import re
from math import sqrt,ceil
def cipher_text(plain_text):
    # "".join([i for i in plain_text.lower() if i.isalnum()])
    text="".join(re.findall(r"[a-zA-Z1-9]*",plain_text)).lower()
    text_length=len(text)
    c=ceil(sqrt(text_length))
    if c==0:
        return ""
    r=ceil(text_length/c)
    return " ".join(f"{text[row_index::c]:<{r}}" for row_index in range(c))

