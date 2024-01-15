#!/usr/bin/python3
"""Module to represent Base object to be extended by Square and Rectangle"""

import json
import csv

class Base:
    """Base class to be subclassed by Square and Rectangle"""

    __nb_object = 0
    """Class variable representing the total count of Base (and subclass)
    instances.
    """

    def __init__(self, id=None):
        """Initialize new Base instance

        Args:
            id: Identifier for instance. If None, use current object count.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Arguments:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles onto the screen using Tkinter and the
        Turtle drawing library.

        Args:
            list_rectangles (list): list of Rectangle instances
        """
        try:
            import turtle
            import random
        except ImportError("Turtle drawing library not available") as e:
            print("[{}]: {}".format(e.__class__.__name__, e))
            for r in list_rectangles:
                print(r, ':')
                r.display()
            print()
            for s in list_squares:
                print(s, ':')
                s.display()
        else:
            max_width = max(max(map(lambda r: r.width, list_rectangles)),
                            max(map(lambda s: s.size, list_squares)))
            max_width_off = max(max(map(lambda r: r.x, list_rectangles)),
                                max(map(lambda s: s.x, list_squares)))
            max_max_width = max_width + max_width_off
            max_height = max(max(map(lambda r: r.height, list_rectangles)),
                             max(map(lambda s: s.size, list_squares)))
            max_height_off = max(max(map(lambda r: r.y, list_rectangles)),
                                 max(map(lambda s: s.y, list_squares)))
            max_max_height = max_height + max_height_off
            max_max_max = max(max_max_width,
                              max_max_height)
            max_len = max(len(list_rectangles), len(list_squares))
            win = turtle.Screen()
            aspect_ratio = 3*max_max_height/(max_max_width*(max_len+1))
            print(aspect_ratio)
            win.setup(width=800, height=int(800*aspect_ratio))
            win.setworldcoordinates(0,
                                    3*max_max_height,
                                    max_max_width*(max_len+1),
                                    0)
            turt = turtle.Turtle()
            turt.hideturtle()
            turt.penup()
            turt.pensize(3)
            turt.color('green', 'blue')
            turt.goto(0, max_max_height/3)
            for i, rect in enumerate(list_rectangles):
                turt.setx(i*max_max_width + (i+1)*max_max_width/(max_len + 1))
                turt.pendown()
                turt.write(rect.__str__())
                turt.dot()
                off_heading = turt.towards(turt.xcor() + rect.x,
                                           turt.ycor() + rect.y)
                curr_heading = turt.heading()
                turt.setheading(off_heading)
                turt.goto(turt.xcor() + rect.x, turt.ycor() + rect.y)
                turt.setheading(curr_heading)
                turt.begin_fill()
                for _ in range(2):
                    turt.forward(rect.width)
                    turt.right(-90)
                    turt.forward(rect.height)
                    turt.right(-90)
                turt.end_fill()
                turt.penup()

            turt.goto(0, 5*max_max_height/3)
            turt.color('orange', 'purple')
            for j, square in enumerate(list_squares):
                turt.setx(j*max_max_width + (j+1)*max_max_width/(max_len + 1))
                turt.pendown()
                turt.write(square.__str__())
                turt.dot()
                off_heading = turt.towards(turt.xcor() + square.x,
                                           turt.ycor() + square.y)
                curr_heading = turt.heading()
                turt.setheading(off_heading)
                turt.goto(turt.xcor() + square.x, turt.ycor() + square.y)
                turt.setheading(curr_heading)
                turt.begin_fill()
                for _ in range(4):
                    turt.forward(square.size)
                    turt.right(-90)
                turt.end_fill()
                turt.penup()
            win.exitonclick()
