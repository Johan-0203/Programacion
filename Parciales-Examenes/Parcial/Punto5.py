def fib(n):
    a = 0
    b = 1
    while (n>1):
        n = n-1
        a, b = b, a+b
    return a

print(fib(1))
print(fib(10))
print(fib(4))
print(fib(6))
print(fib(20))
print(fib(100))