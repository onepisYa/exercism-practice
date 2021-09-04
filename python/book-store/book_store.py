from collections import Counter
from itertools import product
PRICES = {1: 800, 2: 1600 * 0.95, 3: 2400 * 0.90, 4: 3200 * 0.80, 5: 4000 * 0.75}
def total(basket):
    def total_in(basket):
        while len(basket)>0:
            s=set(basket)
            yield s
            [basket.remove(i) for i in s]
            
    new_basket=basket.copy()
    price_li=[PRICES[len(i)] for i in total_in(basket)]
    total_price=sum(price_li) 
    if len(set(new_basket))==5 and len(new_basket)%8==0:
        total_price-=5*len(new_basket)
    elif PRICES[5] in price_li and PRICES[3] in price_li:
        min_=min(price_li.count(PRICES[5]),price_li.count(PRICES[3]))
        total_price=min_*PRICES[4]*2+PRICES[len(new_basket)-min_*2*4]
    return total_price