# Series

Given a string of digits, output all the contiguous substrings of length `n` in
that string in the order that they appear.

给定一串数字，请n按出现的顺序输出该字符串中所有长度相邻的子字符串。

For example, the string "49142" has the following 3-digit series:

例如，字符串 49142具有以下3位数字系列：

- "491"
- "914"
- "142"

And the following 4-digit series:

以及以下4位数字系列：

- "4914"
- "9142"

And if you ask for a 6-digit series from a 5-digit string, you deserve
whatever you get.

如果您要从5位数字的字符串中获取6位数字的序列，那么您应得到的一切都应得到。

请注意，只需要这些序列占据 输入中的相邻位置即可；这些数字不必在数字上连续。

意思就是 输入 一个字符串  和 长度 。 

然后 根据 限定的长度 返回对应长度的字符串 组合

提示 不要理解 为 只要 含有对应的数字 就行。  是要求 不改变原有的顺序。 比如 "918493904243"  并不是  包含这里面的数字  然后 组合 对应长度 。

而是 比如 位移  9184 1849 4 bit 这样 位移过去  要求在对应长度上  不改变位置。  当然 也不管重复值啦。


Note that these series are only required to occupy *adjacent positions*
in the input; the digits need not be *numerically consecutive*.


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

To run the tests, run `pytest series_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest series_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/series` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

A subset of the Problem 8 at Project Euler [http://projecteuler.net/problem=8](http://projecteuler.net/problem=8)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
