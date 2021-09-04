import re
import string

TRANS=str.maketrans(string.ascii_lowercase,string.ascii_lowercase[::-1]," ")
# the deletechars params of translate is deleter at python3
# now use maketrans third params
# delete whitespace or other chars
def encode(plain_text):
    plain_str=decode(plain_text.lower())
    # trim_str=re.sub("\W|_","",plain_str)
    trim_str=re.sub("[^a-z1-9]+","",plain_str)
    return " ".join(re.findall("\w{1,5}",trim_str))

def decode(ciphered_text):
    return ciphered_text.lower().translate(TRANS)
