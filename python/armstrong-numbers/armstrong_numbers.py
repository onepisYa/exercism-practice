def is_armstrong_number(number):
    num_li=list(str(number))
    exp_=len(num_li)
    return number==sum(int(i)**exp_ for i in num_li)
