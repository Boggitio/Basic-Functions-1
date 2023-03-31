import unittest
import Functions1

class TestFunctions1(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(Functions1.ex1(33), "Circle's area is: 3421.194399759285.")
        self.assertEqual(Functions1.ex1(72), "Circle's area is: 16286.016316209487.")
        self.assertEqual(Functions1.ex1(-12), "Circle's area is: 452.3893421169302.")

    def test_factorial(self):
        self.assertEqual(Functions1.factorial(5), 120)
        self.assertEqual(Functions1.factorial(11), 39916800)

    def test_HigherN(self):
        self.assertEqual(Functions1.HigherN(144, 15, -1), "Highest number is  144.")
        self.assertEqual(Functions1.HigherN(1332989, 45.2, 1998), "Highest number is  1332989.")

    def test_checkPrime(self):
        self.assertEqual(Functions1.checkPrime(22), "It's not a prime number.")
        self.assertEqual(Functions1.checkPrime(-33), "It's not a prime number.")
        self.assertEqual(Functions1.checkPrime(11), "It is a prime number.")

    def test_fibonacci(self):
        self.assertEqual(Functions1.fibonacci(72), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(Functions1.fibonacci(500), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])