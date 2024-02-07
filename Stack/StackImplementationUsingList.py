

def isEmpty(stack):
    return len(stack) == 0

def push(stack, element):
    stack.append(element)
    top = len(stack) - 1

def pop(stack):
    if isEmpty(stack):
        print("underflow")
    else:
        element = stack.pop()
        if isEmpty(stack):
            top = None
        else:
            top = len(stack) - 1

if __name__ == "__main__":
    stack=[]
    top=None
    push(stack,1)
    push(stack,2)
    push(stack,3)
    push(stack,4)
    pop(stack)
    pop(stack)
    print(stack)