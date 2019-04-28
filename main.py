# Returns a+b
def add(a, b):
    return a + b

# Returns the nth fibonacci number
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
