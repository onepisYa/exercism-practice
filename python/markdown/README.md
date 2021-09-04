# Markdown

重构Markdown解析器。

markdown练习是一种重构练习。

有一些代码使用Markdown语法 [Markdown
syntax](https://guides.github.com/features/mastering-markdown/) 解析给定的字符串，并返回该字符串的关联HTML。

即使此代码编写混乱且难以遵循，但它仍然可以正常工作并且所有测试都通过了！

您面临的挑战是重新编写此代码，以使其更易于阅读和维护，同时仍要确保所有测试都能通过。

如果您在注释中记录了重构过程中所做的事情，这将很有帮助，以使审阅者可以看到它，但这并不是绝对必要的。最重要的是使代码更好！


需要重构的代码如下：

```python
import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res

```
## 正则回顾
- \1 可以 访问  查询字符串中 查询到的 内容
- flags=re.M 可以使 \n 之后的 也被匹配到 多行匹配
- (?!<[hlu])  ?!  取 不以 <[hlu] 结尾的内容 
    - "Windows(?!95|98|NT|2000)"能匹配"Windows3.1"中的"Windows"，但不能匹配"Windows2000"中的"Windows"
- [^\n] 中括号中 以 ^ 开头 则表示 不包含 \n 
- r 加  r 很重要。 原生字符  尽量都加上 
- re.S=re.DOTALL   
    - 使 '.' 特殊字符完全匹配任何字符，包括换行符；如果没有此标志， '.' 会匹配任何东西 除了 换行符对应于内联标志 (?s) .
    
```python
# 案例

# [in]：

# 匹配任意 不以 Asimov 开头的 字符  因为前面  放了  ^ 所以 原先是取 不以 Asimov 结尾 的 现在则  变成 不以  Asimov 开头 了 
re.match("^(?!Asimov)(.*?$)","Isaac aaa")

# [out]：

< _sre.SRE_Match object; span=(0, 9), match='Isaac aaa' >

# [in]:
re.match("^(?!Asimov)(.*?$)","AsimovIsaac aaa")
# [out]:
# 无输出  因为  匹配不到 Asimov 开头的 字符 
```

```PYTHON
#  \1 可以 访问  查询字符串中 查询到的 内容
import re

a="__This will be bold__"
s = re.sub(r'__(.*?)__', r'<strong>\1</strong>', a)
```

优化后的代码

```python

import re


def parse(markdown):
    s = markdown
    s = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', s)
    s = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', s)
    s = re.sub(r'^\* (.*?$)', r'<li>\1</li>', s, flags=re.M)
    s = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', s, flags=re.S)
    # 利用 format 传入 参数 ， 以及 乘法 复制  #  以及 h 几  
    for i in range(6, 0, -1):
        s = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), s, flags=re.M)
    
    s = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', s, flags=re.M)
    s = re.sub(r'\n', '', s)
    return s
    
 ```
 
根据 前人的想法。 自己 复盘写出来。  大部分还是和人家 一样  

```python

import re


def parse(markdown):
    s = markdown
    s=re.sub(r"__(.+?)__",r"<strong>\1</strong>",s) # --
    s=re.sub(r"_(.+?)_",r"<em>\1</em>",s) # - 
    s=re.sub(r"^\*\s*(.+?$)",r"<li>\1</li>",s,flags=re.M) # *
    s=re.sub(r"(<li>.*</li>)",r"<ul>\1</ul>",s,flags=re.S) # li 
    for i in range(6,0,-1):
        s=re.sub(r"^{}\s*(.*?$)".format("#"*i),r"<h{0}>\1</h{0}>".format(i),s,flags=re.M) # title h
    s=re.sub (r"^(?!<[hul])(.*?$)",r"<p>\1</p>",s,flags=re.M) # <hul p
    s=re.sub(r"\n","",s) # \n
    return s
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

To run the tests, run `pytest markdown_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest markdown_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/markdown` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
