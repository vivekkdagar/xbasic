import unittest
from xbasic.number import Number


class TestNumber(unittest.TestCase):
    def test_arithmetic_operations(self):
        # Addition
        num1 = Number(5)
        num2 = Number(3)
        result, error = num1.added_to(num2)
        self.assertEqual(result.value, 8)
        self.assertIsNone(error)

        # Subtraction
        result, error = num1.subbed_by(num2)
        self.assertEqual(result.value, 2)
        self.assertIsNone(error)

        # Multiplication
        result, error = num1.multed_by(num2)
        self.assertEqual(result.value, 15)
        self.assertIsNone(error)

        # Division
        result, error = num1.dived_by(num2)
        self.assertAlmostEqual(result.value, 1.6666666666666667)
        self.assertIsNone(error)

        # Division by zero
        zero = Number(0)
        result, error = num1.dived_by(zero)
        self.assertIsNone(result)
        self.assertIsNotNone(error)

        # Power
        result, error = num1.powed_by(num2)
        self.assertEqual(result.value, 125)
        self.assertIsNone(error)

    def test_comparison_operations(self):
        # Equal
        num1 = Number(5)
        num2 = Number(5)
        result, error = num1.get_comparison_eq(num2)
        self.assertEqual(result.value, 1)
        self.assertIsNone(error)

        # Not Equal
        result, error = num1.get_comparison_ne(num2)
        self.assertEqual(result.value, 0)
        self.assertIsNone(error)

        # Less than
        result, error = num1.get_comparison_lt(num2)
        self.assertEqual(result.value, 0)
        self.assertIsNone(error)

        # Greater than
        result, error = num1.get_comparison_gt(num2)
        self.assertEqual(result.value, 0)
        self.assertIsNone(error)

        # Less than or equal to
        result, error = num1.get_comparison_lte(num2)
        self.assertEqual(result.value, 1)
        self.assertIsNone(error)

        # Greater than or equal to
        result, error = num1.get_comparison_gte(num2)
        self.assertEqual(result.value, 1)
        self.assertIsNone(error)

    def test_logical_operations(self):
        # And
        num1 = Number(1)
        num2 = Number(0)
        result, error = num1.anded_by(num2)
        self.assertEqual(result.value, 0)
        self.assertIsNone(error)

        # Or
        result, error = num1.ored_by(num2)
        self.assertEqual(result.value, 1)
        self.assertIsNone(error)

        # Not
        result, error = num2.notted()
        self.assertEqual(result.value, 1)
        self.assertIsNone(error)

    def test_copy(self):
        num1 = Number(5)
        copy = num1.copy()
        self.assertEqual(copy.value, num1.value)
        self.assertIsNot(copy, num1)  # Check if a new instance is created

    def test_is_true(self):
        num1 = Number(0)
        self.assertFalse(num1.is_true())

        num2 = Number(5)
        self.assertTrue(num2.is_true())


if __name__ == "__main__":
    unittest.main()
