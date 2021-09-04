# Bob

鲍勃是一个懒散的青少年，在交谈中，他的反应非常有限。

如果你问他一个问题，比如: How are you?  ，鲍勃会回答 Sure 。

如果你对他 "YELL AT HIM" ，他会回答  Whoa, chill out! 

如果你向他提问，他会回答 Calm down,i konw what i'm doing!

如果你跟他说话的时候什么也没说，他就会说 Fine.Be that way! 

对于其他任何事情，他都会回答 Whatever.

鲍勃的对话伙伴在书面交流方面是个纯粹主义者，并且总是遵循英语句子标点符号的正常规则。


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

To run the tests, run `pytest bob_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest bob_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/bob` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Inspired by the 'Deaf Grandma' exercise in Chris Pine's Learn to Program tutorial. [http://pine.fm/LearnToProgram/?Chapter=06](http://pine.fm/LearnToProgram/?Chapter=06)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
