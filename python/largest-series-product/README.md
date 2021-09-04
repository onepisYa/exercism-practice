# Largest Series Product

Given a string of digits, calculate the largest product for a contiguous
substring of digits of length n.

给定一串数字，请为长度为n的连续数字子串计算最大乘积。

For example, for the input `'1027839564'`, the largest product for a
series of 3 digits is 270 (9 * 5 * 6), and the largest product for a
series of 5 digits is 7560 (7 * 8 * 3 * 9 * 5).

3位数字序列的最大乘积是270（9 * 5 * 6）,5 位数字最大乘积 is 7560 (7 * 8 * 3 * 9 * 5)


Note that these series are only required to occupy * adjacent posi tions * 
in the input; the digits need not be * numerically  consecutive * .

请注意，只需要这些序列占据输入中的相邻位置即可；这些数字不必在数字上连续。

For the input `'73167176531330624919225119674426574742355349194934'`,
the largest product for a series of 6 digits is 23520.

连续的6位数字的最大乘积是23520。

Implementation note:
In case of invalid inputs to the 'largest_product' function
your program should raise a ValueError with a meaningful error message.
Feel free to reuse your code from the 'series' exercise!

实施说明：如果对 largest_product函数的输入无效，则程序应引发ValueError并显示有意义的错误消息。随时从系列练习中重用您的代码！


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

To run the tests, run `pytest largest_series_product_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest largest_series_product_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/largest-series-product` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

A variation on Problem 8 at Project Euler [http://projecteuler.net/problem=8](http://projecteuler.net/problem=8)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
