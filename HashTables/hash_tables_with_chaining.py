
"""
Node class will represent a node in a linked list. Each node will
contain a key-value pair, as well as a pointer to the next node in the
linked list
"""
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


"""
The 'HashTable' class will contain the array that will hold the linked
list, as well as methods to insert, retrieve, and delete data from the 
hash table
"""


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity
    
    """
    The 'insert' method will insert a key-value pair into the hash table.
    It takes the index where the pair should be stored using '_hash' method.
    If there is no node at that index, it creates a new node with the 
    key-value pair and sets it as the head of the list.
    If there is a node at that index, it will iterate through the list till the last
    node is found and if the key already exists, then it will update the value. Else it will 
    create a new node and add it to the head of the list 
    """

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None: # if the slot at index is empty
            self.table[index] = Node(key, value)
            self.size += 1

        else: # if the slot at index isn't empty
            # if the key already exists in the list
            current = self.table[index] 
            while current: 
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            # if key doesn't already exist in list
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    

 