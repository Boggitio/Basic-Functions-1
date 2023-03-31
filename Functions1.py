import math
import unittest

#1 - This function takes a desired radius of a circle as input and returns that circle's aria.
def ex1(r):
    AreaCircle = math.pi * r * r
    return(f"Circle's area is: {AreaCircle}.")
#ex1('PyCharm')

#2 - This function finds the factorial of a given number and returns the answer.
def factorial(x):
    #x = int(input("Insert a number to find out it's factorial: "))
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))
    result = factorial(x)
    return(f"Factorial of  {x} is {result}.")
#factorial()

#3 - This function asks for 3 numbers as input and finds then returns which one of them is the highest one.
def HigherN(x, y, z):
    #x = int(input("Specify the first number  "))
    #y = int(input("Specify the second number  "))
    #z = int(input("Specify the third number  "))
    if x > y:
        if x > z:
            return(f"Highest number is  {x}.")
        else:
            return(f"Highest number is  {z}.")
    else:
        if y > z:
            return(f"Highest number is  {y}.")
        else:
            return(f"Highest number is  {z}.")
#HigherN()

#4 - This function checks if a given number is prime or not and returns the answer.
def checkPrime(n):
    #n = int(input("What number would you like to check if they're prime?   "  ))
    if n <= 1:
       return("It's not a prime number.")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return("It's not a prime number.")
                break
        else:
            return("It is a prime number.")
#checkPrime()

#5 - This function prints the fibonacci sequence up to the number you've chosen as parameter.
def fibonacci(n):
    fib_seq = [0, 1] # initialize sequence with the first two numbers
    a, b = 0, 1
    while a + b <= n:
        a, b = b, a + b
        fib_seq.append(b) # add the next Fibonacci number to the sequence
    return fib_seq
#fibonacci(72)
#print(fibonacci(72))