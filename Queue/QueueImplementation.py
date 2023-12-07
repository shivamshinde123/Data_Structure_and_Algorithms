
class Queue:

    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        return (self.__rear == self.__max_size - 1)

    def is_empty(self):
        return (self.__front > self.__rear)
    
    def enqueue(self, data):
        if (self.is_full()):
            print("Queue is full!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if (self.is_empty()):
            print("Queue is empty!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data
    
    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size
    
    def __str__(self):
        msg = list()
        index = self.__front
        while (index <= self.__rear):
            msg.append(self.__elements[index])
            index += 1

        msg = ", ".join(msg)
        msg = f"Queue data (Front to Rear): [{msg}]"
        return msg
    


if __name__ == "__main__":

    queue1 = Queue(5)
    queue1.enqueue('Tom')
    print(f"Queue after en-queuing one person: {queue1}\n")

    queue1.enqueue('Dick')
    queue1.enqueue('Harry')
    queue1.enqueue('Jack')
    queue1.enqueue('Maria')
    print(f"Queue after en-queuing 4 more people: {queue1}\n")

    queue1.dequeue()
    print(f"Queue after de-queuing once: {queue1}\n")

    queue1.dequeue()
    print(f"Queue after de-queuing again: {queue1}")






