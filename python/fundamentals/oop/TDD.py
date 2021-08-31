import unittest


def reverseList(arr):
    for x in range(0, int(len(arr) / 2)):
        tmp = arr[x]
        arr[x] = arr[len(arr) - 1 - x]
        arr[len(arr) - 1 - x] = tmp
    return arr


class reverseListTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])

    def testTwo(self):
        self.assertEqual(reverseList([1]), [1])

    def testThree(self):
        self.assertEqual(reverseList([1, 3, 5, 0]), [0, 5, 3, 1])

    def testFour(self):
        self.assertEqual(reverseList([1, 0, 1, 0, 1]), [1, 0, 1, 0, 1])


def isPalindrome(str):
    for x in range(0, int(len(str) / 2)):
        if str[x] != str[len(str) - x - 1]:
            return False
    return True


class isPalindromeTest(unittest.TestCase):
    def test(self):
        self.assertTrue(isPalindrome("racecar"))

    def testTwo(self):
        self.assertFalse(isPalindrome("rabcr"))

    def testThree(self):
        self.assertTrue(isPalindrome("madam"))

    def testFour(self):
        self.assertTrue(isPalindrome("redivider"))

    def testFive(self):
        self.assertFalse(isPalindrome("apple"))

    def testSix(self):
        self.assertTrue(isPalindrome("reviver"))

    def testSeven(self):
        self.assertFalse(isPalindrome("divided"))


def coin(cents):
    change = []
    change.append(int(cents / 25))
    cents %= 25
    change.append(int(cents / 10))
    cents %= 10
    change.append(int(cents / 5))
    cents %= 5
    change.append(cents)
    return change


class coinTest(unittest.TestCase):
    def test(self):
        self.assertEqual(coin(87), [3, 1, 0, 2])

    def testTwo(self):
        self.assertEqual(coin(1), [0, 0, 0, 1])

    def testThree(self):
        self.assertEqual(coin(50), [2, 0, 0, 0])

    def testFour(self):
        self.assertEqual(coin(5), [0, 0, 1, 0])

    def testFive(self):
        self.assertEqual(coin(15), [0, 1, 1, 0])

    def testSix(self):
        self.assertEqual(coin(36), [1, 1, 0, 1])


def factorial(num):
    if num == 0:
        return 0
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


class factorialTest(unittest.TestCase):
    def test(self):
        self.assertEqual(factorial(5), 120)

    def testTwo(self):
        self.assertEqual(factorial(1), 1)

    def testThree(self):
        self.assertEqual(factorial(2), 2)

    def testFour(self):
        self.assertEqual(factorial(0), 0)

    def testFive(self):
        self.assertEqual(factorial(3), 6)

    def testSix(self):
        self.assertEqual(factorial(4), 24)


def finbonacci(num):
    current = 0
    next = 1
    for x in range(num):
        tmp = current
        current = next
        next = tmp + next
    return current


class finbonacciTest(unittest.TestCase):
    def test(self):
        self.assertEqual(finbonacci(5), 5)

    def testTwo(self):
        self.assertEqual(finbonacci(4), 3)

    def testThree(self):
        self.assertEqual(finbonacci(1), 1)

    def testFour(self):
        self.assertEqual(finbonacci(2), 1)

    def testFive(self):
        self.assertEqual(finbonacci(0), 0)


if __name__ == "__main__":
    unittest.main()
