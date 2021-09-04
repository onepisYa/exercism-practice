from re import sub
def decode(string):
    return sub(r"(?P<int>\d+)(?P<letter>[a-zA-Z\s])",lambda x:int(x.group("int"))*x.group("letter"),string)


def encode(string):
    return sub(r"(?P<dup>.)\1+",lambda x:str(len(x.group()))+x.group("dup"),string)

