# ETL


We are going to do the `Transform` step of an Extract-Transform-Load.

我们将执行Extract-Transform-Load的Transform步骤。

### ETL

Extract-Transform-Load (ETL) is a fancy way of saying, "We have some crufty, legacy data over in this system, and now we need it in this shiny new system over here, so
we're going to migrate this."

(Typically, this is followed by, "We're only going to need to run this
once." That's then typically followed by much forehead slapping and
moaning about how stupid we could possibly be.)

Extract-Transform-Load（ETL）是一种奇特的说法，“我们在该系统中保留了一些原始的旧数据，现在我们需要在这里的闪亮新系统中使用它，因此我们将对其进行迁移。”
`
（通常，这之后是“我们只需要运行一次。”然后通常是在额头上打耳光，抱怨着我们可能有多愚蠢。）


### The goal

We're going to extract some scrabble scores from a legacy system.

我们将从旧版系统中提取一些拼字游戏分数。

The old system stored a list of letters per score:

旧系统按分数存储字母列表：

- 1 point: "A", "E", "I", "O", "U", "L", "N", "R", "S", "T",
- 2 points: "D", "G",
- 3 points: "B", "C", "M", "P",
- 4 points: "F", "H", "V", "W", "Y",
- 5 points: "K",
- 8 points: "J", "X",
- 10 points: "Q", "Z",

The shiny new scrabble system instead stores the score per letter, which
makes it much faster and easier to calculate the score for a word. It
also stores the letters in lower-case regardless of the case of the
input letters:

而是使用崭新的拼字系统来存储每个字母的分数，这使得计算一个单词的分数变得更快，更容易。不管输入字母的大小写，它也以小写形式存储字母：

- "a" is worth 1 point.
- "b" is worth 3 points.
- "c" is worth 3 points.
- "d" is worth 2 points.
- Etc.

Your mission, should you choose to accept it, is to transform the legacy data
format to the shiny new format.

您的任务（如果您选择接受）是将旧数据格式转换为崭新的格式。

### Notes

A final note about scoring, Scrabble is played around the world in a
variety of languages, each with its own unique scoring table. For
example, an "E" is scored at 2 in the Māori-language version of the
game while being scored at 4 in the Hawaiian-language version.

关于得分的最后说明，Scrabble在世界各地以多种语言播放，每种语言都有自己独特的得分表。例如，“ E”在游戏的毛利语版本中得分为2，而在夏威夷语版本中得分为4。

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

To run the tests, run `pytest etl_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest etl_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/etl` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

The Jumpstart Lab team [http://jumpstartlab.com](http://jumpstartlab.com)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
