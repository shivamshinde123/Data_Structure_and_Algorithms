

## hash node class
class HashNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

## hashmap class
class HashMap:

    ## hash element array
    def __init__(self):
        self.capacity = 20
        self.size = 0
        self.arr = [None] * self.capacity
        ## dummy node: Used to mitigate the issues created by deletion of nodes
        self.dummy = HashNode(-1, -1)

    ## Hash function to find index for a key
    def hashCode(self, key):
        return hash(key) % self.capacity
    
    ## function to add new record i.e., a key-value pair
    def insertNode(self, key, value):
        temp = HashNode(key, value)

        ## using counter to avoid infinite loop while searching for empty space
        counter = 0
        ## apply hash function to find index for given key
        hashIndex = self.hashCode(key)

        ## find the next free space
        while self.arr[hashIndex] is not None and self.arr[hashIndex].key != key and self.arr[hashIndex].key != -1:
            if counter > self.capacity:
                return None
            hashIndex += 1
            hashIndex %= self.capacity
            counter += 1

        
        ## if new node to be inserted, increase the current size
        if self.arr[hashIndex] is None or self.arr[hashIndex].key == -1:
            self.size += 1
        
        ## actually inserting the node after finding the empty space
        self.arr[hashIndex] = temp

    def deleteNode(self, key):
        ## apply hash function to find the index for given key
        hashIndex = self.hashCode(key)

        ## finding the node with given key
        while self.arr[hashIndex] is not None:
            ## if node found
            if self.arr[hashIndex].key == key:
                temp = self.arr[hashIndex]

                ## insert dummy node here to avoid the issues while inserting or searching the nodes
                self.arr[hashIndex] = self.dummy

                ## reduce size
                self.size -= 1

                return temp.value
            hashIndex += 1
            hashIndex %= self.capacity
        
        ## if not found return None
        return None
    
    def get(self, key):
        ## Apply hash function to find the index for given key
        hashIndex = self.hashCode(key)
        counter = 0

        ## finding the node with given key
        while self.arr[hashIndex] is not None:
            ## using counter to avoid infinite loop
            if counter > self.capacity:
                return None
            
            ## if node is found, return its value
            if self.arr[hashIndex].key == key:
                return self.arr[hashIndex].value
            hashIndex += 1
            hashIndex %= self.capacity
            counter += 1
        
        ## if not found return None
        return None
    
    ## return the current size
    def sizeOfMap(self):
        return self.size
    
    ## return true if size is 0
    def isEmpty(self):
        return self.size == 0
    
    ## function to display stored key-value pairs
    def display(self):
        for i in range(self.capacity):
            if self.arr[i] is not None and self.arr[i].key != -1:
                print(f"Key = {self.arr[i].key}, Value = {self.arr[i].value}")
    



if __name__ == "__main__":
    h = HashMap()

    print(h.sizeOfMap())

    h.insertNode(1, 1)
    print(h.sizeOfMap())

    h.insertNode(2, 2)
    print(h.sizeOfMap())

    h.insertNode(2, 3)
    print(h.sizeOfMap())

    print(h.deleteNode(2))
    print(h.sizeOfMap())

    print(h.isEmpty())
    print(h.get(2))
    h.display()
