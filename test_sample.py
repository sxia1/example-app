from main import *

def test_add():
    assert add(1,2) == 3

def test_fib0():
    assert fib(10) == 55

def test_fib1():
    answer = [0,1,1,2,3,5,8,13,21,34]
    assert [fib(n) for n in range(10)] == answer
