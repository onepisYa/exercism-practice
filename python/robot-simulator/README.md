# Robot Simulator

Write a robot simulator.

A robot factory's test facility needs a program to verify robot movements.

The robots have three possible movements:

机器人工厂的测试设施需要一个程序来验证机器人的运动。
机器人有三种可能的动作：

- turn right
- turn left
- advance

Robots are placed on a hypothetical infinite grid, facing a particular
direction (north, east, south, or west) at a set of {x,y} coordinates,
e.g., {3,8}, with coordinates increasing to the north and east.

机器人被放置在假设的无限网格上，在一组{x，y}坐标（例如{3,8}）上面向特定方向（north，east，south or west），坐标向 north 和向 east 递增。


The robot then receives a number of instructions, at which point the
testing facility verifies the robot's new position, and in which
direction it is pointing.

然后，机器人会收到许多指令，测试设备将在该点验证机器人的新位置，并指出机器人所指向的方向。

- The letter-string "RAALAL" means:
  - Turn right
  - Advance twice(前进两次)
  - Turn left
  - Advance once(前进一次)
  - Turn left yet again(再左转)
- Say a robot starts at {7, 3} facing north. Then running this stream
  of instructions should leave it at {9, 4} facing west.

假设机器人从{7，3}开始朝 north 。然后，运行此指令流 应将其留在{9，4}面向 west 。


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

To run the tests, run `pytest robot_simulator_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest robot_simulator_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/robot-simulator` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Inspired by an interview question at a famous company.

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
