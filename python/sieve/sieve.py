
# 2
# 870 ms  14.1 ms per loop (mean  std. dev. of 7 runs, 1 loop each)
# primes_1(1000000) 
from math import sqrt
def primes_1(limit):
   if limit<2:
       return []
   primes=list(range(limit+1))
   # filter the duplicate -> last 
   last=int(sqrt(limit))
   for ele in range(last+1):
       if ele>=2:
           tmp=ele*2
           while tmp<=limit:
               primes[tmp]=0
               tmp+=ele
       else:
           continue
   else:
       primes[1]=0
   return [i for i in primes if i is not 0]

# ----------------------------------
# 1 fast
# primes(1000000) 
# 17.6 ms  107 µs per loop (mean  std. dev. of 7 runs, 100 loops each)
import numpy as np

def primes(limit):
    if limit<2:
        return []
    primes=np.arange(limit+1)
    last=int(np.sqrt(limit))
    for ele in range(2,last+1):
        primes[2*ele::ele]=0
    return primes[2:][primes[2:]!=0].tolist()

# ----------------------------------------------
# 3 
# 933 ms  17.8 ms per loop (mean  std. dev. of 7 runs, 1 loop each)
# primes_2(1000000)
from functools import reduce
from math import sqrt


def primes_2(limit):
    if limit<2:
        return []

    def handle(seq, idx):
        tmp = 2 * idx
        while tmp <= limit:
            seq[tmp] = 0
            tmp += idx
        return seq


    seq = list(range(limit + 1))
    last = int(sqrt(limit))
    return [prime for prime in reduce(handle, range(2,last + 1), seq) if prime not in [1,0]]

    # return [*filter(lambda x:x not in (0,1),reduce(handle, range(last + 1), seq))]
