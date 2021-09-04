import string
def rotate(text, key):
    key=key%26
    chars=string.ascii_lowercase
    new_chars=chars[key:]+chars[:key]
    trans=str.maketrans(chars+chars.upper(),new_chars+new_chars.upper()) 
    return text.translate(trans)
