# Clock

实现一个时钟来处理没有日期的时间。

您应该能够添加和减去分钟。

代表相同时间的两个时钟应该彼此相等。

## 归纳

先算分 后算 时  因为 还有进位 ， 避免重复 运算 

分 大于等于 60    divmod 商 加到 时 上，  模 是 分  如果 商 大于 24 继续上一步操作（分钟是负数也是正确的 ）

时 大于等于 24 求 模  不管时 是正数 还是 负数  模 是正确的  时  

```PYTHON

        # 这种方案的话 会比较麻烦 。 
        # 减掉之后还要 判断  大小 继续之前的处理
        # 个人感觉 乘起来之后 。 算总数 比较好
        
class Clock:
    def __init__(self, hour, minute):
        new_hour=hour
        new_minute=minute
        if new_minute >= 60 or new_minute <0:
            self.s1,new_minute = divmod(minute,60)
            new_hour=self.s1+new_hour
        if new_hour >= 24 or new_hour<0:
            new_hour=new_hour%24
        self.s=new_hour
        self.m=new_minute

    def __repr__(self):
        return "{:0>2d}:{:0>2d}".format(self.s,self.m)

    def __eq__(self, other):
        return repr(self)==repr(other)

    def __add__(self, minutes):
        total=self.m+self.s*60
        total+=minutes
        self.s,self.m=divmod(total,60) # 这样写 可能会超出 24的范围。 
        # 所以还是推荐  返回对象  或者  乘以总的分钟数比较好
        return self
'''

    def __sub__(self, minutes):
        total=self.m+self.s*60
        total-=minutes
        self.s,self.m=divmod(total,60)
        return self
'''    
    def __sub__(self, minutes):
        # 另外一种思路 就是  返回新的 实例对象  
        update_m=self.m-minutes
        return Clock(self.s,update_m)

        
        
```

还有一种思路 就是 将   小时全部乘 起来 。  然后加上分 去计算。  

### 代码如下

```PYTHON
class Clock:
    def __init__(self, hour, minute):
        self.total_m=(hour*60+minute)%1440 # 1 day = 24 * 60

    def __repr__(self):
        return "{:0>2d}:{:0>2d}".format(*divmod(self.total_m,60))

    def __eq__(self, other):
        return repr(self)==repr(other)

    def __add__(self, minutes):
        self.total_m+=minutes
        return self

    def __sub__(self, minutes):
        self.total_m-=minutes
        return self

     # 此方法  更加简洁    但是针对负数 有一定局限性 
     # 比如  str(Clock(0, 0) - 160), "21:20"
    # 预期的 "21:20"  实际的  -3:20
    修改优化之后的代码 
class Clock:
    def __init__(self, hour, minute):
        self.total_m=(hour*60+minute)%1440 # 1 day = 24 * 60

    def __repr__(self):
        return "{:0>2d}:{:0>2d}".format(*divmod(self.total_m,60))

    def __eq__(self, other):
        return repr(self)==repr(other)

    def __add__(self, minutes):
        self.total_m+=minutes
        return Clock(*divmod(self.total_m,60))

    def __sub__(self, minutes):
        self.total_m-=minutes
        return Clock(*divmod(self.total_m,60))
    # 其实*divmod(self.total_m,60)
    # 用了3 次 完全可以 写为一个函数
    # 直接调用 
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

To run the tests, run `pytest clock_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest clock_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/clock` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Pairing session with Erin Drummond [https://twitter.com/ebdrummond](https://twitter.com/ebdrummond)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
