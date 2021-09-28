/** @format */

class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

class SLL {
    constructor() {
        this.head = null
    }

    isEmpty() {
        if (this.head) {
            return false
        } else {
            return true
        }
    }

    // when a pointer is to the LEFT of an equal sign, we are CHANGING it
    // when a pointer is to the RIGHT of an equal sign, we are READING it

    // add given node to the head, if it exists. return void
    // list is empty?
    // list already has nodes?
    addToFront(node) {
        node.next = this.head
        this.head = node
        return this
    }

    // create a new node with given data, add it to the head. return void
    addDataToFront(data) {
        return this.addToFront(new Node(data))
    }
}

// instantiate the SLL
var myList = new SLL()

// creating nodes
var myNode = new Node(11)

// executing methods:
myList.addToFront(myNode)
console.log(myList.head.value)
    // myList.addToFront(new Node(11));