"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections import Counter
from functools import partial
# Score categories.
# Change the values as you see fit.
YACHT = lambda x:50 if len(set(x))==1 else 0
FULL_HOUSE = lambda x:sum(x) if {3,2}.issubset(Counter(x).values()) else 0
FOUR_OF_A_KIND = lambda x:sum(4*i for i in set(x) if x.count(i)>=4)
LITTLE_STRAIGHT = lambda x:30 if len(set(x))==5 and sum(x)==15 else 0
BIG_STRAIGHT = lambda x:30 if len(set(x))==5 and sum(x)==20 else 0
CHOICE = lambda x:sum(x)
ONES,TWOS,THREES,FOURS,FIVES,SIXES=[partial(lambda x,i:x.count(i)*i,i=i) for i in range(1,7)]


def score(dice, category):
    """
    :dice: list -> like [1,2,3,4,6]
    :category: lambda function
    """
    return category(dice)

