
## Initialize the node
class Node:

    def __init__(self, data):
        # adding an element to the node
        self.data = data 
        # initially the node won't be linked to any element in either directions
        self.next = None 
        self.prev = None


## Class for doubly linked list
class doublyLinkedList:
    
    def __init__(self):
        self.head = None # Initially there are no elements in the list
        self.tail = None

    ## Finding the node with given data value
    def searchNode(self, data):
        x = self.head

        if x == None:
            print("Linked list is empty")
        
        while x != None:
            if x.data == data:
                return x
            else:
                x = x.next
        
        print("Did not find the node with given value")

    # Adding an element before the first element
    def pushFront(self, data): 
        # Creating a new node with the desired value
        new_node = Node(data) 

        # Newly created node's next pointer will the head of the linked list
        new_node.next = self.head

        if self.head != None: # Checks if the list is empty or not
            self.head.prev = new_node 
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None

    # Adding an element after the last element of the linked list
    def pushBack(self, data):
        # Creating a new node with the desired value
        new_node = Node(data) 

        # Newly created node's previous pointer will be the tail of a linked list
        new_node.prev = self.tail

        
        if self.tail != None: # Checks if the list is empty or not
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node 
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None

    # Finding the first element and return it
    def peekFront(self):
        if self.head != None:
            return self.head.data
        else:
            print("List is empty")

    # Finding the last element and return it
    def peekBack(self):
        if self.tail != None:
            return self.tail.data
        else:
            print("List is empty")

    # Finding element at particular index value
    def peekAtIndex(self, index):
        x = self.head

        if x == None:
            print("Linked List is empty")
        
        while x != None:
            for i in range(index):
                x = x.next
            return x.data


    # Removing and returning the first element
    def popFront(self):

        if self.head == None:
            print("List is empty")
        
        else:
            old_head = self.head
            old_head.next.prev = None
            self.head = old_head.next
            old_head.next = None
            return old_head.data
    
    # Removing and returning the last element
    def popBack(self):

        if self.tail == None:
            print("List is empty")
        
        else:
            old_tail = self.tail
            old_tail.prev.next = None
            self.tail = old_tail.prev
            old_tail.prev = None
            return old_tail.data
        
    # Insert a new node after the given node
    def insertAfter(self, already_present_node, new_data):

        if already_present_node == None:
            print("Given node is empty")
        
        else:
            new_node = Node(new_data)
            new_node.next = already_present_node.next
            already_present_node.next = new_node
            new_node.prev = already_present_node

            if new_node.next != None:
                new_node.next.prev = new_node

            if already_present_node == self.tail:
                self.tail = new_node

    # Insert a new node before the given node
    def insertBefore(self, already_present_node, new_data):

        if already_present_node == None:
            print("Given node is empty")
        
        else:
            new_node = Node(new_data)
            new_node.next = already_present_node
            new_node.prev = already_present_node.prev
            already_present_node.prev = new_node

            if new_node.prev != None:
                new_node.prev.next = new_node

            if already_present_node == self.head:
                self.head = new_node

    def __str__(self):
        print("The values of nodes in the linked list are:")
        x = self.head

        if x == None:
            print("Linked List is empty")
        
        while x != None:
            print(x.data)
            x = x.next


if __name__ == "__main__":

    d = doublyLinkedList()

    d.pushFront(10)

    d.pushBack(20)
    d.pushBack(50)
    d.pushBack(19)
    d.pushBack(38)
    d.pushBack(28)
    d.pushBack(58)

    d.pushFront(100)

    d.insertAfter(d.searchNode(58),44)
    d.insertBefore(d.searchNode(10), 99)
    d.insertBefore(d.searchNode(38), 543)
    d.insertBefore(d.searchNode(20), 67)

    print(d.peekFront())
    print(d.peekBack())
    print(d.peekAtIndex(2))
    print()
    d.__str__()
    

    
