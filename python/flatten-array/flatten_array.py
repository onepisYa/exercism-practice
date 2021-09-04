# 1. Common Implementation
def flatten_(iterable):
    result=[]
    def _flatten(iterable):
        [_flatten(el) if isinstance(el,list) else result.append(el) for el in iterable if el is not None]
    _flatten(iterable)
    return result


# 2. generator implementation 
def generator_flatten(iterable):
    def _flatten(lst):
        for i in lst:
            if type(i)==list:
                yield from _flatten(i)
            elif i is not None:
                yield i
    return list(_flatten(iterable))


# 3. star expression implementation
def flatten__star(iterable,result=None):
    if result is None:
        result=[]
    flag=0
    for el in iterable:
        if isinstance(el,list):
            result=[*result,*el]
            flag+=1 
        elif el is not None:
            result.append(el)
    else:
        if flag==0:
            return result
        
    return flatten(result)

# 4.
def flatten(iterable):
    result=[]
    flag=0
    for el in iterable:
        if isinstance(el,list):
            result.extend(el)
            flag+=1
        elif el is not None:
            result.append(el)
    else:
        if flag==0:
            return result
    return flatten(result)
