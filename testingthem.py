def fibonacci(n):
    fib_seq = [0, 1] # initialize sequence with the first two numbers
    a, b = 0, 1
    while a + b <= n:
        a, b = b, a + b
        fib_seq.append(b) # add the next Fibonacci number to the sequence
    return fib_seq
fibonacci(500)
print(fibonacci(500))