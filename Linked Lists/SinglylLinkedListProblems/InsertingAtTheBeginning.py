class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    # Implement Here
    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
        
        self.length += 1
            
            
            
        