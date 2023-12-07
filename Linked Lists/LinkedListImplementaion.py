
class Node:

    """This class is used to create the single node in the linked list"""

    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next   #############DOES THIS GIVE NEXT NODE OR ADDRESS OF THE NEXT NODE####################
    
    def set_next(self, next_node):

        """This method is used to create a new connection between a present node and newly created node"""

        self.__next = next_node


class LinkedList:
    
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self, data):

        """This method is used to add the new data at the end of a linked list"""
        new_node = Node(data)

        if (self.__head is None): 

            """Difference between == and is operators in Python. We use the is operator when we want to compare two objects' identities. On the other hand, we use the == operator when we want to compare the two objects' values."""

            self.__head = self.__tail = new_node # for linked list with only one node, head and tail node will be same
        else:
            self.__tail.set_next(new_node) # creating the new connection
            self.__tail = new_node # updating the tail

    def find_node(self, data):
        temp = self.__head
        while (temp is not None):
            if (temp.get_data() == data):
                return temp
            temp = temp.get_next()  #############DOES THIS GIVE NEXT NODE OR ADDRESS OF THE NEXT NODE####################
        return None
                
    
    def insert(self, data, data_before):

        """This method is used to insert the new data data after the already existing data data_before in a linked list
        i.e., data_before is the already present element in the linked list after which we wish to insert new node with data data"""

        new_node = Node(data)

        if (data_before == None): # if we want to insert a new element just before head
            new_node.set_next(self.__head) # creating connection with the head
            self.__head = new_node # updating the head 
            if (new_node.get_next() == None): # if newly inserted node is the last node
                self.__tail = new_node # updating the tail of the linked list

        else:
            node_before = self.find_node(data_before)
            if (node_before is not None):
                new_node.set_next(node_before.get_next()) # check the notes for clarification
                node_before.set_next(new_node) # check the notes for clarification
                if (new_node.get_next() is None):
                    self.__tail = new_node
            else:
                print(f"{data_before} is not present in the linked list")

    def display(self):
        temp = self.__head
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_next() #############DOES THIS GIVE NEXT NODE OR ADDRESS OF THE NEXT NODE####################

    def delete(self, data):

        """This method is used to delete the node with data data"""
        node = self.find_node(data)

        if (node is not None):
            if (node == self.__head):
                if (self.__head == self.__tail):
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while(temp is not None):
                    if (temp.get_next() == node):
                        temp.set_next(node.get_next())
                        if (node == self.__tail):
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(f"{data} is not present in Linked List")

    
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()

        msg = ", ".join(msg)
        msg = f"Linked List data (Head to Tail): [{msg}]"
        return msg




if __name__ == "__main__":

    marias_list = LinkedList()
    marias_list.add('Sugar')
    print(f"Maria's list after adding Sugar {marias_list}\n")

    marias_list.add('Tea Bags')
    marias_list.add('Milk')
    marias_list.add('Biscuit')
    print(f"Maria's list after adding three more items: {marias_list}\n")

    marias_list.insert('Salt', 'Sugar') 
    print(f"Maria's list after adding 'Salt' after 'Sugar': {marias_list}")

    marias_list.delete('Milk')
    print(f"Maria's list after deleting Milk: {marias_list}")

 

    