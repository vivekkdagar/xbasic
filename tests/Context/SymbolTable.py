import unittest
from xbasic.context_handler.symbol_table import SymbolTable


class TestSymbolTable(unittest.TestCase):
    def test_set_and_get(self):
        # Test setting and getting symbols
        symbol_table = SymbolTable()
        symbol_table.set('x', 10)
        self.assertEqual(symbol_table.get('x'), 10)

        # Test setting and getting multiple symbols
        symbol_table.set('y', 20)
        symbol_table.set('z', 30)
        self.assertEqual(symbol_table.get('y'), 20)
        self.assertEqual(symbol_table.get('z'), 30)

    def test_parent_scope(self):
        # Test parent scope lookup
        parent_table = SymbolTable()
        parent_table.set('x', 10)

        child_table = SymbolTable(parent=parent_table)
        self.assertEqual(child_table.get('x'), 10)

        # Test child scope shadows parent scope
        child_table.set('x', 20)
        self.assertEqual(child_table.get('x'), 20)

        # Test accessing parent scope after shadowing
        self.assertEqual(child_table.parent.get('x'), 10)

    def test_remove(self):
        # Test removing symbols
        symbol_table = SymbolTable()
        symbol_table.set('x', 10)
        symbol_table.set('y', 20)

        symbol_table.remove('x')
        self.assertIsNone(symbol_table.get('x'))
        self.assertEqual(symbol_table.get('y'), 20)

        # Test removing symbols from parent scope
        parent_table = SymbolTable()
        parent_table.set('x', 10)

        child_table = SymbolTable(parent=parent_table)
        child_table.remove('x')
        self.assertIsNone(child_table.get('x'))
        self.assertEqual(parent_table.get('x'), 10)

    def test_nested_scopes(self):
        # Test nested scopes
        grandparent_table = SymbolTable()
        grandparent_table.set('x', 10)

        parent_table = SymbolTable(parent=grandparent_table)
        parent_table.set('y', 20)

        child_table = SymbolTable(parent=parent_table)
        child_table.set('z', 30)

        # Test accessing symbols from all scopes
        self.assertEqual(child_table.get('x'), 10)
        self.assertEqual(child_table.get('y'), 20)
        self.assertEqual(child_table.get('z'), 30)


if __name__ == '__main__':
    unittest.main()
