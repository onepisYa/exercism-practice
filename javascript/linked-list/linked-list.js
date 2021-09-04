    // This is only a SKELETON file for the 'Linked List' exercise. It's been provided as a
    // convenience to get you started writing code faster.
    //
    "use strict";
    class Node {
        constructor(value) {
            this.value = value;
            this.next = null;
            this.pre = null;
        }
    }

    // -----------------------
    export class LinkedList {

        constructor(...items) {
            this.size = 0;
            if (items.length) {
                items.forEach(item => {
                    this.push(item);
                })

            } else {
                this.head_node = null;
                this.tail_node = null;

            }

        }

        push(item) {
            // tail insert
            //
            if (!this.head_node) {
                this.head_node = new Node(item);
                this.tail_node = this.head_node;
            } else {
                let node = new Node(item);
                let cur_node = this.head_node
                while (cur_node.next != null) {
                    cur_node = cur_node.next;
                }
                cur_node.next = node;
                node.pre = cur_node;
                this.tail_node = node;
            }
            this.size++

        }

        pop() {
            // tail remove
            //
            if (!this.size) {
                throw new Error("size 0 ");
            }
            let result;
            if (this.tail_node == this.head_node) {
                result = this.tail_node.value;
                this.tail_node = null;
                this.head_node = null;

            } else {
                result = this.tail_node.value;
                this.tail_node.pre.next = null;
                this.tail_node = this.tail_node.pre;
            }
            this.size--;
            return result;
        }

        shift() {
            // head revmove
            //
            if (!this.size) {
                throw new Error("size 0 ");
            }
            let result = this.head_node.value;
            if (this.size <= 1) {
                this.head_node = null;
                this.tail_node = null;
                this.size = 0;
            } else {
                this.head_node.next.pre = null;
                this.head_node = this.head_node.next;
                this.size--;
            }


            return result;
        }

        unshift(item) {
            // head insert
            //
            if (this.size == 0) {
                this.push(item);
            } else {
                let node = new Node(item);
                this.head_node.pre = node;
                node.next = this.head_node;
                this.head_node = node;
                this.size++;
            }
        }

        delete(item) {
            // delete
            if (!this.size) {
                throw new Error("not delete the LinkedList of size 0");
            }
            let cur_node = this.head_node;
            if (cur_node.value == item) {
                this.shift();
                return;
            } else if (this.tail_node.value == item) {
                this.pop();

            } else if (cur_node.next) {
                while (cur_node.next) {
                    if (cur_node.value == item) {
                        cur_node.pre.next = cur_node.next;
                        cur_node.next.pre = cur_node.pre;
                        this.size--;
                        break
                    }
                    cur_node = cur_node.next;

                }

            }

        }

        count() {
            //
            return this.size
        }
    }

    // -----------------------
    let arr = [1, 2, 5, 7, 10];
    let list = new LinkedList(...arr);
    let list_2 = new LinkedList(1);
    let list_1 = new LinkedList();
    console.log(list);
    console.log(list_2);
    console.log(list_1)