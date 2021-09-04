# Tournament

记录小型足球比赛的结果。

根据一个包含哪个队与哪个队对抗以及结果如何的输入文件，创建一个带有如下表的文件：

```text
Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1
```

这些缩写是什么意思？

- MP: Matches Played  参加比赛
- W: Matches Won  比赛获胜
- D: Matches Drawn (Tied)  比赛对局（并列）
- L: Matches Lost  比赛失利
- P: Points  点 分数

一场胜利可为球队赢得3分。平局赢得1。亏损赢得0。

结果应**按点数降序排列**。如果出现**平局，则球队按字母顺序排列**。

###

Input

您的统计程序将收到如下输入：

```text
Allegoric Alaskans;Blithering Badgers;win
Devastating Donkeys;Courageous Californians;draw
Devastating Donkeys;Allegoric Alaskans;win
Courageous Californians;Blithering Badgers;loss
Blithering Badgers;Devastating Donkeys;loss
Allegoric Alaskans;Courageous Californians;win
```

比赛结果参考列出的第一支球队。所以这条线

```text
Allegoric Alaskans;Blithering Badgers;win
```

意味着 Allegoric Alaskans 击败了Blithering ger。

This line:

```text
Courageous Californians;Blithering Badgers;loss
```

意味着Blithering Badgers 击败了 Courageous Californians。

And this line:

```text
Devastating Donkeys;Courageous Californians;draw
```

意味着Devastating Donkeys 和 Courageous Californians 并列。


