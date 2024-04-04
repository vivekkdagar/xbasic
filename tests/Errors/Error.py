import unittest
from xbasic.error_handler.error import (Error,
                                        IllegalCharError,
                                        ExpectedCharError,
                                        InvalidSyntaxError)
from xbasic.utils.position import Position


class TestErrorClasses(unittest.TestCase):
    def test_Error_as_string(self):
        # Test Error class
        pos_start = Position(1, 0, 0, 'file.txt', 'Some text')
        pos_end = Position(1, 5, 0, 'file.txt', 'Some text')
        error = Error(pos_start, pos_end, 'Error Name', 'Error details')
        expected_output = ("Error Name: Error details\n"
                           "File file.txt, line 1\n\n"
                           "Some text\n     ^^^^^")
        self.assertEqual(error.as_string(), expected_output)

    def test_IllegalCharError(self):
        # Test IllegalCharError subclass
        pos_start = Position(1, 0, 0, 'file.txt', 'Some text')
        pos_end = Position(1, 5, 0, 'file.txt', 'Some text')
        error = IllegalCharError(pos_start, pos_end, 'Illegal character: %')
        expected_output = ("Illegal Character: Illegal character:"
                           "%\nFile file.txt, line 1\n\nSome text\n    "
                           " ^^^^^")
        self.assertEqual(error.as_string(), expected_output)

    def test_ExpectedCharError(self):
        # Test ExpectedCharError subclass
        pos_start = Position(1, 0, 0, 'file.txt', 'Some text')
        pos_end = Position(1, 5, 0, 'file.txt', 'Some text')
        error = ExpectedCharError(pos_start, pos_end, 'Expected character: =')
        expected_output = ("Expected Character:"
                           "Expected character: =\nFile file.txt,"
                           "line 1\n\nSome text\n     ^^^^^")
        self.assertEqual(error.as_string(), expected_output)

    def test_InvalidSyntaxError(self):
        # Test InvalidSyntaxError subclass
        pos_start = Position(1, 0, 0, 'file.txt', 'Some text')
        pos_end = Position(1, 5, 0, 'file.txt', 'Some text')
        error = InvalidSyntaxError(pos_start, pos_end, 'Invalid syntax')
        expected_output = ("Invalid Syntax: Invalid syntax\n"
                           "File file.txt, line 1\n\n"
                           "Some text\n     ^^^^^")
        self.assertEqual(error.as_string(), expected_output)


if __name__ == '__main__':
    unittest.main()
