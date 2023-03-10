import math
#1 - This function takes a desired radius of a circle as input and returns that circle's aria.
def AriaCircle(r):
    r = int(input("Specify the radius of a circle: "))
    AriaCircle = math.pi * r * r
    print("Circle's aria is: ", AriaCircle)
AriaCircle('PyCharm')

#2 - This function finds the factorial of a given number and returns the answer.
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))
x = int(input("Insert a number to find out it's factorial: "))
result = factorial(x)
print("Factorial of ", x, " is ", result)
factorial(x)

#3 - This function asks for 3 numbers as input and finds then returns which one of them is the highest one.
def HigherN():
    x = int(input("Specify the first number  "))
    y = int(input("Specify the second number  "))
    z = int(input("Specify the third number  "))
    if x > y:
        if x > z:
            print("Highest number is ", x)
        else:
            print("Highest number is ", z)
    else:
        if y > z:
            print("Highest number is ", y)
        else:
            print("Highest number is ", z)
HigherN()

#4 - This function checks if a given number is prime or not and returns the answer.
def checkPrime():
    n = int(input("What number would you like to check if they're prime?   "  ))
    if n <= 1:
       print("It's not a prime number.")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print("It's not a prime number.")
                break
        else:
            print("It is a prime number.")
checkPrime()

#5 - This function prints the fibonacci sequence up to the number you've chosen as parameter.
def fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b
fibonacci(72)
