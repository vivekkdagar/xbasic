import unittest
from xbasic.error_handler.rterror import RTError
from xbasic.utils.position import Position
from xbasic.context_handler.context import Context


class TestRTError(unittest.TestCase):
    def test_generate_traceback(self):
        # Create positions
        pos1 = Position('file1', 1, 0, 'code1')
        pos2 = Position('file2', 3, 0, 'code2')

        # Create context
        ctx1 = Context('Function1', pos1)
        ctx2 = Context('Function2', pos2, ctx1)

        # Create RTError
        rt_error = RTError(pos2, pos1, 'Error details', ctx2)

        # Generate traceback
        expected_traceback = (
            "Traceback (most recent call last):\n"
            f"  File file2, line 4, in Function2\n"
            f"  File file1, line 2, in Function1\n"
        )

        self.assertEqual(rt_error.generate_traceback(), expected_traceback)

    def test_as_string(self):
        # Create positions
        pos_start = Position('file1', 1, 0, 'code1')
        pos_end = Position('file1', 1, 5, 'code1')

        # Create context
        ctx = Context('Function1', pos_start)

        # Create RTError
        rt_error = RTError(pos_start, pos_end, 'Error details', ctx)

        # Create expected error string
        expected_error_string = (
            "Traceback (most recent call last):\n"
            f"  File file1, line 2, in Function1\n"
            "Runtime Error: Error details\n\n"
            "code1\n"
            "^^^^^\n"
        )

        self.assertEqual(rt_error.as_string(), expected_error_string)


if __name__ == '__main__':
    unittest.main()
