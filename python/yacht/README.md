# Yacht

# 在游艇上执一次骰子 (游艇) *Yacht*


The dice game [Yacht](https://en.wikipedia.org/wiki/Yacht_(dice_game)) is from
the same family as Poker Dice, Generala and particularly Yahtzee, of which it
is a precursor. 在游戏中，5个骰子被掷出，结果可以输入十二个类别中的任何一个

掷骰子的得分取决于所选的类别。

## Scores in Yacht (分数表）

| Category | Score | Description | Example |
| -------- | ----- | ----------- | ------- |
| Ones | 1 × number of ones | Any combination	| 1 1 1 4 5 scores 3 |
| Twos | 2 × number of twos | Any combination | 2 2 3 4 5 scores 4 |
| Threes | 3 × number of threes | Any combination | 3 3 3 3 3 scores 15 |
| Fours | 4 × number of fours | Any combination | 1 2 3 3 5 scores 0 |
| Fives | 5 × number of fives| Any combination | 5 1 5 2 5 scores 15 |
| Sixes | 6 × number of sixes | Any combination | 2 3 4 5 6 scores 6 |
| Full House | Total of the dice | 一个数字的三个和另一个数字的两个| 3 3 3 5 5 scores 19 |
| Four of a Kind | Total of the four dice | 至少有四个骰子显示相同的面孔 | 4 4 4 4 6 scores 16 |
| Little Straight （小顺子30分）|  30 points | 1-2-3-4-5 | 1 2 3 4 5 scores 30 |
| Big Straight （大顺子）| 30 points | 2-3-4-5-6 | 2 3 4 5 6 scores 30 |
| Choice （分数为求和骰子的值）| Sum of the dice | Any combination | 2 3 3 4 6 scores 18 |
| Yacht | 50 points | 5个一样的骰子 | 4 4 4 4 4 scores 50 |

如果骰子不满足一个类别的要求，则得分为零

另外 比如 类别 Fours  如果 骰子 是 12335 那么分数 是 0  因为 只有 0 个 4  如果   是  44444 那么 分数 为 20 


## Task
给定 5 个骰子的值 和 类别 , 你的解决方案 应该返回 这一类骰子 的分数

如果骰子不满足类别的要求，解决方案应该返回0。 If the dice do not s

您可以假设总是显示五个值

每个值都在1到6之间。(包含 1 和 6）

你不应该假设骰子是按顺序排列的。

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

To run the tests, run `pytest yacht_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest yacht_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/yacht` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

James Kilfiger, using wikipedia [https://en.wikipedia.org/wiki/Yacht_(dice_game)](https://en.wikipedia.org/wiki/Yacht_(dice_game))

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
