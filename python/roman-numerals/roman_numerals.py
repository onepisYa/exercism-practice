# I，V，X，L，C，D，M
# I 1
# V 5
# X 10
# L 50 
# C 100
# D 500
# M 1000

R_dic={1000: 'M',900: 'CM',500: 'D',400: 'CD',
       100: 'C',90: 'XC',50: 'L',40: 'XL',
       10: 'X',9: 'IX',5: 'V',4: 'IV',
       1: 'I'}

# I thought about it for a long time, and I didn’t think of a better way than this. I admire the people who came up with this idea.
def roman(number):
    result=''
    if R_dic.get(number,None):
        return R_dic.get(number)
    for int_nu in R_dic:
        while number>=int_nu:
                result+=R_dic.get(int_nu)
                number-=int_nu
                
    return result

