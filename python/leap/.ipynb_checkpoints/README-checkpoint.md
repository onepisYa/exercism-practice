# Leap

给定一年，请报告是否是 润年。

The tricky thing here is that a leap year in the Gregorian calendar occurs:
棘手的是，公历发生了闰年：
```text
on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
```

例如，1997年不是闰年，而1996年是闰年。1900年不是闰年，而2000年是闰年。

四年一闰，百年不闰，四百年再闰.

```python

# import calendar
# def leap_year(year):
#     return calendar.isleap(year)


# A leap in four years, no leap in one hundred years, four hundred years leap again.
def leap_year(year):    
    return True if (year % 100!=year % 4 == 0 or year%4 ==year%400==0) else False

```

## Notes

Though our exercise adopts some very simple rules, there is more to
learn!

尽管我们的练习采用了一些非常简单的规则，但还有很多东西要学习！

有关整个leap年现象的令人愉快的四分钟说明， [this youtube video][video].

[video]: http://www.youtube.com/watch?v=xX96xng7sAE


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

To run the tests, run `pytest leap_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest leap_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/leap` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

JavaRanch Cattle Drive, exercise 3 [http://www.javaranch.com/leap.jsp](http://www.javaranch.com/leap.jsp)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
