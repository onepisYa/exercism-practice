def square(number):
    if number<1 or number>64:
        raise ValueError("min number is 1 and max number is 64")
    return 2**(number-1)


def total():
    '''
    64 is number of board's square
    '''
    return int("0b"+"1"*64,2)
