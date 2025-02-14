
import time
import random

def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} call executed in {elapsed_time:.4f} sec")
        return result
    return wrapper

@decorator_1
def func():
    print("Starting the function")
    result = 0
    n = random.randint(20, 500)
    for i in range(n):
        result += (i ** 3)

@decorator_1
def funx(n=3, m=10):
    print("Processing serious task")
    max_val = float('-inf')
    n = random.randint(20, 500)
    res = [pow(i, 3) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
