# Pangram

判断一个句子是否是一个引号. A pangram (Greek: παν γράμμα, pan gramma,
"every letter")是一个使用字母的序列每个字母至少一次的句子

最著名的 English pangram is:

> The quick brown fox jumps over the lazy dog.

就是一个句子是否 包含 全部 26个字母

所使用的字母由ASCII字母a到z（含）组成，并且不区分大小写。输入将不包含非ASCII符号。

```python
# 别人的解决方案
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(string):
    return ALPHABET.issubset(string.lower())


# 我的 解决方案
from collections import Counter
import numpy as np
import string
def is_pangram(sentence):
    ct=Counter(sentence.lower()).keys()
    return bool(np.in1d(np.array(list(string.ascii_lowercase)),np.array(list(ct))).all())
# 这里 之所以 转换为 bool  其实不用的。
# 因为 测试的时候 用了  AssertIs  所以 需要转换一下。

```
## 相关知识
```python
issubset(other)
set <= other
测试集合中的每个元素是否都在 other .

set < other
测试集合是否为 other 也就是说， set <= other and set != other .
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

To run the tests, run `pytest pangram_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest pangram_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/pangram` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Wikipedia [https://en.wikipedia.org/wiki/Pangram](https://en.wikipedia.org/wiki/Pangram)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
