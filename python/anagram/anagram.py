from collections import Counter
import re
def find_anagrams(word, candidates):
    """  
    >>> find_anagrams("Orchestra",["cashregister", "Carthorse", "radishes"])
    ['Carthorse']
    """
    # word_count=Counter(word.upper())
    # return filter(lambda x:Counter(x.upper())==word_count and x.upper()!=word.upper(),candidates)
    # return [i for i in candidates if Counter(i.upper())==word_count and i.upper()!=word.upper()] 
    # return [i for i in candidates if sorted(i.upper())==sorted(word.upper()) and i.upper()!=word.upper()]
    return filter(lambda x:sorted(x.upper())==sorted(word.upper()) and x.upper()!=word.upper(),candidates)
    
