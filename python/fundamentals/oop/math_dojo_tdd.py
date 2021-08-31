import unittest


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        # your code here
        self.result += num
        for number in nums:
            self.result += number
        return self

    def subtract(self, num, *nums):
        # your code here
        self.result -= num
        for number in nums:
            self.result -= number
        return self

        # create an instance:


md = MathDojo()
# to test:
class mathdojoTest(unittest.TestCase):
    def test(self):
        self.assertEqual(md.add(2).add(2, 5, 1).subtract(3, 2).result, 5)


if __name__ == "__main__":
    unittest.main()
