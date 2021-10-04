/**
 * /* Stacks
 *
 * A stack is a LIFO data structure
 * LAST IN, FIRST OUT
 * LIFO / FILO
 *
 * push - add to top
 * pop - remove from top
 * peek - check the top
 * isEmpty - check if the stack is empty, true/false
 * length - return size of stack
 *
 * @format
 */

class Node {
    constructor(data) {
        this.data = data
        this.next = null
    }
}

class slStack {
    constructor() {
        this.top = null // this.head, this.end
        this.length = 0
    }

    // add to top
    push(newNode) {
        newNode.next = this.top
        this.top = newNode
        this.length++
    }

    // remove from top
    pop() {
        let popped = this.top.data
        this.top = this.top.next
        this.length--
            return popped
    }

    // aka check top
    peek() {
        return this.top
    }

    // check if empty
    isEmpty() {
        return this.top == null
    }

    // "1" == 1 //true
    // "1" === 1 //false

    // length getter
    getLength() {
        return this.length
    }
}

// don't forget to instantiate the slStack!
// add a few nodes first