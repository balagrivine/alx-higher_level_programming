import unittest
from models.square import Square
from io import StringIO
import contextlib
import os
"""cleating a unittest for the Square class
"""


class SquareTestCases(unittest.TestCase):
    """class hat inherits from the python unittest class

    Args:
        unittest.TestCase (class): unittest TestCase class
    """

    def test_square(self):
        """testing Square class attributes
        """

        s1 = Square(3, 1, 3, 17)
        self.assertEqual(str(s1), "[Square] (17) 1/3 - 3")
        self.assertEqual(str(s1.area()), "9")
        s1.display()
        expected_output = "###\n ###\n ###"
        with StringIO() as buffer, contextlib.redirect_stdout(buffer):
            s1.display()
            output = buffer.getvalue().strip()
        self.assertMultiLineEqual(expected_output, output)

    def test_square_size(self):
        """testing Square class size attribute
        """

        s1 = Square(1, 2, 3, 4)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 10")

        with self.assertRaises(TypeError) as context:
            s1.size = "10"
            self.assertTrue('width must be an integer' in context.exception)

    def test_square_update_args_kwargs(self):
        """testing Square class update method
        """

        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(11)
        self.assertEqual(str(s1), "[Square] (11) 0/0 - 5")

        s1.update(size=7, id=89, x=12, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_square_dictionary(self):
        """testing Square class on converting to dictionary
        """

        st1 = '[{"id": 13, "width": 10, "height": 7, "x": 2, "y": 8},'
        st2 = ' {"id": 14, "width": 2, "height": 4, "x": 0, "y": 0}]'
        st3 = "{'id': 18, 'size': 10, 'x': 2, 'y': 1}"
        s1 = Square(10, 2, 1, 18)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(str(s1_dictionary), st3)

        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            ac = file.read()
        ec = st1 + st2
        self.assertEqual(ac, ec)


if __name__ == "__main__":
    unittest.main()
