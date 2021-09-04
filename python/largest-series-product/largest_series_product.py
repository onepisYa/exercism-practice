from functools import reduce
def largest_product(series, size):
    def mul_(seq):
        return reduce(lambda a,b:a*b,seq,1)

    seq_len=len(series)
    if size>seq_len or size<0:
        raise ValueError("the size>series of length , Value Error")
    str_=series
    seq=[int(i) for i in str_]
    return max(mul_(seq[i:i+size]) for i in range(seq_len-size+1))


# If you don't want to import reduce 
# use this series_product
def series_product(series):
    product = 1
    for char in series:
       product *= int(char) 
    return product
