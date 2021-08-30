'''
Code modified from Single Linked List, adding in the feature node.prev
'''


class DLNode:
    def __init__(self, val):
        self.prev = None
        self.value = val
        self.next = None


class DList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = DLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node  # SET the list's head TO the node we created in the last step
        return self  # return self to allow for chaining

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next  # set the runner to its neighbor
        return self  # once the loop is done, return self to allow for chaining

    def add_to_back(self, val):
        if self.head == None:  # if the list is empty
            self.add_to_front(val)  # run the add_to_front method
            return self  # let's make sure the rest of this function doesn't happen if we add to the front
        new_node = DLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node  # increment the runner to the next node in the list
        new_node.prev = runner
        return self  # return self to allow for chaining

    # code challange
    def remove_from_front(self):
        runner = self.head
        if runner.next == None:
            self.head = None
        else:
            self.head = runner.next
            self.head.prev = None
        return self  # return self to allow for chaining

    def remove_from_back(self):
        runner = self.head
        runner2 = runner.next
        if runner.next == None:
            return self.remove_from_front()
        while (runner2.next != None):
            runner = runner.next
            runner2 = runner2.next
        runner.next = None
        return runner2.value

    def remove_val(self, val):
        if self.head.value == val:
            return self.remove_from_front()
        runner = self.head
        runner2 = runner.next
        while (runner2.value != val):
            runner = runner.next
            runner2 = runner2.next
        if runner2.next == None:
            return self.remove_from_back()
        runner.next = runner2.next
        return self

    # the following part of the code has not been tested but it should be right theoratically
    def insert_at(self, val, n):
        if n == 0: return self.add_from_front(val)
        runner = self.head
        for x in n:
            runner = runner.next
        if runner.next == None: return self.add_to_back(val)
        new_node = DLNode(val)
        new_node.prev = runner
        new_node.next = runner.next
        runner.next = new_node
        return self


my_list = DList()  # create a new instance of a list
# chaining, yeah!
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back(
    "fun!").print_values()
# output should be:
# Linked lists
# are
# fun!
