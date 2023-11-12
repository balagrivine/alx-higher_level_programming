import unittest
from io import StringIO
import contextlib
from models.rectangle import Rectangle
from models.base import Base
"""cleating a unittest for the Rectangle class
"""


class RectangleTestCases(unittest.TestCase):
    """class hat inherits from the python unittest class

    Args:
        unittest.TestCase (class): unittest TestCase class
    """

    def test_rectangle_inheritance(self):
        r4 = Rectangle(1, 2, 3, 4, 10)
        with self.assertRaises(TypeError) as context:
            r0 = Rectangle(1)
            self.assertTrue('__init__() missing 1 required positional\
                argument' in context.exception)
        self.assertEqual(r4.id, 10)

    def test_validate_rectangle_int_type_error(self):
        """test for rectangle class attribute validation
        """

        with self.assertRaises(TypeError) as context:
            r0 = Rectangle("1")
            self.assertTrue('width must be an integer' in context.exception)
        with self.assertRaises(TypeError) as context:
            r0 = Rectangle(2, "1")
            self.assertTrue('height must be an integer' in context.exception)
        with self.assertRaises(TypeError) as context:
            r0 = Rectangle(1, 2, "1")
            self.assertTrue('x must be an integer' in context.exception)
        with self.assertRaises(TypeError) as context:
            r0 = Rectangle(1, 2, 3, "1")
            self.assertTrue('y must be an integer' in context.exception)

    def test_validate_rectangle_int_value_error(self):
        """test for rectangle class attribute validation
        """

        with self.assertRaises(ValueError) as context:
            r0 = Rectangle(0, 1)
            self.assertTrue('width must be > 0' in context.exception)
        with self.assertRaises(ValueError) as context:
            r0 = Rectangle(1, 0)
            self.assertTrue('height must be > 0' in context.exception)
        with self.assertRaises(ValueError) as context:
            r0 = Rectangle(1, 2, -2)
            self.assertTrue('x must be >= 0' in context.exception)
        with self.assertRaises(ValueError) as context:
            r0 = Rectangle(1, 3, 3, -2000)
            self.assertTrue('y must be >= 0' in context.exception)

    def test_rectangle_area(self):
        """testing rectangle class area method
        """

        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_rectangle_display(self):
        """testing rectangle class display method
        """

        r = Rectangle(3, 2)

        expected_output = "###\n###"

        with StringIO() as buffer, contextlib.redirect_stdout(buffer):
            r.display()
            output = buffer.getvalue().strip()

        self.assertMultiLineEqual(expected_output, output)

    def test_rectangle_str(self):
        """testing rectangle class __str__ method
        """

        r7 = Rectangle(3, 2, 4, 5, 12)
        self.assertEqual(str(r7), "[Rectangle] (12) 4/5 - 3/2")
        r7 = Rectangle(3, 2, 0, 0, 12)
        self.assertEqual(str(r7), "[Rectangle] (12) 0/0 - 3/2")

    def test_rectangle_display_x_y(self):
        """testing rectangle class display method
        """

        r8 = Rectangle(3, 2, 0, 0, 23)
        expected_output = "###\n###"
        with StringIO() as buffer, contextlib.redirect_stdout(buffer):
            r8.display()
            output = buffer.getvalue().strip()
        self.assertMultiLineEqual(expected_output, output)

        r9 = Rectangle(2, 3, 2, 2, 20)
        expected_output = "##\n  ##\n  ##"
        with StringIO() as buffer, contextlib.redirect_stdout(buffer):
            r9.display()
            output = buffer.getvalue().strip()
        self.assertMultiLineEqual(expected_output, output)

    def test_rectangle_update_args(self):
        """testing rectangle class update method for the
        *args parameter
        """

        r7 = Rectangle(3, 2, 0, 0, 12)
        r7.update(12, 13, 34, 56, 107)
        self.assertEqual(str(r7), "[Rectangle] (12) 56/107 - 13/34")

        r7.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r7), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_update_kwargs(self):
        """testing rectangle class update method fro the
        **kwargs argument
        """

        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")
        r1.update(height=1, id=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_rectangle_dictionary(self):
        """testing rectangle class to_dictionary method
        """

        st1 = "{'id': 6, 'width': 10, 'height': 2, 'x': 1, 'y': 9}"
        r11 = Rectangle(10, 2, 1, 9, 6)
        r1_dictionary = r11.to_dictionary()
        self.assertEqual(str(r1_dictionary), st1)

    def test_dictionary_to_json(self):
        """testing rectangle class to_json method
        """

        st1 = '[{"id": 4, "width": 10, "height": 7, "x": 2, "y": 8}]'
        r15 = Rectangle(10, 7, 2, 8, 4)
        dictionary = r15.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(json_dictionary), st1)

    def test_write_json_to_file(self):
        """testing rectangle class writing to a json file
        """

        r16 = Rectangle(10, 7, 2, 8)
        r17 = Rectangle(2, 4)
        Rectangle.save_to_file([r16, r17])

    def test_json_to_dictionary(self):
        """testing rectangle class on converting json
        data to python dictionary
        """

        st1 = "[{'id': 89, 'width': 10, 'height': 4},"
        st2 = " {'id': 7, 'width': 1, 'height': 7}]"
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(str(list_output), st1 + st2)

    def test_dictionary_to_instance(self):
        """testing rectangle class in converting
        json fle data to python instance
        """

        r18 = Rectangle(3, 5, 1, 2, 2)
        r1_dictionary = r18.to_dictionary()
        r19 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r19), "[Rectangle] (2) 1/2 - 3/5")


if __name__ == "__main__":
    unittest.main()
