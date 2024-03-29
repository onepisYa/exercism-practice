# Rotational Cipher

Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.
凯撒密码 


The Caesar cipher is a simple shift cipher that relies on
transposing all the letters in the alphabet using an integer key
between `0` and `26`. Using a key of `0` or `26` will always yield
the same output due to modular arithmetic. The letter is shifted
for as many values as the value of the key.

Caesar 密码是一个简单的移位密码，它依赖于使用一个介于0和26之间的整数键将字母表中的所有字母进行移位。使用一个0或26的键总是会产生相同的输出，由于同余关系。字母的位移与键值的位移一样多。


The general notation for rotational ciphers is `ROT + <key>`.
The most commonly used rotational cipher is `ROT13`.

旋转密码的一般表示法是 ROT + < key > 。最常用的旋转密码是 ROT13。


A `ROT13` on the Latin alphabet would be as follows:

关于拉丁字母的 ROT13如下:

```text
明文Plain:  abcdefghijklmnopqrstuvwxyz
密文Cipher: nopqrstuvwxyzabcdefghijklm
```

It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.

它比 Atbash 密码更强大，因为它有27个可能的密钥和25个可用的密钥。

Ciphertext is written out in the same formatting as the input including spaces and punctuation.


加密文本以与输入相同的格式写出，包括空格和标点符号


## Examples

- ROT5  `omg` gives `trl`
- ROT0  `c` gives `c`
- ROT26 `Cool` gives `Cool`
- ROT13 `The quick brown fox jumps over the lazy dog.` gives `Gur dhvpx oebja sbk whzcf bire gur ynml qbt.`
- ROT13 `Gur dhvpx oebja sbk whzcf bire gur ynml qbt.` gives `The quick brown fox jumps over the lazy dog.`


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

To run the tests, run `pytest rotational_cipher_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest rotational_cipher_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/rotational-cipher` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Wikipedia [https://en.wikipedia.org/wiki/Caesar_cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
