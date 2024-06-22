# Given a singly linked list, write a function that removes all the duplicates. use this linked list .

# Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"

# Result Linked List - "1 -> 2 -> 4 -> 3


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def remove_duplicates(self):
        if self.head is None:
            return
        
        node_values = set()
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next is not None:
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
                
        
        self.tail = current_node
        
        
        
        
        
        
        
        
        
        