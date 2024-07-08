import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self) -> None:
        node = Textnode("This is a text node", "bold")
        node2 = Textnode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self) -> None:
        node = Textnode("This is a text node", "bold")
        node2 = Textnode("This is a text node", "normal")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
