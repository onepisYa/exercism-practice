def reverse(text):
    #  1
    # return text[::-1]
    
    #  2
    # return "".join(reversed(text))
    
    #  3
    # text=list(text)
    # text.reverse()
    # return "".join(text)
    
    #  4
#     t=""
#     for i in range(len(text)):
#         t+=text[-(i+1)]
#     return t
    
    #  5
    return "".join([text[-(i+1)] for i in range(len(text))])
    
    

