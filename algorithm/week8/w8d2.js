/** @format */

class Node {
    constructor(data) {
        this.data = data
        this.next = null
    }
}

// Queue
// FIFO (First in, first out)

// - enqueue
// - dequeue
// - peek
// - isEmpty
// - count

class Queue {
    constructor() {
        this.front = null // sometimes called head "front of the line"
        this.back = null // sometimes called rear or tail "back of the line"
        this.length = 0
    }

    // add nodes to the back of the queue
    enqueue(node) {
        this.front = this.front == null && node // if this.front == null. then this.front = node
        node.next = this.back // points the node.next to the current back
        this.back = node // insert node to this.back
        this.length++
    }

    // remove from the front
    dequeue() {
        if (this.front != null) {
            let removed = this.front
            this.front = this.front.next
            this.length--
                return removed
        }
        return null
    }

    // check the front of the queue
    peek() {
        return this.front ? this.front.data : this.front
    }

    // return true / false if queue is empty
    isEmpty() {
        return this.front == null
    }

    // return length
    count() {
        return this.length
    }
}

// NINJA BONUS:
// print every value in the queue
// you may only use one queue or stack for additional storage
// return the queue back to it's original order when you are done
// you are not allowed to linearly traverse the queue
// only use public methods enqueue(), dequeue(), peek(), isEmpty(), and count()
function readQueue(queue) {
    let tempQ = new Queue()
    while (!queue.isEmpty()) {
        let itsNode = queue.dequeue()
        console.log(itsNode.data)
        console.log("check mark")
        tempQ.enqueue(itsNode)
    }
    queue.front = tempQ.front
    queue.back = tempQ.back
    queue.length = tempQ.length
}

let a = new Queue()
a.enqueue(new Node(1))
a.enqueue(new Node(2))
readQueue(a)