## 一些知识
### typing 模块
[typing模块文档](https://www.osgeo.cn/cpython/library/typing.html?highlight=union#typing.Union)

Python运行时不强制执行函数和变量类型注释。它们可以被第三方工具使用，如类型检查、ide、linter等。

这个模块就是为了  类型别名的

类型别名是通过将类型分配给别名来定义的。在这个例子中， Vector 和 List[float] 将被视为可互换的同义词：

```python
from typing import List
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```
类型别名对于简化复杂类型签名很有用。例如：：


```python
from typing import Dict, Tuple, Sequence

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...

＃静态类型检查器会将先前的类型签名视为
＃与此完全相同。
def broadcast_message(
        message: str,
        servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:

```
注意 None 由于类型提示是一种特殊情况，因此被替换为 type(None) .



```python
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)
```
**Union**

联合类型； Union[X, Y] 表示x或y。


**Counter**

A Counter 是一个 dict 用于计算hash对象的子类。它是一个集合，元素存储为字典键，其计数存储为字典值。计数可以是任何整数值，包括零计数或负计数。这个 Counter 在其他语言中，类类似于包或多集

另外Counter 对象 不存在的对象也可以 直接 以 字典方式访问   返回的 是  0 如果 键 不存在

**itemgetter**

operator.itemgetter(item)

operator.itemgetter(*items)

返回获取的可调用对象 item 使用操作数的 __getitem__() 方法。如果指定了多个项，则返回查找值的元组。例如：

后 f = itemgetter(2) 调用 f(r) 返回 r[2] .

后 g = itemgetter(2, 5, 3) 调用 g(r) 返回 (r[2], r[5], r[3]) .

等同于：

```python

def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g
```

可以是操作数接受的任何类型 __getitem__() 方法。字典接受任何hash值。列表、元组和字符串接受索引或切片：
```python
[in]:itemgetter('name')({'name': 'tu', 'age': 18})

[out]:'tu'

[in]:itemgetter(1)('ABCDEFG')

[out]:'B'

[out]:[in]:itemgetter(1,3,5)('ABCDEFG')

[out]:('B', 'D', 'F')

[out]:[in]:itemgetter(slice(2,None))('ABCDEFG')

'CDEFG'
```
使用示例 itemgetter() 要从元组记录中检索特定字段，请执行以下操作：

```python
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
getcount = itemgetter(1)
list(map(getcount, inventory))

out: [3, 2, 5, 1]

sorted(inventory, key=getcount)

out: [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

```


可以用作 字典的多索引排序  以及其他东西


## 针对此题 别人的好的解决方案

一些命令测试
```python
In [42]: from typing import Counter, DefaultDict, List, Sequence, Tuple, Union

In [44]: teams: DefaultDict[str, Counter[str]] = DefaultDict(Counter)
# 直接写  teams = DefaultDict(Counter)  也可以。 前面那个是注解 没有实际意义。 标注一下 类型
# 另外一种写法
# from collections import defaultdict,Counter
# aa['a']['b']+=1
# aa 输出以后 是以下 内容
# defaultdict(collections.Counter, {'a': Counter({'b': 1})})
In [45]: teams
Out[45]: defaultdict(typing.Counter, {})

In [46]: Cell
Out[46]: typing.Union[str, int]

In [47]: Row
Out[47]: typing.Tuple[str, typing.Union[str, int], typing.Union[str, int], typing.Union[str, int], typing.Union[str, int], typing.Union[str, int]]

In [48]: teams['a_team']['win']+=1

In [49]: teams
Out[49]: defaultdict(typing.Counter, {'a_team': Counter({'win': 1})})

In [52]: Cell = Union[str, int] # 字符串或者数字
    ...: Row = Tuple[str, Cell, Cell, Cell, Cell, Cell]

In [53]: table: List[Row] = []
        # 这里 也可以写成  table=[]  List[Row] 这是注解
        # 实际上 table 就是一个列表

In [54]: table
Out[54]: []

In [55]: table.insert(0, ("Team", "MP", "W", "D", "L", "P"))

In [56]: table
Out[56]: [('Team', 'MP', 'W', 'D', 'L', 'P')]

```
["Allegoric Alaskans;Blithering Badgers;win"] 是 Sequence[str]  其实也可以 写成 List[str]

仅仅是注解 所以没有什么实际意义 ， 提高可读性



```python
"""
Exercism solution for "tournament"
"""
from operator import itemgetter
from typing import Counter, DefaultDict, List, Sequence, Tuple, Union

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
OUTCOME_MAP = {"win": "loss", "loss": "win", "draw": "draw"}


Cell = Union[str, int] # 定义类型 cel 是  str 或者 int
Row = Tuple[str, Cell, Cell, Cell, Cell, Cell]

def tally(results: Sequence[str]) -> List[str]:
    """
    Tally a football tournament.
    """
    teams: DefaultDict[str, Counter[str]] = DefaultDict(Counter)
    for result in results:
        home, away, outcome = result.split(";")
        teams[home][outcome] += 1
        teams[away][OUTCOME_MAP[outcome]] += 1

    table: List[Row] = []
    for team, record in sorted(teams.items()):
        # sorted 默认是 升序
        wins, draws, losses = record["win"], record["draw"], record["loss"]
        matches, points = wins + draws + losses, 3 * wins + draws
        table.append((team, matches, wins, draws, losses, points))
    table.sort(key=itemgetter(-1), reverse=True)

    table.insert(0, ("Team", "MP", "W", "D", "L", "P"))
    return [ROW_FORMAT.format(*row) for row in table]
```
## 无注解 简化版
```python
from typing import Counter, DefaultDict

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
OUTCOME_MAP = {"win": "loss", "loss": "win", "draw": "draw"}

def tally(results):
    teams=DefaultDict(Counter)
    for result in results:
        home,away,outcome=result.split(";")
        teams[home][outcome]+=1
        teams[away][OUTCOME_MAP[outcome]]+=1
    table=[]
    for team,record in sorted(teams.items()):
        w,d,l=record['win'],record['draw'],record['loss']
        mp,p=w+d+l,w*3+d # 计算得分 和  参与场数
        table.append((team,mp,w,d,l,p)) # 添加到列表
    table.sort(key=lambda x:x[-1],reverse=True) # 排序
    table.insert(0, ("Team", "MP", "W", "D", "L", "P")) # 插入表头

    return [ROW_FORMAT.format(*row) for row in table] # 批量添加 添加 字符串格式


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

To run the tests, run `pytest tournament_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest tournament_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/tournament` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
