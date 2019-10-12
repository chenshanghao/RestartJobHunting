# Function to create a stack
def createStack():
    stack = []
    return stack

# Function to check if the stack is empty
def isEmpty(stack):
    return len(stack) == 0

# Function to push an item to stack
def push(stack, item):
    stack.append(item)

# Function to get top item of stack
def top(stack):
    if isEmpty(stack):
        return None
    p = len(stack)
    return stack[p-1]

# Function to pop an item from stack
def pop(stack):
    if isEmpty(stack):
        print("Stack Underflow")
        exit()
    return stack.pop()

# Function to print the stack
def prints(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end = ' ')
    print()

# Function to return the sorted stack
def sortStack(stack):
    tmpStack = createStack()

    while(not isEmpty(stack)):
        # pop out the first element 
        tmp = top(stack) 
        pop(stack)

        # while temporary stack is not empty and top of stack is greater than temp
        while(not isEmpty(tmpStack) and int(top(tmpStack)) > int(tmp)):
            # pop from temporary stack and push it to the input stack 
            push(stack， top(tmpStack))
            pop(tmpStack)

        # push temp in tempory of stack
        push(tmpStack, tmp)
    return tmpStack
