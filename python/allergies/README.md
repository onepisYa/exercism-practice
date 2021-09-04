# Allergies

Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies.

给定一个人的过敏评分，确定他们是否对给定的物品过敏，以及他们完整的过敏清单。

An allergy test produces a single numeric score which contains the
information about all the allergies the person has (that they were
tested for).

过敏测试产生一个单一的数字评分，其中包含有关该人所有（已对其进行测试的）过敏的信息。

The list of items (and their value) that were tested are:

被测试的项目(及其价值)列表如下:

* eggs (1)
* peanuts (2)
* shellfish (4)
* strawberries (8)
* tomatoes (16)
* chocolate (32)
* pollen (64)
* cats (128)

So if Tom is allergic to peanuts and chocolate, he gets a score of 34.

Now, given just that score of 34, your program should be able to say:

所以，如果汤姆对花生和巧克力过敏，他会得到34分。

现在，给出34分，你的程序应该能够说:

- Whether Tom is allergic to any one of those allergens listed above.
- All the allergens Tom is allergic to.

- 汤姆是否对上面列出的任何一种过敏原过敏。
- 汤姆对所有的过敏原都过敏。


Note: a given score may include allergens **not** listed above (i.e.
allergens that score 256, 512, 1024, etc.).  Your program should
ignore those components of the score.  For example, if the allergy
score is 257, your program should only report the eggs (1) allergy.

注: 一个给定的分数可能包括未列出的过敏原(即分数为256、512、1024等的过敏原)。你的程序应该忽略这些分数的组成部分。例如，如果过敏评分是257，你的程序应该只报告鸡蛋(1)过敏。

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

To run the tests, run `pytest allergies_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest allergies_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/allergies` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Jumpstart Lab Warm-up [http://jumpstartlab.com](http://jumpstartlab.com)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
