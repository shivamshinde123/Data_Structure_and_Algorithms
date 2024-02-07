
# queue = []

def isEmpty(queue):
    return len(queue) == 0

## Adding elements to the queue at the rear end
def enqueue(queue, element):
    queue.insert(0, element)


## Removing the front element from the queue
def dequeue(queue):
    if isEmpty(queue):
        print("underflow")
    else:
        return queue.pop()
    
if __name__=="__main__":
   queue=[]
   enqueue(queue, 5)
   enqueue(queue, 6)
   enqueue(queue, 9)
   enqueue(queue, 5)
   enqueue(queue, 3)
   print("Popped Element is: "+str(dequeue(queue)))