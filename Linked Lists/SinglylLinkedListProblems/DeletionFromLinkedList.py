# Write a function to delete a node from a singly linked list and return deleted_node. 
# The function should take the index(starting from 0) of the node to be deleted as a parameter.Write a function to delete a node 
# from a singly linked list and return deleted_node. The function should take the index(starting from 0) of the node to be deleted as a parameter.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def remove(self, index):
        
        if index < 0 or index >= self.length:
            return None
            
        if index == 0:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp
            
        if index == self.length - 1:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            
            temp = self.tail
            self.tail = current
            current.next = None
            self.length -= 1
            return temp
            
        
        current = self.head
        for _ in range(index-1):
            current = current.next
        target = current.next
        current.next = target.next
        target.next = None
        self.length -= 1
        return target
        
            
        
        
        
        
        
        
        
        
        
        