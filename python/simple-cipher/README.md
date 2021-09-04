# Simple Cipher

Implement a simple shift cipher like Caesar and a more secure substitution cipher.

实现像Caesar (凯撒) 这样的简单移位密码和更安全的替换密码。

## Step 1

"If he had anything confidential to say, he wrote it in cipher, that is,
by so changing the order of the letters of the alphabet, that not a word
could be made out. If anyone wishes to decipher these, and get at their
meaning, he must substitute the fourth letter of the alphabet, namely D,
for A, and so with the others."
—Suetonius, Life of Julius Caesar

如果他有什么要说的机密内容，他会用密码来写，也就是说，通过改变字母的顺序，就无法辨认出一个单词。如果有人希望对它们进行解密并理解他们的意思，意思是，他必须用字母A替换字母的第四个字母D，然后用其他字母替换。 -苏顿纽斯，尤利乌斯凯撒生平


Ciphers are very straight-forward algorithms that allow us to render
text less readable while still allowing easy deciphering. They are
vulnerable to many forms of cryptanalysis, but we are lucky that
generally our little sisters are not cryptanalysts.

密码是非常简单的算法，它使我们可以使文本的可读性降低，同时仍然易于解密。他们很容易受到多种形式的密码分析的影响，但是我们很幸运，我们的小姐妹通常不是密码分析员。


The Caesar Cipher was used for some messages from Julius Caesar that
were sent afield. Now Caesar knew that the cipher wasn't very good, but
he had one ally in that respect: almost nobody could read well. So even
being a couple letters off was sufficient so that people couldn't
recognize the few words that they did know.

凯撒密码用于从朱利叶斯·凯撒（Julius Caesar）发送到现场的一些消息。现在凯撒知道密码不是很好，但是在这方面他有一个盟友：几乎没有人会读得很好。因此，即使只写几封信也足够使人们无法认出他们确实知道的几个单词。


Your task is to create a simple shift cipher like the Caesar Cipher.
This image is a great example of the Caesar Cipher:

您的任务是创建像Caesar Cipher这样的简单移位密码。此图像是凯撒密码的一个很好的例子：

![Caesar Cipher][1]

For example:

Giving "iamapandabear" as input to the encode function returns the cipher "ldpdsdqgdehdu". Obscure enough to keep our message secret in transit.

When "ldpdsdqgdehdu" is put into the decode function it would return
the original "iamapandabear" letting your friend read your original
message.

将“ iamapandabear”作为编码函数的输入将返回密码“ ldpdsdqgdehdu”。晦涩难懂，以使我们的消息在传输过程中保持机密。

将“ ldpdsdqgdehdu”放入解码函数后，它将返回原始的“ iamapandabear”，让您的朋友阅读您的原始消息。

## Step 2

Shift ciphers are no fun though when your kid sister figures it out. Try
amending the code to allow us to specify a key and use that for the
shift distance. This is called a substitution cipher.

当您的孩子姐姐弄清楚移位密码时，它并不有趣。尝试修改代码，以允许我们指定一个键并将其用于移位距离。这称为替换密码。

Here's an example:

Given the key "aaaaaaaaaaaaaaaaaa", encoding the string "iamapandabear"
would return the original "iamapandabear".

给定键“ aaaaaaaaaaaaaaaaaaaaaa”，编码字符串“ iamapandabear”将返回原始的“ iamapandabear”。

Given the key "ddddddddddddddddd", encoding our string "iamapandabear"
would return the obscured "ldpdsdqgdehdu"

给定键“ ddddddddddddddddddd”，编码我们的字符串“ iamapandabear”将返回模糊的“ ldpdsdqgdehdu”


In the example above, we've set a = 0 for the key value. So when the
plaintext is added to the key, we end up with the same message coming
out. So "aaaa" is not an ideal key. But if we set the key to "dddd", we
would get the same thing as the Caesar Cipher.

在上面的示例中，我们为键值设置了a = 0。因此，当将纯文本添加到密钥时，我们最终会收到相同的消息。因此，“ aaaa”不是理想的键。但是，如果将密钥设置为“ dddd”，我们将得到与凯撒密码相同的东西。

## Step 3

The weakest link in any cipher is the human being. Let's make your
substitution cipher a little more fault tolerant by providing a source
of randomness and ensuring that the key contains only lowercase letters.

If someone doesn't submit a key at all, generate a truly random key of
at least 100 alphanumeric characters in length.

任何密码中最薄弱的环节是人。通过提供随机源并确保密钥仅包含小写字母，让我们的替换密码更具容错能力。
如果有人根本不提交密钥，请生成一个长度至少为100个字母数字字符的真正随机密钥。

key 是 偏移加密秘钥  plaintext 是 明文  a 偏移为0 ，b 偏移为 1

假设  key =abc  那么偏移为 012
但是明文比 key 更长   "iamapandabear"  那么 依次 012012012012 这样依次 对应到 明文上 进行偏移。

1. 首先 将key 对应的 偏移 计算出来
2. 计算字母对应的偏移 26 的 余数

```
letters=string.ascii_letters
;'b' 代表的是 明文      'c' 代表的 是 key 的 索引
; 当 两个索引 的 和 对 26 取余  x%26  当 x 小于26 的时候等于本身，等于26的 时候等于 0   也就是 第一个字母。  这样正好是我们的需求。
; -1%26  包括负数 也是 一样的  任何 数除以 26 余数 都是 0 到 25 之间的数。

当然我的代码里面 其实也可以不使用 cycle  而 使用"str"*数字 然后 切片 , 整除 加 1 乘以 "str" 

letters[(letters.index("b")+letters.index("c"))%26]

```

## Extensions

Shift ciphers work by making the text slightly odd, but are vulnerable
to frequency analysis. Substitution ciphers help that, but are still
very vulnerable when the key is short or if spaces are preserved. Later
on you'll see one solution to this problem in the exercise
"crypto-square".

If you want to go farther in this field, the questions begin to be about
how we can exchange keys in a secure way. Take a look at [Diffie-Hellman
on Wikipedia][dh] for one of the first implementations of this scheme.

[1]: https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Caesar_cipher_left_shift_of_3.svg/320px-Caesar_cipher_left_shift_of_3.svg.png
[dh]: http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

## Should I use random or secrets?

Python, as of version 3.6, includes two different random modules.

The module called `random` is pseudo-random, meaning it does not generate
true randomness, but follows an algorithm that simulates randomness.
Since random numbers are generated through a known algorithm, they are not truly random.

The `random` module is not correctly suited for cryptography and should not be used,
precisely because it is pseudo-random.

For this reason, in version 3.6, Python introduced the `secrets` module, which generates
cryptographically strong random numbers that provide the greater security required for cryptography.

Since this is only an exercise, `random` is fine to use, but note that **it would be
very insecure if actually used for cryptography.**


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

To run the tests, run `pytest simple_cipher_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest simple_cipher_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/simple-cipher` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Substitution Cipher at Wikipedia [http://en.wikipedia.org/wiki/Substitution_cipher](http://en.wikipedia.org/wiki/Substitution_cipher)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
