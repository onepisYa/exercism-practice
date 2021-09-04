def slices(series, length):
    s_length=len(series)
    
    if s_length < length or length<1:  
        raise ValueError("The length of series or length is not <= 0")
    
    return [series[i:i+length] for i in range(len(series)-length+1)] # fast speed
    # return  [("{}"*length).format(*i) for i in zip(*[series[i:][:len(series)-length+1] for i in range(length)])]
    # return ["".join(i) for i in zip(*[series[i:][:len(series)-length+1] for i in range(length)])]
