# Roman Numerals

Write a function to convert from normal numbers to Roman Numerals.

The Romans were a clever bunch. They conquered most of Europe and ruled
it for hundreds of years. They invented concrete and straight roads and
even bikinis. One thing they never discovered though was the number
zero. This made writing and dating extensive histories of their exploits
slightly more challenging, but the system of numbers they came up with
is still in use today. For example the BBC uses Roman numerals to date
their programmes.

The Romans wrote numbers using letters - I, V, X, L, C, D, M. (notice
these letters have lots of straight lines and are hence easy to hack
into stone tablets).
编写一个将普通数字转换为罗马数字的函数。

罗马人是一群聪明人。他们征服了欧洲大部分地区并统治了数百年。他们发明了混凝土和笔直的道路甚至比基尼。他们从未发现的一件事是数字零。这使得撰写和约会他们的漏洞利用的广泛历史更具挑战性，但是他们今天提出的数字系统仍在使用。例如，英国广播公司（BBC）使用罗马数字来标注他们的节目。

罗马人使用字母I，V，X，L，C，D，M写数字（请注意，这些字母有很多直线，因此很容易被凿成石碑）。

```text
 1  => I
10  => X
 7  => VII
```

There is no need to be able to convert numbers larger than about 3000.
(The Romans themselves didn't tend to go any higher)

Wikipedia says: Modern Roman numerals ... are written by expressing each
digit separately starting with the left most digit and skipping any
digit with a value of zero.

To see this in practice, consider the example of 1990.
不需要转换大于3000的数字。（罗马人本人并没有倾向于更高的数字）

维基百科说：现代罗马数字...是通过分别表示每个数字（从最左边的数字开始，然后跳过任何值为零的数字）来编写的。

要在实践中看到这一点，请考虑1990年的例子。

In Roman numerals 1990 is MCMXC:

1000=M
900=CM
90=XC

2008 is written as MMVIII:

2000=MM
8=VIII

See also: http://www.novaroma.org/via_romana/numbers.html


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

To run the tests, run `pytest roman_numerals_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest roman_numerals_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/roman-numerals` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

The Roman Numeral Kata [http://codingdojo.org/cgi-bin/index.pl?KataRomanNumerals](http://codingdojo.org/cgi-bin/index.pl?KataRomanNumerals)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
