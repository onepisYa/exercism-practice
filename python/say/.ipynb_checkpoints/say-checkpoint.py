from functools import partial
import sys
# sys.setrecursionlimit(100000)
# set recursion depth
ones = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]
tens = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
    'ninety'
]
def memo(f):
    """ return a single param function of f """
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized
    
def say_r(n):
    template=partial(lambda x,str_x,n:" ".join(([say(n//x),str_x ,say(n%x)] if n%x>0 else [say(n//x),str_x])).strip(),n=n)
    if 0>n or n>=1000000000000:
        raise ValueError("the value are out of range ! ")
    if 0<= n < 20:
        return ones[n]
    elif n < 100:
            return tens[n//10]+"-"+ones[n%10] if n%10>0 else  tens[n//10]
    elif n<1000:
        return template(100,"hundred")
    elif n<1000000:
        return template(1000,'thousand')
    elif n<1000000000:
        return template(1000000,"million")
    elif n<1000000000000:
        return template(1000000000,"billion")
        

    
say=memo(say_r)
