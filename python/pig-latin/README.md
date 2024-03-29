# Pig Latin

Implement a program that translates from English to Pig Latin.

实施将英语翻译成Pig Latin的程序

Pig Latin is a made-up children's language that's intended to be
confusing. It obeys a few simple rules (below), but when it's spoken
quickly it's really difficult for non-children (and non-native speakers)
to understand.

拉丁猪（Pig Latin）是一种虚构的儿童语言，旨在引起混淆。它遵循一些简单的规则（如下），但是当它说的很快时，非孩子（和非母语人士）真的很难理解。

- **Rule 1**: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").

如果单词以元音开头，则在单词末尾添加“ ay”声音。请注意，单词开头的“ xr”和“ yt”会发出元音（例如“ xray”->“ xrayay”，“ yttria”->“ yttriaay”）。



- **Rule 2**: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, a.k.a. a consonant cluster (e.g. "chair" -> "airchay").


如果单词以辅音开头，请将其移至单词末尾，然后在单词末尾添加“ ay”声音。辅音可以由多个辅音（也称为辅音簇）组成（例如“椅子”->“ airchay”）。


- **Rule 3**: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").


如果单词以辅音开头，后跟“ qu”，请将其移到单词末尾，然后在单词末尾添加“ ay”声音（例如“ square”->“ aresquay” ）。



- **Rule 4**: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
如果一个单词在辅音簇之后包含“ y”或作为两个字母单词中的第二个字母，则会发出元音（例如，“节奏”->“ ythmrhay”，“我的”->“ ymay”） 



There are a few more rules for edge cases, and there are regional
variants too.

See <http://en.wikipedia.org/wiki/Pig_latin> for more details.


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

To run the tests, run `pytest pig_latin_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest pig_latin_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/pig-latin` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

The Pig Latin exercise at Test First Teaching by Ultrasaurus [https://github.com/ultrasaurus/test-first-teaching/blob/master/learn_ruby/pig_latin/](https://github.com/ultrasaurus/test-first-teaching/blob/master/learn_ruby/pig_latin/)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
