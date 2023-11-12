import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
"""cleating a unittest for the Base class
"""


class BaseTestCases(unittest.TestCase):
    """class hat inherits from the python unittest class

    Args:
        unittest.TestCase (class): unittest TestCase class
    """

    def test_base_id(self):
        """testing the base id attribute
        """
        self.assertEqual(Base(1).id, 1)
        self.assertEqual(Base(12).id, 12)

    def test_from_file_to_instances(self):
        """testing the base class on converting json
        data to an instance
        """
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()


if __name__ == "__main__":
    unittest.main()
