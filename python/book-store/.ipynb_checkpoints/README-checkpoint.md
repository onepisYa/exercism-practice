# Book Store

为了促进最受欢迎的5本书系列，销售更多不同的书籍，一家书店决定为购买多本书籍提供折扣。

五本书中的任何一本书的售价均为8美元。

但是，如果您购买了两本不同的书，则这两本书将获得5％的折扣。

如果您购买3本不同的书籍，您将获得10％的折扣。

如果您购买4本不同的书籍，您将获得20％的折扣。

如果您全部购买5本书，则可享受25％的折扣。

注意：如果您购买了四本书，其中三本书是不同的书名，则您可以从构成书集一部分的三本书中获得10％的折扣，但是第四本书仍然要花费$ 8。

您的任务是编写一段代码来计算任何可能的购物篮（仅包含相同系列的书籍）的价格，并提供尽可能多的折扣。

例如，这篮子书要多少钱？

- 2 copies of the first book （两本第一册）
- 2 copies of the second book （两本第二册）
- 2 copies of the third book （两本第三册）
- 1 copy of the fourth book （1本第四册）
- 1 copy of the fifth book （1本第五册）

将这8本书分组的一种方法是：

- 1 group of 5 --> 25% discount (1st,2nd,3rd,4th,5th) （5本）
- +1 group of 3 --> 10% discount (1st,2nd,3rd)  （3本）

这样总共可以得到：

- 5 books at a 25% discount （5本书的 25% 折扣）
- +3 books at a 10% discount （3本书 的 10% 折扣）

结果：

- 5 x (8 - 2.00) == 5 x 6.00 == $30.00
- +3 x (8 - 0.80) == 3 x 7.20 == $21.60

总计 $51.60

但是，将这8本书分组的另一种方法是：

- 1 group of 4 books --> 20% discount  (1st,2nd,3rd,4th) 4本书
- +1 group of 4 books --> 20% discount  (1st,2nd,3rd,5th) 4本书

这样总共可以得到：

- 4 books at a 20% discount （4本书 20%的折扣）
- +4 books at a 20% discount （4本书 20%的折扣）

结果：

- 4 x (8 - 1.60) == 4 x 6.40 == $25.60
- +4 x (8 - 1.60) == 4 x 6.40 == $25.60

总计 $51.20

$51.20 是更好的折扣

## 知识点
### itertools.product(*iteralbes,repeat=1)

大致相当于生成器表达式中的嵌套for循环。

例如， product(A, B) 返回与相同的 ((x,y) for x in A for y in B)

**思路是根据 每个分组 是多少本 来 分组**

**方法 1 ：** 比如  分两组(3本,4本)  (2本，5本)

分几组  根据  相同的书  有 基本。 

比如  第一册 有 3本  那么 在这个案例里面 就可以分三组 

策略就是将 尽可能多的 不一样的书  分成一组 。

**方法 2：**

还有一种就是 利用 set 去重 。 每次  yield 之后  从  列表中删除 。

剩下的再次 set 去重 提取不重复的  再 yield 出去 . 然后根据 事先定义好的价格 就行 计价

然后 排除一些 特例  比如   3+5 和  4+4  4 +4 要便宜

```python

in: print(*product([1,23],[11,22]))
out: (1, 11) (1, 22) (23, 11) (23, 22)
```


嵌套循环像里程表一样循环，在每次迭代中都有最右边的元素前进。这个模式创建一个词典排序，这样，如果输入的iterables被排序，则产品元组将按排序顺序发出。

要用ITerable本身计算ITerable的积，请用可选的 重复 关键字参数。

例如， product(A, repeat=4) 意思与 product(A, A, A, A) .
```python
a=[1,2,3]
bb=product(a,repeat=2)
print(*bb)

out: (1, 1) (1, 2) (1, 3) 
     (2, 1) (2, 2) (2, 3) 
     (3, 1) (3, 2) (3, 3)
    
#######

bb=product(a,repeat=1)
print(*bb)

out: (1,) (2,) (3,)

#######
bb=product(a,repeat=3)
print(*bb)


out：(1, 1, 1) (1, 1, 2) (1, 1, 3) 
     (1, 2, 1) (1, 2, 2) (1, 2, 3) 
     (1, 3, 1) (1, 3, 2) (1, 3, 3) 
        
     (2, 1, 1) (2, 1, 2) (2, 1, 3) 
     (2, 2, 1) (2, 2, 2) (2, 2, 3) 
     (2, 3, 1) (2, 3, 2) (2, 3, 3) 
    
     (3, 1, 1) (3, 1, 2) (3, 1, 3) 
     (3, 2, 1) (3, 2, 2) (3, 2, 3) 
     (3, 3, 1) (3, 3, 2) (3, 3, 3)
    # 1 1 乘以  123  ， 1 2 乘以  1 2 3
    # 一直 到  3 3 
```

### itertools.combinations_with_replacement(iterable, r)

返回 r 输入元素的长度子序列 可迭代的 **允许单个元素重复多次。**

