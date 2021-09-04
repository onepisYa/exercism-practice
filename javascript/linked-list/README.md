# Linked List

Implement a doubly linked list.

Like an array, a linked list is a simple linear data structure. Several
common data types can be implemented using linked lists, like queues,
stacks, and associative arrays.

A linked list is a collection of data elements called *nodes*. In a
*singly linked list* each node holds a value and a link to the next node.
In a *doubly linked list* each node also holds a link to the previous
node.

You will write an implementation of a doubly linked list. Implement a
Node to hold a value and pointers to the next and previous nodes. Then
implement a List which holds references to the first and last node and
offers an array-like interface for adding and removing items:

实现一个双向链表。
像数组一样，链表是一个简单的线性数据结构。可以使用链接列表来实现几种常见的数据类型，例如队列，堆栈和关联数组。
链表是称为节点的数据元素的集合。在单链列表中，每个节点都包含一个值和到下一个节点的链接。在双向链表中，每个节点还拥有到前一个节点的链接。
您将编写一个双向链表的实现。实现一个节点来保存值和指向下一个和上一个节点的指针。然后实现一个List，该List包含对第一个和最后一个节点的引用，并提供用于添加和删除项目的类似数组的接口：


* `push` (*insert value at back*);
* `pop` (*remove value at back*);
* `shift` (*remove value at front*).
* `unshift` (*insert value at front*);

To keep your implementation simple, the tests will not cover error
conditions. Specifically: `pop` or `shift` will never be called on an
empty list.

If you want to know more about linked lists, check [Wikipedia](https://en.wikipedia.org/wiki/Linked_list).

Your list must also implement the following interface:

为了简化实施，测试将不涵盖错误情况。具体来说：弹出或移位永远不会在空列表中被调用。
如果您想了解有关链表的更多信息，请查看Wikipedia。
您的列表还必须实现以下接口：

- `delete` (delete the first occurence of a specified value)


## Setup

Go through the setup instructions for Javascript to install the necessary
dependencies:

[https://exercism.io/tracks/javascript/installation](https://exercism.io/tracks/javascript/installation)

## Requirements

Please `cd` into exercise directory before running all below commands.

Install assignment dependencies:

```bash
$ npm install
```

## Making the test suite pass

Execute the tests with:

```bash
$ npm test
```

In the test suites all tests but the first have been skipped.

Once you get a test passing, you can enable the next one by changing `xtest` to
`test`.


## Submitting Solutions

Once you have a solution ready, you can submit it using:

```bash
exercism submit linked-list.js
```

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have
completed the exercise.

## Exercise Source Credits

Classic computer science topic

