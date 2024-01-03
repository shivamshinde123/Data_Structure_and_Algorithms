
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

    """
    The 'search' method retrieves the value associated with a given key.
    It first gets the index where key-value pair should be stored using _hash
    method. It then search the linked list at that index for the key. If it
    finds the key, it returns the associated value. If it doesn't find the key,
    it raises a KeyError
    """

    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)
    

    """
    The 'remove' methods removes a key-value pair from the hash-table. It
    first gets the index where the pair should be stored using '_hash' method.
    It then searches the linked list at that index for the key. If it finds the key,
    it removes the node from the list. If it doesn't find the key, it raises a 'keyError'.
    """

    def remove(self, key):
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return 
            previous = current
            current = current.next

        raise KeyError(key)
    
    """
    __str__ method returns a string representation of the hash table
    """

    def __Str__(self):
        elements = []

        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key,current.value))
                current = current.next
        return str(elements)
    
    """__len__ magic method"""
    def __len__(self):
        return self.size
    
    """__contains magic method"""
    def __contains__(self,key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False
        

 # Driver code 
if __name__ == '__main__': 
  
    # Create a hash table with 
    # a capacity of 5 
    ht = HashTable(5) 
  
    # Add some key-value pairs 
    # to the hash table 
    ht.insert("apple", 3) 
    ht.insert("banana", 2) 
    ht.insert("cherry", 5) 
  
    # Check if the hash table 
    # contains a key 
    print("apple" in ht)  # True 
    print("durian" in ht)  # False 
  
    # Get the value for a key 
    print(ht.search("banana"))  # 2 
  
    # add the value for a key 
    ht.insert("strawberry", 4) 
    print(ht.search("banana"))  # 4 
  
    ht.remove("apple") 
    # Check the size of the hash table 
    print(len(ht))  # 3