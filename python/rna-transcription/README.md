# RNA Transcription

给定一条DNA链，返回其RNA补体（每次RNA转录）。

DNA 和 RNA 链都是核苷酸序列。

在 DNA 中发现的四种核苷酸是 
- adenine (**A**)
- cytosine (**C**),
- guanine (**G**) 
- thymine (**T**).

在 RNA 中发现的四个核苷酸是 
- adenine (**A**)
- cytosine (**C**)
- guanine (**G**)
- uracil (**U**)

给定一条DNA链，其转录的RNA链是通过将每个核苷酸替换为其互补序列而形成的：

* `G` -> `C`
* `C` -> `G`
* `T` -> `A`
* `A` -> `U`

## 代码
```python
# 方法 1 
TRANS=dict(G="C",C="G",T="A",A="U")
def to_rna(dna_strand):
    return "".join(TRANS.get(i) for i in dna_strand)

# 方法 2
trans = str.maketrans("GCTA", "CGAU")

class DNA():

    def __init__(self, dna_string):
        self.dna_string = dna_string

    def to_rna(self):
        return self.dna_string.translate(trans)
    
# 1
TRANS=dict(G="C",C="G",T="A",A="U")
def to_rna(dna_strand):
    return "".join(TRANS.get(i) for i in dna_strand)

# 2 
trans = str.maketrans("GCTA", "CGAU")
def to_rna(dna_strand):
    return dna_string.translate(trans)
```
## 关于 translate 和 maketrans  字符串映射

```python


In [48]: trans=str.maketrans("A","B")

In [49]: trans
Out[49]: {65: 66}

In [50]: "A".translate(trans)
Out[50]: 'B'

In [51]: trans=str.maketrans("AC","BD")

In [52]: "A".translate(trans)
Out[52]: 'B'

In [53]: "AC".translate(trans)
Out[53]: 'BD'
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

To run the tests, run `pytest rna_transcription_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest rna_transcription_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/rna-transcription` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Hyperphysics [http://hyperphysics.phy-astr.gsu.edu/hbase/Organic/transcription.html](http://hyperphysics.phy-astr.gsu.edu/hbase/Organic/transcription.html)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
