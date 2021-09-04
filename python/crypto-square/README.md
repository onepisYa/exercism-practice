# Crypto Square

Implement the classic method for composing secret messages called a square code.

Given an English text, output the encoded version of that text.

First, the input is normalized: the spaces and punctuation are removed
from the English text and the message is downcased.

Then, the normalized characters are broken into rows.  These rows can be
regarded as forming a rectangle when printed with intervening newlines.
实现经典的方法来构成秘密信息，称为方码。
给定英文文本，输出该文本的编码版本。
首先，将输入标准化：从英文文本中删除空格和标点符号，并将消息缩小写。
然后，将规范化的字符分成几行。当用中间的换行符打印时，这些行可以视为形成矩形。

For example, the sentence

```text
"If man was meant to stay on the ground, god would have given us roots."
```

is normalized to:

```text
"ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
```

The plaintext should be organized in to a rectangle.  The size of the
rectangle (`r x c`) should be decided by the length of the message,
such that `c >= r` and `c - r <= 1`, where `c` is the number of columns
and `r` is the number of rows.

明文应组织成一个矩形。矩形的大小（r x c）应该由消息的长度决定，这样c> = r且c-r <= 1，其中c是列数，r是行数。


Our normalized text is 54 characters long, dictating a rectangle with
`c = 8` and `r = 7`:

我们的规范化文本长54个字符，指定了c = 8和r = 7的矩形：

```text
"ifmanwas"
"meanttos"
"tayonthe"
"groundgo"
"dwouldha"
"vegivenu"
"sroots  "
```

The coded message is obtained by reading down the columns going left to
right.

The message above is coded as:

通过读取从左到右的列可以获取编码后的消息。
上面的消息编码为：

```text
"imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"
```

Output the encoded text in chunks that fill perfect rectangles `(r X c)`,
with `c` chunks of `r` length, separated by spaces. For phrases that are
`n` characters short of the perfect rectangle, pad each of the last `n`
chunks with a single trailing space.

以填充完全矩形（r X c）的块的形式输出编码后的文本，其中c个长度为r的块以空格分隔。对于距离完美矩形短n个字符的短语，请在最后n个块中的每个块后面加上一个空格。

如何决定 r 和 c 的值？  用平方根 然后 向上取整 sqrt() 得到 c

然后长度 除以 这个数  得到 r  这样就满足了 下列 不等式。

c  is  columns

r is rows

 c >= r and c - r <= 1   

 切割 的时候 应该 使用 步长  c 较大的那个数。  因为第一小段结束后  下一小段开始的 是 第 c 个字符

```text
"imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
```

Notice that were we to stack these, we could visually decode the
ciphertext back in to the original message:

注意，如果我们将它们堆叠起来，我们可以在视觉上将密文解码回原始消息：

```text
"imtgdvs"
"fearwer"
"mayoogo"
"anouuio"
"ntnnlvt"
"wttddes"
"aohghn "
"sseoau "
```


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

To run the tests, run `pytest crypto_square_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest crypto_square_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/crypto-square` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

J Dalbey's Programming Practice problems [http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html](http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