组合元组根据输入的顺序以字典顺序发出 可迭代的 . 所以，如果输入 可迭代的 如果排序，组合元组将按排序顺序生成。

元素根据其位置而不是其值被视为唯一的。因此，如果输入元素是唯一的，生成的组合也将是唯一的。

大致相当于：

也就是说 位置  ab  和 ba  视为 一样的 

```python
def combinations_with_replacement(iterable, r):
    # 我觉得 与 product 的区别 就是  比如  product  1 2 2 有了 之后   2 1 1 还是 会 存在
    # 但是  combinations_with_replacement 去掉了 2 1 1 这类 值。 
    
    
    # example: combinations_with_replacement('ABC', 2) --> 
    # AA AB AC 
    # BB BC 
    # CC
    # combinations_with_replacement('ABC', 3) --> 
    # ('A', 'A', 'A') ('A', 'A', 'B') ('A', 'A', 'C') ('A', 'B', 'B') ('A', 'B', 'C') ('A', 'C', 'C') 
    # ('B', 'B', 'B') ('B', 'B', 'C') ('B', 'C', 'C') 
    # ('C', 'C', 'C')
    # combos=combinations_with_replacement(range(1,6), 2)
    # print(*combos)
    # (1, 1) (1, 2) (1, 3) (1, 4) (1, 5) 
    # (2, 2) (2, 3) (2, 4) (2, 5) 
    # (3, 3) (3, 4) (3, 5)
    # (4, 4) (4, 5) 
    # (5, 5)
    # combos=combinations_with_replacement(range(1,6), 3)
    # print(*combos)
    # (1, 1, 1) (1, 1, 2) (1, 1, 3) (1, 1, 4) (1, 1, 5) (1, 2, 2) (1, 2, 3) (1, 2, 4) (1, 2, 5) (1, 3, 3) (1, 3, 4) (1, 3, 5) (1, 4, 4) (1, 4, 5) (1, 5, 5) 
    # (2, 2, 2) (2, 2, 3) (2, 2, 4) (2, 2, 5) (2, 3, 3) (2, 3, 4) (2, 3, 5) (2, 4, 4) (2, 4, 5) (2, 5, 5) 
    # (3, 3, 3) (3, 3, 4) (3, 3, 5) (3, 4, 4) (3, 4, 5) (3, 5, 5) 
    # (4, 4, 4) (4, 4, 5) (4, 5, 5) 
    # (5, 5, 5)
    
    
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
```
也可以表示为此代码

也可以表示为 product() 在过滤元素不按排序顺序排列的条目（根据它们在输入池pool中的位置）：

比如  1 2 2 存在 

但是 2 1 1 不在了 被过滤掉了

也就是说只有  本身顺序  就是升序 的 才会 存在下来。
```python
def combinations_with_replacement(iterable, r):
    pool = tuple(iterable) # 输入的可迭代 对象 转元组 
    n = len(pool)  # 长度 
    for indices in product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
```
---

## 测试 
证明  8 本书的 时候   4+4 是 最优惠的 

其实 直接  将 价格  个  键 拿过来  加 也是可以的 

```python
from itertools import groupby
PRICES = {1: 8, 2: 16 * 0.95, 3: 24 * 0.90, 4: 32 * 0.80, 5: 40 * 0.75}
bb=list(product(range(1,6),repeat=2))
bb.sort(key=lambda x:sum(x))
li=[]
for i in bb:
    li_=list(i)
    li_.sort()
    li.append(li_)
bb=set([tuple(i) for i in li])  
bb_=[PRICES[l]+PRICES[r] for l,r in bb]
bb=zip(bb,bb_)
cc=groupby(bb,key=lambda x:sum(x[0]))
cc=[{i:list(v)} for i,v in cc]
cc.sort(key=lambda x:list(x.keys())[0]) # 根据键名 排序 


out: # 键为 本数   值 元组 是分组 方式。  数字 是 金额
[{2: [((1, 1), 16)]},
 {3: [((1, 2), 23.2)]},
 {4: [((1, 3), 29.6)]},
 {4: [((2, 2), 30.4)]},
 {5: [((1, 4), 33.6)]},
 {5: [((2, 3), 36.8)]},
 {6: [((3, 3), 43.2)]},
 {6: [((1, 5), 38.0), ((2, 4), 40.8)]},
 {7: [((2, 5), 45.2), ((3, 4), 47.2)]},
 {8: [((4, 4), 51.2)]},
 {8: [((3, 5), 51.6)]},
 {9: [((4, 5), 55.6)]},
 {10: [((5, 5), 60.0)]}]

```

