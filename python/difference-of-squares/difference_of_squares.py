def square_of_sum(number):
    """
    1+....+n=(1+n)*n*0.5
    """
    return sum([(number+1)*number*0.5])**2


def sum_of_squares(number):
    """
    1**2 + 2**2 + ... + n**2 = n*(n+1)*(2n+1)/6
    """
    return number*(number+1)*(2*number+1)/6 


def difference_of_squares(number):
    return square_of_sum(number)-sum_of_squares(number)
    
