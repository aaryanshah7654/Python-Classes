def log_args(func):
    def wrapper(*args,**kwargs):
        print(f"Argument where:{args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Aaryan")
greet("alice", greeting="Hi")

import time

def retry(func):
    def wrapper(*args, **kwargs):
        attempt = 3
        for i in range(attempt):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {i+1} failed with error: {e}")
                time.sleep(1) 
        print("All attempts failed.")
    return wrapper

@retry
def risky_operation():
    import random
    if random.random() < 0.7:
        raise ValueError("Something went wrong!")
    print("Success!")

risky_operation()

def cache(func):
    memory = {}

    def wrapper(*args):
        if args in memory:
            print("Fetching from cache")
            return memory[args]
        result = func(*args)
        memory[args] = result
        print("Calculating and storing result")
        return result

    return wrapper

@cache
def slow_add(a, b):
    print("Doing some slow math...")
    return a + b

print(slow_add(3, 4))  
print(slow_add(3, 4))  
