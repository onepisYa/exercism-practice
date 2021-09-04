def factors(value):
    result=[]
    dividend = value
    divisor=2
    while divisor <= dividend:
        while dividend % divisor == 0:
            result.append(divisor)
            dividend/=divisor

        divisor+=1
    return result
