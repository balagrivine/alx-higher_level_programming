#!/usr/bin/python3
"""class base"""
import json
import os


class Base:
    """the base class of all other classes of the project"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """gets json string rep of list dictionaries

        Args:
            list_dictionaries: list of dictionaries

        Return:
            json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string rep of list_objs to a file
        
        Args:
            list_objs: list of instances who inherits from base

        Return: nothing
        """

        if list_objs is None or len(list_objs) == 0:
            list_objs = []
        file_name = cls.__name__ + ".json"
        fc = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(fc)

    @staticmethod
    def from_json_string(json_string):
        """returns list of the JSON string representation

        Args:
            json_string: string representing a list of dictionaries

        Return:
            python list object
        """

        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that gets  a list of instances

        Returns:
            instance: returns a list of instances
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_data = file.read()

        instance_dicts = cls.from_json_string(json_data)
        instances = [cls.create(**data) for data in instance_dicts]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Base class method that that serializes and deserializes in CSV

        Args:
            list_objs (list ): list objects
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                instance = cls.create_from_csv_row(row)
                instances.append(instance)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Base class method that displays the Rectangle
        and Square classes in GUI

        Args:
            list_rectangles (list): list containing Rectangle instances
            list_squares (list): list containing Square instances
        """
        window = turtle.Screen()
        window.bgcolor("white")
        pen = turtle.Turtle()
        pen.speed(1)

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("red")
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.right(90)
                pen.forward(rectangle.height)
                pen.right(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("blue")
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)

        turtle.done()
