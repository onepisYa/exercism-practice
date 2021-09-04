# ISBN Verifier

The [ISBN-10 verification process](https://en.wikipedia.org/wiki/International_Standard_Book_Number) 用于验证书籍识别号，这些号码通常包含破折号，外观如下: `3-598-21508-8`

## ISBN

ISBN-10格式是9个数字(0到9)加上一个检查字符(只有一个数字或一个 x)。在这种情况下，检查字符是一个 x，这表示值’10’。这些符号可以有连字符也可以没有连字符，可以通过以下公式检查其有效性:

```
(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
```

如果结果是0，那么它是一个有效的 ISBN-10，否则它是无效的。

## Example

 让我们把 `3-598-21508-8`插入到公式中，得到:
```
(3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
```

由于结果是0，这证明了我们的 ISBN 是有效的。

## Task

给定一个字符串，程序应该检查所提供的字符串是否是有效的 ISBN-10。要实现这一点，需要在计算 ISBN 的校验位之前对字符串进行预处理/解析。

该程序应该能够验证 ISBN-10和不分离破折号。


## Caveats
在某些语言中，将字符串转换为数字是很棘手的。现在，由于 ISBN-10的校验数字可能是“ x”(表示“10”) ，这就更加棘手了。例如，`3-598-21507-X` 是有效的 ISBN-10。

## Bonus tasks

* Generate a valid ISBN-13 from the input ISBN-10 (and maybe verify it again with a derived verifier).

* Generate valid ISBN, maybe even from a given starting ISBN.

## 奖励任务

* 从输入 ISBN-10生成一个有效的 ISBN-13(并可能使用派生验证器再次验证它)。

* 生成有效的 ISBN，甚至可以从给定的开始 ISBN 生成。

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

To run the tests, run `pytest isbn_verifier_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest isbn_verifier_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/isbn-verifier` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Converting a string into a number and some basic processing utilizing a relatable real world example. [https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-10_check_digit_calculation](https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-10_check_digit_calculation)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
