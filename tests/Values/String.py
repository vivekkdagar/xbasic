import unittest
from xbasic.string_value import String
from xbasic.number import Number


class TestString(unittest.TestCase):
    def test_addition(self):
        # Test addition with two strings
        string1 = String("Hello, ")
        string2 = String("world!")
        result, error = string1.added_to(string2)
        self.assertEqual(result.value, "Hello, world!")
        self.assertIsNone(error)

        # Test addition with a string and a non-string
        string3 = String("Hello, ")
        num = Number(123)
        result, error = string3.added_to(num)
        self.assertIsNone(result)
        self.assertIsNotNone(error)

    def test_multiplication(self):
        # Test multiplication of a string with a positive integer
        string1 = String("abc")
        num1 = Number(3)
        result, error = string1.multed_by(num1)
        self.assertEqual(result.value, "abcabcabc")
        self.assertIsNone(error)

        # Test multiplication of a string with zero
        string2 = String("abc")
        num2 = Number(0)
        result, error = string2.multed_by(num2)
        self.assertEqual(result.value, "")
        self.assertIsNone(error)

        # Test multiplication with a non-integer
        string3 = String("abc")
        num3 = Number(3.5)
        result, error = string3.multed_by(num3)
        self.assertIsNone(result)
        self.assertIsNotNone(error)

    def test_is_true(self):
        # Test truthiness of an empty string
        empty_string = String("")
        self.assertFalse(empty_string.is_true())

        # Test truthiness of a non-empty string
        non_empty_string = String("Hello")
        self.assertTrue(non_empty_string.is_true())

    def test_copy(self):
        # Test copying of a string
        string = String("Hello")
        copy = string.copy()
        self.assertEqual(copy.value, string.value)
        self.assertIsNot(copy, string)  # Check if a new instance is created

    def test_str_representation(self):
        # Test string representation
        string = String("Hello")
        self.assertEqual(str(string), "Hello")
        self.assertEqual(repr(string), '"Hello"')


if __name__ == "__main__":
    unittest.main()
