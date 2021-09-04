import string
from itertools import cycle
from secrets import randbelow
import re
class Cipher:
    def __init__(self, key=None):
        self.letters=string.ascii_lowercase
        self.key=self.set_key(key)

    def encode(self, text):
        return self.shift(text,derection=1) 

    def decode(self, text):
        return self.shift(text,derection=-1) 

    def shift(self,text,derection):
        result=""
        for k,t in zip(cycle(self.key),text):
            result+=self.letters[(self.letters.index(t)+derection*self.letters.index(k))%26] 
        return result 

    def set_key(self,key):
        if key is None:
            return "".join([self.letters[randbelow(26)] for i in range(100)])
        elif re.fullmatch(r"^[a-z]*",key) and key is not '':
            return key
        else:
            raise ValueError("cipher key is error!")
