# Write a function to reverse a singly linked list. The function should reverse the original linked list.

# Example:

# Original singly linked list:   1 -> 2 -> 3 -> 4 -> 5

# Reversed singly linked list:  5 -> 4 -> 3 -> 2 -> 1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def reverse(self):
        
        prev_node = None
        current_node = self.head
        
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        self.head, self.tail = self.tail, self.head
        
            
            
            
            
            
            
        
            