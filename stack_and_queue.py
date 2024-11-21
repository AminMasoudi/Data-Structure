class Stack:
    """
    # Stack DataStructure
    This is a simple example to show you how a stack works and you can see the difference between Stack and Queue
    However you can use LifoQueue from queue or similar things in collection lib
    >>> from queue import LifoQueue
    >>> from collections import SimpleQueue, dequeue 
    ry writing this yourself and using a linked list  
    To do this, you need to write a linked list class and then add some standard methods to it
    such as `__len__()`, `append()`, `pop()`, ... 
    """
    data: list[int|None] = []

    def push(self, new_data:int) -> None:
        self.data.append(new_data)

    def pop(self):
        assert self.data.__len__() != 0, "Stack is Empty"
        return self.data.pop(0)
    

class Queue:
    data: list[int| None] = []


    def enqueue(self, new_data:int) -> None:
        self.data.append(new_data)

    def dequeue(self):
        assert self.data.__len__() != 0, "Queue is Empty"
        return self.data.pop()