```python
  

from itertools import  groupby,combinations_with_replacement,product
from collections import Counter

PRICES = {0: 0, 1: 8, 2: 16 * 0.95, 3: 24 * 0.90, 4: 32 * 0.80, 5: 40 * 0.75}
bbb=[(PRICES[i]+PRICES[v],(i,v)) for i,v in iter(set([(i,v) for i,v in product([0,1,2,3,4,5],repeat=2)]))]
Counter(bbb)

bbb.sort(key=lambda x:x[0])
bbb=dict(bbb) # 去除 重复 的键
bbb=list(dict(bbb).items())
ccc=[tuple(set(filter(lambda x:sum(x[1])==sum(i[1]),bbb))) for i in bbb]
# list 和 set  都 会报错  
# 我下一步要 去重   set ccc   如果 ccc 里面 是 set  就会 报错
ccc=set(ccc)
# 这里列出了 所有的可能性 相同价格 去除了重复 分两组  
d_=[dict(i) for i in ccc]
d_.sort(key=lambda x:(sum(list(x.values())[0])))
dd_={}
for idx,dic in enumerate(d_):
    dd_.update({idx:{min(dic.keys()):dic[min(dic.keys())]}})
# 输出 dd_
# 可以 看到 8 本的时候  是  4 本 4本  最便宜 。 其他时候都是 最大值 才是最便宜

# ---
dd_
out: {0: (0, 0),
 1: (0, 1),
 2: (2, 0),
 3: (0, 3),
 4: (0, 4),
 5: (0, 5),
 6: (1, 5),
 7: (5, 2),
 8: (4, 4),
 9: (4, 5),
 10: (5, 5)}
# ---
ccc 

out: {((0, (0, 0)),),
 ((8, (0, 1)),),
 ((15.2, (2, 0)), (16, (1, 1))),  #  总共 两本书 的 分组 情况   2 本 和  1 本 ，1本 
 ((23.2, (1, 2)), (21.6, (0, 3))),
 ((25.6, (0, 4)), (29.6, (3, 1)), (30.4, (2, 2))),
 ((30.0, (0, 5)), (36.8, (2, 3)), (33.6, (1, 4))),
 ((43.2, (3, 3)), (38.0, (1, 5)), (40.8, (2, 4))),
 ((45.2, (5, 2)), (47.2, (3, 4))),
 ((51.6, (5, 3)), (51.2, (4, 4))),
 ((55.6, (4, 5)),),
 ((60.0, (5, 5)),)}
 

```

## 本题解决方案

```python
from collections import Counter
from itertools import product
PRICES = {1: 800, 2: 1600 * 0.95, 3: 2400 * 0.90, 4: 3200 * 0.80, 5: 4000 * 0.75}
def total(basket):
    num_books=len(basket)
    unique=len(set(basket))
    counts=Counter(basket).values();combos=[]
    pool=tuple(range(1,unique+1));n=len(pool)
    try:
        for c in range(1,max(counts)+1):
            for i in product(range(n),repeat=c):
                if sorted(i) == list(i):
                    combos.append(tuple(pool[j] for j in i))

    except ValueError:
        return 0
    combos=[combo for combo in combos if sum(combo)==num_books]
    # Counter((4, 4, 5)).most_common(1)[0][0] # 出现频率 最高的 键 也就是 4 了 
    # Counter((4, 4, 5)).most_common(1)[0][1] # 出现频率 最高的 值 也就是 2 了
    # min(Counter(counts).items(),key=lambda x:x[1])[1] # 获取 出现 的最少的 册子 的 计次。 
    # 比如  2， 2  代表 有 两种册子  只有 两本 
    # 要求是 要小于 它 
    # min(Counter(counts).items(),key=lambda x:x[1])[1] < Counter((4, 4, 5)).most_common(1)[0][1] 
    # min_copy_book=min(Counter(counts).items(),key=lambda x:x[1])[1]
    # return [sum([PRICES[j] for j in i]) for  i in combos]
    # 暂时 是想不出来了 。 以后再说吧 。
    min_copy_book=min(Counter(counts).items(),key=lambda x:x[1])[1]
    return int(min([sum([PRICES[j] for j in i]) for i in combos if min_copy_book<Counter(i).most_common(1)[0][1]]))
    
  
    
'''
这个 写法  可以 不用去判断   4 4 组合 大于 5 3 组合 。  但是 需要 处理  有的时候 书籍 本书 不够 最低价格的组合 。
#  现在 还没解决这个  bug  还是有问题 
basket = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]
total(basket)
[(1, 5, 5, 5), (2, 4, 5, 5), (3, 3, 5, 5), (3, 4, 4, 5), (4, 4, 4, 4)]
# 判断这些  组合  哪些 是可以使用的 同时 获取最小值
9800


basket=[1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]
它将假设您可以做3 x 5 +1，总计98.00美元
但是，没有3组，每组5个。书籍4和5仅出现两次。
正确答案是4 x 4 = $ 102.40。
一个真正的解决方案将使用counts变量中的所有信息，而不仅仅是max（counts）

'''
---

这个方案  全部测试通过

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
    
```







## Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to
indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include
a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of
`raise Exception`, you should write:

```python
raise Exception("Meaningful message indicating the source of the error")
```

## Running the tests

To run the tests, run `pytest book_store_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest book_store_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/book-store` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Inspired by the harry potter kata from Cyber-Dojo. [http://cyber-dojo.org](http://cyber-dojo.org)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
