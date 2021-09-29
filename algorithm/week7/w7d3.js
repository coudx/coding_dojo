/** @format */

class Node {
    constructor(data) {
        this.data = data
        this.next = null
    }
}

class SLL {
    constructor() {
            this.head = null
        }
        // return true or false if this.head is null
    isEmpty() {
        return this.head == null
    }

    // add given node to the head, if it exists. return void
    addToFront(node) {
        node.next = this.head // set the new node's next to the head
        this.head = node // move the head to the new node
    }

    // create a new node with given data, add it to the head. return void
    addDataToFront(data) {
        addToFront(new Node(data))
    }

    // ---------------------------------
    // console log (print) the data of every node in the current list
    // traversal
    read() {
        let runner = this.head
        while (runner) {
            console.log(runner.data)
            runner = runner.next
        }
    }

    // find: return true / false if current list contains a data equal to value
    contains(value) {
        let runner = this.head
        while (runner) {
            if (runner.value == value) {
                return true
            }
            runner = runner.next
        }
        return false
    }

    // Remove from front: remove and return the first node in the SLL
    removeFromFront() {
        let node = this.head
        this.head = this.head ? this.head.next : null
        return node
    }
}

// ⚠ don't forget to instantiate the Singly Linked List
// instantiate the SLL
var myList = new SLL()

// creating nodes
var myNode = new Node(11)

// executing methods:
myList.addToFront(myNode)
myList.addToFront(new Node(22))
myList.addToFront(new Node(33))
myList.addToFront(new Node(44))
myList.read()