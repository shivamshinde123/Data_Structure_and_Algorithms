

class Stack:

    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        return (self.__top == self.__max_size - 1)
    
    def is_empty(self):
        return (self.__top == -1)
    
    def push(self, data):
        if (self.is_full()):
            print("The stack is full!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if (self.is_empty()):
            print("The stack is empty!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data
        
    def display(self):
        if (self.is_empty()):
            print("The stack is empty")
        else:
            index = self.__top
            while (index >= 0):
                print(self.__elements[index])
                index -= 1

    def get_max_size(self):
        return self.__max_size

    def __str__(self):
        msg = list()
        index = self.__top
        while (index >= 0):
            msg.append(str(self.__elements[index]))
            index -= 1
        msg = ", ".join(msg)
        msg = f"Stack data (Top to Bottom): [{msg}]"
        return msg


if __name__ == "__main__":

    stack1 = Stack(5)
    stack1.push('Shirt1')

    print(f"Stack after adding one shirt: {stack1}\n")

    stack1.push('Shirt2')
    stack1.push('Shirt3')
    stack1.push('Shirt4')
    stack1.push('Shirt5')
    print(f"Stack after adding all the 5 shirts: {stack1}\n")

    stack1.pop()
    print(f"Stack after one pop operation: {stack1}")

    stack1.pop()
    stack1.pop()
    stack1.pop()
    print(f"Stack after 3 more pop operations: {stack1}")

    