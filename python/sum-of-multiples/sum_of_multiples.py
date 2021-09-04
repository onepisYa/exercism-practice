# 
def sum_of_multiples(limit, multiples):
    return sum(i for i in range(limit) if any(map(lambda x:not i%x,filter(lambda y:y!=0,multiples))))


# very fast 
def sum_of_multiples1(limit,multiples):
    multiples=[*filter(lambda y:y!=0,multiples)]
    lengthes=map(lambda x:limit//x,multiples)
    result=set()
    for multiple,length in zip(multiples,lengthes):
        result=result.union(iter({multiple*idx if multiple*idx<limit else 0 for idx in range(1,length+1)}))
    return sum(iter(result))


#  code easy
import numpy as np
def sum_of_multiples2(limit,multiples):
    multiples=[*filter(lambda y:y!=0,multiples)]
    if not multiples:
        return 0
    length=limit//min(multiples)
    mul=np.array(multiples,dtype='int')
    result=np.array([],dtype='int')
    for idx in range(1,length+1):
        result=np.concatenate((mul*idx,result),axis=0)
    return np.sum(np.unique(result[result<limit]))
