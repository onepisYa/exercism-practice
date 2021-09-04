def convert(number):
    """
    >>> convert(5)
    'Plang'
    >>> convert(1)
    '1'
    >>> convert(49)
    'Plong'
    >>> convert(52)
    '52'
    """
    drops = {3: "Pling", 5: "Plang", 7: "Plong"}
    return "".join((drops[i] for i in drops if number % i == 0)) or str(number)
