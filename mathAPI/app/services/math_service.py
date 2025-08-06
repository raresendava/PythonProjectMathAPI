import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 0: raise ValueError("Negative not allowed")
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a

@functools.lru_cache(maxsize=128)
def factorial(n: int) -> int:
    if n < 0: raise ValueError("Negative not allowed")
    result = 1
    for i in range(2, n + 1): result *= i
    return result

def calculate_operation(operation: str, a: int = None, b: int = None):
    if operation == "pow":
        if a is None or b is None:
            raise ValueError("Parameters a and b are required for pow")
        return a ** b
    elif operation == "fib":
        return fibonacci(a)
    elif operation == "fact":
        return factorial(a)
    else:
        raise ValueError("Unsupported operation")