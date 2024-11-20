from dataclasses import dataclass


"""
Think of a linked list as a tree

There are a number of nodes in this tree
Each node has a value of type int or None
And each node has a next node which is of node type

We have an empty node representing the head of the linked list
"""


# when the @dataclass decorator is used, it automatically generates special methods such as: __init__, __repr__, __eq__ .
@dataclass
class Node:
    """
    creates objects of type nodes

    """
    value: int = None
    next: "Node" = None


class LinkedList:
    __head = Node()

    @property
    def head(self):
        return self.__head

    def append(self, new_value:int):
        """
        we should walk through a list of nodes until the last one.
        last node has no next node.
        after that we set our new_node as the next of that last node. 
        """
        new_node = Node(value=new_value)
        node = self.__head
        while node.next != None:
            node = node.next
        node.next = new_node

    def search(self, value:int)-> int:
        """
        search for a value and return index of that if it exists. otherwise return -1
        """
        #TODO
        raise NotImplementedError

    
    def add_to(self, index:int, new_node: Node):
        """
        add the new node to the given index and shift the rest of the list.
        for example:
        list  [1, 3, 5]
        add_to(1,4)
        list  [1, 4, 3, 5]
        """
        #TODO
        raise NotImplementedError

    


def main():
    list = LinkedList()
    for i in range(10):
        list.append(i)

    print(list.head)



if __name__=="__main__":
    main()