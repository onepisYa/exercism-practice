
VOWEL='aeiou'
VOWEL_LI=['yt','xr']
def translate(text,max_r=0):
    def translate_word(text,max_r=0):
        idx=max_r
        text_len=len(text)
        if text[0] in VOWEL or text[:2] in VOWEL_LI:
            return "".join([text,'ay'])
        elif text[:2] =='qu':
            return "".join([text[2:],'qu','ay'])
        else: 
            if idx>=(text_len-1):
                return text+"ay"
            else:
                return translate_word(text[1:]+text[0],idx+1)

    if len(text.split(" "))<=1:
        return translate_word(text)
    else:
        return " ".join([translate_word(word) for word in text.split(" ")])
