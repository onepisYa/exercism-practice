# Say

Given a number from 0 to 999,999,999,999, spell out that number in English.
999999999999 =10**12-1

九千九百九十九亿九千九百九十九万九千九百九十九

ones = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]


tens = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
    'ninety'
]



hundred = "hundred" (100)  ##!!! You can add 'trillion'(万亿), 'quadrillion'(千万亿), etc. to the threes list and it will work, but it will fail to raise an exception in that one test


threes = [
    'thousand', 'million'(百万) 'billion'(十亿)
]  #'trillion'万亿, 'quadrillion'千万亿, 'quintillion'(五亿), 'sextillion'(六亿), 'septillion'(9亿), 'octillion'(80亿), 'nonillion'(90亿)
million (百万)
billion (十亿)


## Step 1

Handle the basic case of 0 through 99.

If the input to the program is `22`, then the output should be
`'twenty-two'`.

Your program should complain loudly if given a number outside the
blessed range.

Some good test cases for this program are:

处理0到99的基本情况。
如果程序的输入为22，则输出应为 'twenty-two'
如果给定的数字超出了允许范围，则您的程序应大声抱怨。
此程序的一些不错的测试用例是：

- 0
- 14
- 50
- 98
- -1
- 100

### Extension

If you're on a Mac, shell out to Mac OS X's `say` program to talk out
loud. If you're on Linux or Windows, eSpeakNG may be available with the command `espeak`.

## Step 2

Implement breaking a number up into chunks of thousands.

So `1234567890` should yield a list like 1, 234, 567, and 890, while the
far simpler `1000` should yield just 1 and 0.

The program must also report any values that are out of range.

实现将数字分解为成千上万的块。
因此1234567890应该产生一个像1、234、567和890这样的列表，而更简单的1000应该只产生1和0。
该程序还必须报告任何超出范围的值。

## Step 3

Now handle inserting the appropriate scale word between those chunks.

So `1234567890` should yield `'1 billion 234 million 567 thousand 890'`

The program must also report any values that are out of range.  It's
fine to stop at "trillion".

现在，处理在这些块之间插入适当的比例词。
所以1234567890应该产生'10亿2.34亿567万890'
该程序还必须报告任何超出范围的值。停止在万亿就可以了。


## Step 4

将所有内容放在一起，只会得到简单的英语。
12345应该给一万二千三百四十五。
该程序还必须报告任何超出范围的值。

Put it all together to get nothing but plain English.

`12345` should give `twelve thousand three hundred forty-five`.

The program must also report any values that are out of range.

### Extensions

Use _and_ (correctly) when spelling out the number in English:

- 14 becomes "fourteen".
- 100 becomes "one hundred".
- 120 becomes "one hundred and twenty".
- 1002 becomes "one thousand and two".
- 1323 becomes "one thousand three hundred and twenty-three".

拼写英文数字时，请使用和（正确）：
14变成十四。
100变成一百。
120变成一百二十。
1002变成一千零二。
1323年变成十三百二十三。


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

To run the tests, run `pytest say_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest say_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/say` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

A variation on JavaRanch CattleDrive, exercise 4a [http://www.javaranch.com/say.jsp](http://www.javaranch.com/say.jsp)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
