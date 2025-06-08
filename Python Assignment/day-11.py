           # QUEUE  (FIFO)
# Function to add an element to the queue
def add(queue_list, element):
    queue_list.append(element)

# Function to remove and return the first element from the queue
def deque(queue_list):
    if queue_list:
        return queue_list.pop(0)
    else:
        return "Queue is empty"

# Function to return (but not remove) the first element in the queue
def peek(queue_list):
    if queue_list:
        return queue_list[0]
    else:
        return "Queue is empty"

queue = []
add(queue, "A")
add(queue, "B")
add(queue, "C")

print("Queue:", queue)        
print("Peek:", peek(queue))   
print("Deque:", deque(queue)) 
print("Queue after deque:", queue)  

                # STACK    (LIFO)
# Push function: adds to the top of the stack
def push(stack_list, element):
    stack_list.append(element)

# Pop function: removes the top element
def pop(stack_list):
    if stack_list:
        return stack_list.pop()
    else:
        return "Stack is empty"

# Peek function: shows the top element
def peek(stack_list):
    if stack_list:
        return stack_list[-1]
    else:
        return "Stack is empty"

stack = []
push(stack, "A")
push(stack, "B")
push(stack, "C")

print("Stack:", stack)          
print("Pop:", pop(stack))        
print("Peek:", peek(stack))      
print("Final Stack:", stack)     