# Luhn

Given a number determine whether or not it is valid per the Luhn formula.

The [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) is
a simple checksum formula used to validate a variety of identification
numbers, such as credit card numbers and Canadian Social Insurance
Numbers.

The task is to check if a given string is valid.

Validating a Number
------

长度为1或更短的字符串无效。输入中允许有空格，但在检查之前应将其删除。禁止使用其他所有非数字字符。

## Example 1: valid credit card number（有效信用卡）

```text
4539 1488 0343 6467
```

Luhn算法的第一步是从右边开始每隔两位数加倍。我们将加倍

```text
4_3_ 1_8_ 0_4_ 6_6_
```

如果将数字加倍会导致数字大于9，则将乘积减去9。我们加倍的结果：

```text
8569 2478 0383 3437
```

然后将所有数字相加：

```text
8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
```

如果总和可被10整除，则该数字有效。这个号码是有效的！

## Example 2: invalid credit card number（无效的信用卡号）

```text
8273 1232 7352 0569
```

从右边开始，将第二个数字加倍

```text
7253 2262 5312 0539
```

求和

```text
7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57
```

57不能被10整除，因此该数字无效。

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

To run the tests, run `pytest luhn_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest luhn_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/luhn` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

The Luhn Algorithm on Wikipedia [http://en.wikipedia.org/wiki/Luhn_algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
