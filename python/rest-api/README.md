[toc]


# Rest Api


实现用于跟踪 IOUs 的 RESTful API。(Implement a RESTful API for tracking IOUs.)


四个室友有经常互相借钱的习惯，难以记住谁欠谁，欠多少。

你的任务是实现一个简单的 [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer)  该api接收 [IOU](https://en.wikipedia.org/wiki/IOU)s （借条）作为 POST 请求, 并可以通过GET请求传递指定的摘要信息


### API Specification（api规范）

#### User object （用户对象）
```json
{
  "name": "Adam",
  "owes": {
    "Bob": 12.0,
    "Chuck": 4.0,
    "Dan": 9.5
  },
  "owed_by": {
    "Bob": 6.5,
    "Dan": 2.75,
  },
  "balance": "<(total owed by other users) - (total owed to other users)>"
}
```

#### Methods（方法）

| Description | HTTP Method | URL | Payload Format | Response w/o Payload | Response w/ Payload |
| --- | --- | --- | --- | --- | --- |
| List of user information（用户信息清单） | GET | /users | `{"users":["Adam","Bob"]}` | `{"users":<List of all User objects>}` | `{"users":<List of User objects for <users> (sorted by name)}` |
| Create user（创建用户） | POST | /add | `{"user":<name of new user (unique)>}` | N/A | `<User object for new user>` |
| Create IOU | POST | /iou | `{"lender":<name of lender>,"borrower":<name of borrower>,"amount":5.25}` | N/A | `{"users":<updated User objects for <lender> and <borrower> (sorted by name)>}` |


## 关于可变参数  **kwargs 的 巧妙用法
```python
database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {"Chuck": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Chuck", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
            ]
        }
bb=database['users'][2]

def f(name,owes=None,owed_by=None,**kwargs):
    print("name",name)
    print("owes",owes)
    print("owed_by",owed_by)
    

f(**bb)

输出：
bb= {'name': 'Chuck', 'owes': {}, 'owed_by': {'Bob': 3.0}, 'balance': 3.0}
name Chuck
owes {}
owed_by {'Bob': 3.0}

```
## 关于 functools.wraps 装饰器函数

```pthon

>>> from functools import wraps
>>> def my_decorator(f):
...     @wraps(f)
...     def wrapper(*args, **kwds):
...         print('Calling decorated function') # 先 打印 第一句
...         return f(*args, **kwds)  # 然后打印 第2句
...     return wrapper
...
>>> @my_decorator
... def example():
...     """Docstring"""
...     print('Called example function')
...
>>> example()
Calling decorated function
Called example function
>>> example.__name__
'example'
>>> example.__doc__
'Docstring'
```

## 我的实现
```python

import json


class RestAPI:
    def __init__(self, database=None):
        self.db=database
        
    def get(self, url, payload=None):
        if url=="/users":
            return json.dumps({"users":[user for user in self.db["users"] if user["name"] in json.loads(payload)["users"]]})

    def post(self, url, payload=None):
        if url=="/add":
            return json.dumps({"name": json.loads(payload)["user"], "owes": {}, "owed_by": {}, "balance": 0.0})
        
        elif url=="/iou":
            payload_py=json.loads(payload)
            lender,borrower,mount=payload_py["lender"],payload_py["borrower"],payload_py["amount"]
            iou_info=filter(lambda x:x['name'] in [lender,borrower],self.db['users'])
            
            for iou in iou_info:
                if iou["name"]==lender and borrower in iou['owes']:
                    if mount<=iou['owes'][borrower]:
                        iou['owes'][borrower]-=mount
                        if not iou['owes'][borrower]:
                            del iou['owes'][borrower]
                    else:
                        iou['owed_by'][borrower]=mount-iou['owes'][borrower]
                        del iou['owes'][borrower]
                        
                    iou["balance"]+=mount
                        
                elif iou['name']==borrower and lender in iou['owed_by']:
                    if mount<=iou['owed_by'][lender]:
                        iou['owed_by'][lender] -=mount
                        if not iou['owed_by'][lender]:
                            del iou['owed_by'][lender]
                        
                    else:
                        iou['owes'][lender]=mount-iou['owed_by'][lender]
                        del iou['owed_by'][lender]
                    
                    iou["balance"]-=mount
                    
                elif iou["name"]==lender and borrower not in iou['owes']:
                    borr=iou['owed_by']
                    borr[borrower]=borr.get(borrower,0)+mount
                    iou["balance"]+=mount
                    
                elif iou['name']==borrower and lender not in iou['owed_by']:
                    lend=iou['owes']
                    lend[lender]=lend.get(lender,0)+mount
                    iou["balance"]-=mount
                    

            new_iou={"users":[user for user in self.db["users"] if user['name'] in [lender,borrower]]}
            return json.dumps(new_iou)


```


## 别人的实现（虽然比较长，不过模块化做的好）便于维护

```python
from functools import wraps
import json


def json_io(func):
    @wraps(func)
    def dec(self, url, payload=None):
        if payload is not None and isinstance(payload, str):
            payload = json.loads(payload)
        return json.dumps(func(self, url, payload), indent=2)
    return dec


class User(object):
    def __init__(self, name, owed_by=None, owes=None, **kwargs):
        self.name = name
        self.records = {}
        for borrower, amount in (owed_by or {}).items():
            self.loan(borrower, amount)
        for lender, amount in (owes or {}).items():
            self.borrow(lender, amount)

    def borrow(self, borrower, amount):
        self.records[borrower] = self.records.get(borrower, 0) - amount

    def loan(self, lender, amount):
        self.records[lender] = self.records.get(lender, 0) + amount

    @property
    def owes(self):
        return {k: -v for k, v in self.records.items() if v < 0}

    @property
    def owed_by(self):
        return {k: v for k, v in self.records.items() if v > 0}

    @property
    def balance(self):
        return sum(self.records.values())

    @property
    def __dict__(self):
        return {
            'name': self.name,
            'owes': self.owes,
            'owed_by': self.owed_by,
            'balance': self.balance
        }


class RestAPI(object):
    def __init__(self, database=None):
        self.users = {
            user['name']: User(**user)
            for user in (database or {}).get('users', [])
        }

    @json_io
    def get(self, url, payload=None):
        if url == '/users':
            return {'users': [
                user.__dict__
                for name, user in sorted(self.users.items())
                if payload is None or name in payload['users']
            ]}

    @json_io
    def post(self, url, payload):
        if url == '/add':
            user = User(payload['user'])
            self.users[user.name] = user
            return user.__dict__
        elif url == '/iou':
            lender = self.users[payload['lender']]
            borrower = self.users[payload['borrower']]
            amount = payload['amount']
            lender.loan(borrower.name, amount)
            borrower.borrow(lender.name, amount)
            return {'users': sorted(
                [lender.__dict__, borrower.__dict__],
                key=lambda u: u['name']
            )}
        
        
        
```

### Other Resources（其他资源）:
- https://restfulapi.net/
- Example RESTful APIs
  - [GitHub](https://developer.github.com/v3/)
  - [Reddit](https://www.reddit.com/dev/api/)
  

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

To run the tests, run `pytest rest_api_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest rest_api_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/rest-api` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
