import time

def my_decorator(func_obj):
    def wrapped(*args, **kwargs):
        print('Start time: %d' % time.time())
        return_obj = func_obj(*args, **kwargs)
        print('End time: %d' % time.time())
        return return_obj
    return wrapped


    def my_func(name):
        print("Hello world! is" % name)


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            print('Finding the valude for %d' % x)
            memo[x] = f(x)
        print('Factorial for %d is %d' % (x, memo[x]))
        return memo[x]
    return helper

@memoize
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#factorial(5)



def memoize(l):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = l(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n-1) * fib(n-2))

#fib(10)

class Foo(object):
    val = 5
    a = Foo()


def rest():
    
