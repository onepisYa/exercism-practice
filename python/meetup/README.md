# Meetup

计算聚会的日期。

典型的见面会在一周的同一天举行。 在这个练习中，您将获得一个聚会日期的描述，并返回实际的聚会日期。

一般说明的例子包括:

- The first Monday of January 2017
- The third Tuesday of January 2017
- The wednesteenth of January 2017
- The last Thursday of January 2017

您需要解析的描述符是：

first, second, third, fourth, fifth, last, monteenth, tuesteenth, wednesteenth,
thursteenth, friteenth, saturteenth, sunteenth

请注意 "monteenth", "tuesteenth", 等等都是虚构的词。

有一次聚会，其成员意识到在一个月中有7天是以`-teenth` 结束的。因此

一个是保证每天的一周(Monday, Tuesday, ...) 每个月都会有一个日期以'-teenth' 命名

给出一个聚会日期的例子，每个包含月、日、年和描述符，计算实际聚会的日期。

For example, if given
"The first Monday of January 2017", the correct meetup date is 2017/1/2.


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

To run the tests, run `pytest meetup_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest meetup_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/meetup` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Jeremy Hinegardner mentioned a Boulder meetup that happens on the Wednesteenth of every month [https://twitter.com/copiousfreetime](https://twitter.com/copiousfreetime)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
