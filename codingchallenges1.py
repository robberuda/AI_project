# the code is written by Coding Challenges: http://bit.do/e6c6X
from vpython import *  # for 3D animations and cube
import random  # for randomizing the cube
import time  # for mesuring the solve time and slowing down the cube


def make_small_cube(colorsidefront, colorsideleft, colorsideright, colorsidedown, colorsideup, colorsideback):
    colorsidefront = colorsidefront
    colorsideleft = colorsideleft
    colorsideright = colorsideright
    colorsidedown = colorsidedown
    colorsideup = colorsideup
    colorsideback = colorsideback

    # to color each side of a box i used 6 piramides with different colors
    container = box(pos=vector(0.5, 0, 0), size=vector(0.99, 0.999, 0.99), color=vector(0.5, 0.5, 0.5))
    blue = pyramid(pos=vector(0, 0, 0), size=vector(0.9, 0.9, 0.9), color=colorsideleft)
    side2 = pyramid(pos=vector(1, 0, 0), size=vector(0.9, 0.9, 0.9), axis=vector(-1, 0, 0), color=colorsideright)
    green = pyramid(pos=vector(0.5, -0.5, 0), size=vector(0.9, 0.9, 0.9), axis=vector(0, 1, 0), color=colorsidedown)
    orange = pyramid(pos=vector(0.5, 0.5, 0), size=vector(0.9, 0.9, 0.9), axis=vector(0, -1, 0), color=colorsideup)
    white = pyramid(pos=vector(0.5, 0, -0.5), size=vector(0.9, 0.9, 0.9), axis=vector(0, 0, 1), color=colorsideback)
    yellow = pyramid(pos=vector(0.5, 0, 0.5), size=vector(0.9, 0.9, 0.9), axis=vector(0, 0, -1), color=colorsidefront)
    return compound([container, blue, side2, green, orange, white, yellow])


# with function i made all posible small cubes in a rubiix
cube1 = make_small_cube(color.blue, color.red, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.white,
                        vector(0.5, 0.5, 0.5))
cube2 = make_small_cube(color.blue, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.white,
                        vector(0.5, 0.5, 0.5))
cube3 = make_small_cube(color.blue, vector(0.5, 0.5, 0.5), color.orange, vector(0.5, 0.5, 0.5), color.white,
                        vector(0.5, 0.5, 0.5))
cube4 = make_small_cube(color.blue, color.red, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5),
                        vector(0.5, 0.5, 0.5))
cube5 = make_small_cube(color.blue, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5),
                        vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5))
cube6 = make_small_cube(color.blue, vector(0.5, 0.5, 0.5), color.orange, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5),
                        vector(0.5, 0.5, 0.5))
cube7 = make_small_cube(color.blue, color.red, vector(0.5, 0.5, 0.5), color.yellow, vector(0.5, 0.5, 0.5),
                        vector(0.5, 0.5, 0.5))
cube8 = make_small_cube(color.blue, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.yellow, vector(0.5, 0.5, 0.5),
                        vector(0.5, 0.5, 0.5))
cube9 = make_small_cube(color.blue, vector(0.5, 0.5, 0.5), color.orange, color.yellow, vector(0.5, 0.5, 0.5),
                        vector(0.5, 0.5, 0.5))
cube10 = make_small_cube(vector(0.5, 0.5, 0.5), color.red, vector(0.5, 0.5, 0.5), color.yellow, vector(0.5, 0.5, 0.5),
                         vector(0.5, 0.5, 0.5))
cube11 = make_small_cube(vector(0.5, 0.5, 0.5), color.red, vector(0.5, 0.5, 0.5), color.yellow, vector(0.5, 0.5, 0.5),
                         color.green)
cube12 = make_small_cube(vector(0.5, 0.5, 0.5), color.red, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5),
                         vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5))
cube13 = make_small_cube(vector(0.5, 0.5, 0.5), color.red, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5),
                         vector(0.5, 0.5, 0.5), color.green)
cube14 = make_small_cube(vector(0.5, 0.5, 0.5), color.red, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.white,
                         vector(0.5, 0.5, 0.5))
cube15 = make_small_cube(vector(0.5, 0.5, 0.5), color.red, vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.white,
                         color.green)
cube16 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.orange, color.yellow,
                         vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5))
cube17 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.orange, color.yellow,
                         vector(0.5, 0.5, 0.5), color.green)
cube18 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.orange, vector(0.5, 0.5, 0.5),
                         vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5))
cube19 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.orange, vector(0.5, 0.5, 0.5),
                         vector(0.5, 0.5, 0.5), color.green)
cube20 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.orange, vector(0.5, 0.5, 0.5), color.white,
                         vector(0.5, 0.5, 0.5))
cube21 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.orange, vector(0.5, 0.5, 0.5), color.white,
                         color.green)
cube22 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5),
                         color.white, vector(0.5, 0.5, 0.5))
cube23 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5),
                         color.white, color.green)
cube24 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.yellow,
                         vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5))
cube25 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), color.yellow,
                         vector(0.5, 0.5, 0.5), color.green)
cube26 = make_small_cube(vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5), vector(0.5, 0.5, 0.5),
                         vector(0.5, 0.5, 0.5), color.green)


# Here I defined classes for different types of small cubes. corners, edges, each one has coordinates and functions that changes coordinates acording to movments
class corner_cube:
    def __init__(self, position, correct_position, name, orientation1, correct_orientation1, orientation2,
                 correct_orientation2, orientation3, correct_orientation3):
        self.position = position
        self.correct_position = correct_position
        self.name = name
        self.orientation1 = orientation1
        self.correct_orientation1 = correct_orientation1
        self.orientation2 = orientation2
        self.correct_orientation2 = correct_orientation2
        self.orientation3 = orientation3
        self.correct_orientation3 = correct_orientation3

    def front_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, -1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, -1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 1, 0)

            if self.orientation3 == vector(0, 1, 0):
                self.orientation3 = vector(1, 0, 0)
            elif self.orientation3 == vector(1, 0, 0):
                self.orientation3 = vector(0, -1, 0)
            elif self.orientation3 == vector(0, -1, 0):
                self.orientation3 = vector(-1, 0, 0)
            elif self.orientation3 == vector(-1, 0, 0):
                self.orientation3 = vector(0, 1, 0)

        if self.position == vector(0, 2, 0):
            self.position = vector(2, 2, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, 0):
            self.position = vector(2, 0, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, 0):
            self.position = vector(0, 0, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 0, 0):
            self.position = vector(0, 2, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def front_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, -1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, -1, 0)

            if self.orientation3 == vector(0, 1, 0):
                self.orientation3 = vector(-1, 0, 0)
            elif self.orientation3 == vector(1, 0, 0):
                self.orientation3 = vector(0, 1, 0)
            elif self.orientation3 == vector(0, -1, 0):
                self.orientation3 = vector(1, 0, 0)
            elif self.orientation3 == vector(-1, 0, 0):
                self.orientation3 = vector(0, -1, 0)

        if self.position == vector(0, 2, 0):
            self.position = vector(0, 0, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, 0):
            self.position = vector(0, 2, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, 0):
            self.position = vector(2, 2, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 0, 0):
            self.position = vector(2, 0, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def right_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(0, -1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(0, 1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(0, -1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(0, 1, 0)

            if self.orientation3 == vector(0, 1, 0):
                self.orientation3 = vector(0, 0, -1)
            elif self.orientation3 == vector(0, 0, -1):
                self.orientation3 = vector(0, -1, 0)
            elif self.orientation3 == vector(0, -1, 0):
                self.orientation3 = vector(0, 0, 1)
            elif self.orientation3 == vector(0, 0, 1):
                self.orientation3 = vector(0, 1, 0)

        if self.position == vector(2, 0, 0):
            self.position = vector(2, 2, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, 0):
            self.position = vector(2, 2, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, -2):
            self.position = vector(2, 0, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, -2):
            self.position = vector(2, 0, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def right_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(0, 1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(0, -1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(0, 1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(0, -1, 0)

            if self.orientation3 == vector(0, 1, 0):
                self.orientation3 = vector(0, 0, 1)
            elif self.orientation3 == vector(0, 0, -1):
                self.orientation3 = vector(0, 1, 0)
            elif self.orientation3 == vector(0, -1, 0):
                self.orientation3 = vector(0, 0, -1)
            elif self.orientation3 == vector(0, 0, 1):
                self.orientation3 = vector(0, -1, 0)

        if self.position == vector(2, 0, 0):
            self.position = vector(2, 0, -2)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, 0):
            self.position = vector(2, 0, 0)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, -2):
            self.position = vector(2, 2, 0)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, -2):
            self.position = vector(2, 2, -2)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def left_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(0, -1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(0, 1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(0, -1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(0, 1, 0)

            if self.orientation3 == vector(0, 1, 0):
                self.orientation3 = vector(0, 0, -1)
            elif self.orientation3 == vector(0, 0, -1):
                self.orientation3 = vector(0, -1, 0)
            elif self.orientation3 == vector(0, -1, 0):
                self.orientation3 = vector(0, 0, 1)
            elif self.orientation3 == vector(0, 0, 1):
                self.orientation3 = vector(0, 1, 0)

        if self.position == vector(0, 0, 0):
            self.position = vector(0, 2, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, 0):
            self.position = vector(0, 2, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, -2):
            self.position = vector(0, 0, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 0, -2):
            self.position = vector(0, 0, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def left_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(0, 1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(0, -1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(0, 1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(0, -1, 0)

            if self.orientation3 == vector(0, 1, 0):
                self.orientation3 = vector(0, 0, 1)
            elif self.orientation3 == vector(0, 0, -1):
                self.orientation3 = vector(0, 1, 0)
            elif self.orientation3 == vector(0, -1, 0):
                self.orientation3 = vector(0, 0, -1)
            elif self.orientation3 == vector(0, 0, 1):
                self.orientation3 = vector(0, -1, 0)

        if self.position == vector(0, 0, 0):
            self.position = vector(0, 0, -2)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, 0):
            self.position = vector(0, 0, 0)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, -2):
            self.position = vector(0, 2, 0)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 0, -2):
            self.position = vector(0, 2, -2)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def top_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 0, 1)

            if self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 0, 1)

            if self.orientation3 == vector(0, 0, 1):
                self.orientation3 = vector(-1, 0, 0)
            elif self.orientation3 == vector(-1, 0, 0):
                self.orientation3 = vector(0, 0, -1)
            elif self.orientation3 == vector(0, 0, -1):
                self.orientation3 = vector(1, 0, 0)
            elif self.orientation3 == vector(1, 0, 0):
                self.orientation3 = vector(0, 0, 1)

        if self.position == vector(2, 2, 0):
            self.position = vector(0, 2, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, 0):
            self.position = vector(0, 2, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, -2):
            self.position = vector(2, 2, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, -2):
            self.position = vector(2, 2, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def top_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 0, -1)

            if self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 0, -1)

            if self.orientation3 == vector(0, 0, 1):
                self.orientation3 = vector(1, 0, 0)
            elif self.orientation3 == vector(-1, 0, 0):
                self.orientation3 = vector(0, 0, 1)
            elif self.orientation3 == vector(0, 0, -1):
                self.orientation3 = vector(-1, 0, 0)
            elif self.orientation3 == vector(1, 0, 0):
                self.orientation3 = vector(0, 0, -1)

        if self.position == vector(2, 2, 0):
            self.position = vector(2, 2, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, 0):
            self.position = vector(2, 2, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, -2):
            self.position = vector(0, 2, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, -2):
            self.position = vector(0, 2, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def down_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 0, 1)

            if self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 0, 1)

            if self.orientation3 == vector(0, 0, 1):
                self.orientation3 = vector(-1, 0, 0)
            elif self.orientation3 == vector(-1, 0, 0):
                self.orientation3 = vector(0, 0, -1)
            elif self.orientation3 == vector(0, 0, -1):
                self.orientation3 = vector(1, 0, 0)
            elif self.orientation3 == vector(1, 0, 0):
                self.orientation3 = vector(0, 0, 1)

        if self.position == vector(0, 0, 0):
            self.position = vector(0, 0, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 0, -2):
            self.position = vector(2, 0, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, -2):
            self.position = vector(2, 0, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, 0):
            self.position = vector(0, 0, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def down_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 0, -1)

            if self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 0, -1)

            if self.orientation3 == vector(0, 0, 1):
                self.orientation3 = vector(1, 0, 0)
            elif self.orientation3 == vector(-1, 0, 0):
                self.orientation3 = vector(0, 0, 1)
            elif self.orientation3 == vector(0, 0, -1):
                self.orientation3 = vector(-1, 0, 0)
            elif self.orientation3 == vector(1, 0, 0):
                self.orientation3 = vector(0, 0, -1)

        if self.position == vector(0, 0, 0):
            self.position = vector(2, 0, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 0, -2):
            self.position = vector(0, 0, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, -2):
            self.position = vector(0, 0, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, 0):
            self.position = vector(2, 0, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def back_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, -1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, -1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 1, 0)

            if self.orientation3 == vector(0, 1, 0):
                self.orientation3 = vector(1, 0, 0)
            elif self.orientation3 == vector(1, 0, 0):
                self.orientation3 = vector(0, -1, 0)
            elif self.orientation3 == vector(0, -1, 0):
                self.orientation3 = vector(-1, 0, 0)
            elif self.orientation3 == vector(-1, 0, 0):
                self.orientation3 = vector(0, 1, 0)

        if self.position == vector(0, 0, -2):
            self.position = vector(0, 2, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, -2):
            self.position = vector(2, 2, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, -2):
            self.position = vector(2, 0, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, -2):
            self.position = vector(0, 0, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def back_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, -1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, -1, 0)

            if self.orientation3 == vector(0, 1, 0):
                self.orientation3 = vector(-1, 0, 0)
            elif self.orientation3 == vector(1, 0, 0):
                self.orientation3 = vector(0, 1, 0)
            elif self.orientation3 == vector(0, -1, 0):
                self.orientation3 = vector(1, 0, 0)
            elif self.orientation3 == vector(-1, 0, 0):
                self.orientation3 = vector(0, -1, 0)

        if self.position == vector(0, 0, -2):
            self.position = vector(2, 0, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(0, 2, -2):
            self.position = vector(0, 0, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 2, -2):
            self.position = vector(0, 2, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

        elif self.position == vector(2, 0, -2):
            self.position = vector(2, 2, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)


class edge_cube:
    def __init__(self, position, correct_position, name, orientation1, correct_orientation1, orientation2,
                 correct_orientation2):
        self.position = position
        self.correct_position = correct_position
        self.name = name
        self.orientation1 = orientation1
        self.correct_orientation1 = correct_orientation1
        self.orientation2 = orientation2
        self.correct_orientation2 = correct_orientation2

    def front_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, -1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, -1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 1, 0)

        if self.position == vector(1, 0, 0):
            self.position = vector(0, 1, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 1, 0):
            self.position = vector(1, 2, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1, 2, 0):
            self.position = vector(2, 1, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 1, 0):
            self.position = vector(1, 0, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def front_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, -1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, -1, 0)

        if self.position == vector(1, 0, 0):
            self.position = vector(2, 1, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 1, 0):
            self.position = vector(1, 0, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1, 2, 0):
            self.position = vector(0, 1, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 1, 0):
            self.position = vector(1, 2, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def right_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(0, -1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(0, 1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(0, -1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(0, 1, 0)

        if self.position == vector(2, 1, 0):
            self.position = vector(2, 2, -1)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 2, -1):
            self.position = vector(2, 1, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 1, -2):
            self.position = vector(2, 0, -1)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 0, -1):
            self.position = vector(2, 1, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def right_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(0, 1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(0, -1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(0, 1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(0, -1, 0)

        if self.position == vector(2, 1, 0):
            self.position = vector(2, 0, -1)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 2, -1):
            self.position = vector(2, 1, 0)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 1, -2):
            self.position = vector(2, 2, -1)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 0, -1):
            self.position = vector(2, 1, -2)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def left_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(0, -1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(0, 1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(0, -1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(0, 1, 0)

        if self.position == vector(0, 1, 0):
            self.position = vector(0, 2, -1)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 2, -1):
            self.position = vector(0, 1, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 1, -2):
            self.position = vector(0, 0, -1)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 0, -1):
            self.position = vector(0, 1, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def left_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(0, 1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(0, -1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(0, 1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(0, -1, 0)

        if self.position == vector(0, 1, 0):
            self.position = vector(0, 0, -1)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 2, -1):
            self.position = vector(0, 1, 0)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 1, -2):
            self.position = vector(0, 2, -1)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 0, -1):
            self.position = vector(0, 1, -2)
            self.name.rotate(angle=1.57079633, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def top_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 0, 1)

            if self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 0, 1)

        if self.position == vector(1, 2, 0):
            self.position = vector(0, 2, -1)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 2, -1):
            self.position = vector(1, 2, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1, 2, -2):
            self.position = vector(2, 2, -1)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 2, -1):
            self.position = vector(1, 2, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def top_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 0, -1)

            if self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 0, -1)

        if self.position == vector(1, 2, 0):
            self.position = vector(2, 2, -1)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 2, -1):
            self.position = vector(1, 2, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1, 2, -2):
            self.position = vector(0, 2, -1)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 2, -1):
            self.position = vector(1, 2, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def down_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 0, -1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 0, 1)

            if self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 0, -1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 0, 1)

        if self.position == vector(1, 0, 0):
            self.position = vector(0, 0, -1)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 0, -1):
            self.position = vector(1, 0, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1, 0, -2):
            self.position = vector(2, 0, -1)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 0, -1):
            self.position = vector(1, 0, 0)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def down_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 0, 1):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 0, 1)
            elif self.orientation1 == vector(0, 0, -1):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 0, -1)

            if self.orientation2 == vector(0, 0, 1):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 0, 1)
            elif self.orientation2 == vector(0, 0, -1):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 0, -1)

        if self.position == vector(1, 0, 0):
            self.position = vector(2, 0, -1)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 0, -1):
            self.position = vector(1, 0, 0)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1, 0, -2):
            self.position = vector(0, 0, -1)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 0, -1):
            self.position = vector(1, 0, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def back_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, -1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, 1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, -1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, 1, 0)

        if self.position == vector(1, 0, -2):
            self.position = vector(0, 1, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 1, -2):
            self.position = vector(1, 2, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1, 2, -2):
            self.position = vector(2, 1, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 1, -2):
            self.position = vector(1, 0, -2)
            self.name.rotate(angle=-1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)

    def back_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0, 1, 0):
                self.orientation1 = vector(-1, 0, 0)
            elif self.orientation1 == vector(1, 0, 0):
                self.orientation1 = vector(0, 1, 0)
            elif self.orientation1 == vector(0, -1, 0):
                self.orientation1 = vector(1, 0, 0)
            elif self.orientation1 == vector(-1, 0, 0):
                self.orientation1 = vector(0, -1, 0)

            if self.orientation2 == vector(0, 1, 0):
                self.orientation2 = vector(-1, 0, 0)
            elif self.orientation2 == vector(1, 0, 0):
                self.orientation2 = vector(0, 1, 0)
            elif self.orientation2 == vector(0, -1, 0):
                self.orientation2 = vector(1, 0, 0)
            elif self.orientation2 == vector(-1, 0, 0):
                self.orientation2 = vector(0, -1, 0)

        if self.position == vector(1, 0, -2):
            self.position = vector(2, 1, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0, 1, -2):
            self.position = vector(1, 0, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1, 2, -2):
            self.position = vector(0, 1, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2, 1, -2):
            self.position = vector(1, 2, -2)
            self.name.rotate(angle=1.57079633, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.name.pos = self.position
            orientation_changer(self)


# all positions of the cubes in vectors(x,y,z)
v1 = vector(0, 2, 0)
v2 = vector(1, 2, 0)
v3 = vector(2, 2, 0)
v4 = vector(0, 1, 0)
v5 = vector(1, 1, 0)
v6 = vector(2, 1, 0)
v7 = vector(0, 0, 0)
v8 = vector(1, 0, 0)
v9 = vector(2, 0, 0)
v10 = vector(0, 0, -1)
v11 = vector(0, 0, -2)
v12 = vector(0, 1, -1)
v13 = vector(0, 1, -2)
v14 = vector(0, 2, -1)
v15 = vector(0, 2, -2)
v16 = vector(2, 0, -1)
v17 = vector(2, 0, -2)
v18 = vector(2, 1, -1)
v19 = vector(2, 1, -2)
v20 = vector(2, 2, -1)
v21 = vector(2, 2, -2)
v22 = vector(1, 2, -1)
v23 = vector(1, 2, -2)
v24 = vector(1, 0, -1)
v25 = vector(1, 0, -2)
v26 = vector(1, 1, -2)

# all posible orientations of each small cube
orientwhite = vector(0, 1, 0)
orientblue = vector(0, 0, 1)
orientyellow = vector(0, -1, 0)
orientred = vector(-1, 0, 0)
orientorange = vector(1, 0, 0)
orientgreen = vector(0, 0, -1)
cubes = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10, cube11, cube12, cube13, cube14, cube15,
         cube16, cube17, cube18, cube19, cube20, cube21, cube22, cube23, cube24, cube25, cube26]
vectors = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23,
           v24, v25, v26]

# loop for definin small cube positions
for i in range(len(cubes)):
    cubes[i].pos = vectors[i]

# here I defined small cubes to object according to where they are located. Look at line 45
c1 = corner_cube(v1, v1, cube1, orientwhite, orientwhite, orientred, orientred, orientblue, orientblue)
c3 = corner_cube(v3, v3, cube3, orientwhite, orientwhite, orientorange, orientorange, orientblue, orientblue)
c7 = corner_cube(v7, v7, cube7, orientyellow, orientyellow, orientred, orientred, orientblue, orientblue)
c9 = corner_cube(v9, v9, cube9, orientyellow, orientyellow, orientorange, orientorange, orientblue, orientblue)
c11 = corner_cube(v11, v11, cube11, orientyellow, orientyellow, orientred, orientred, orientgreen, orientgreen)
c15 = corner_cube(v15, v15, cube15, orientgreen, orientgreen, orientred, orientred, orientwhite, orientwhite)
c17 = corner_cube(v17, v17, cube17, orientyellow, orientyellow, orientorange, orientorange, orientgreen, orientgreen)
c21 = corner_cube(v21, v21, cube21, orientorange, orientorange, orientgreen, orientgreen, orientwhite, orientwhite)

c2 = edge_cube(v2, v2, cube2, orientwhite, orientwhite, orientblue, orientblue)
c4 = edge_cube(v4, v4, cube4, orientblue, orientblue, orientred, orientred)
c6 = edge_cube(v6, v6, cube6, orientblue, orientblue, orientorange, orientorange)
c8 = edge_cube(v8, v8, cube8, orientyellow, orientyellow, orientblue, orientblue)
c10 = edge_cube(v10, v10, cube10, orientyellow, orientyellow, orientred, orientred)
c13 = edge_cube(v13, v13, cube13, orientred, orientred, orientgreen, orientgreen)
c14 = edge_cube(v14, v14, cube14, orientwhite, orientwhite, orientred, orientred)
c16 = edge_cube(v16, v16, cube16, orientyellow, orientyellow, orientorange, orientorange)
c19 = edge_cube(v19, v19, cube19, orientorange, orientorange, orientgreen, orientgreen)
c20 = edge_cube(v20, v20, cube20, orientwhite, orientwhite, orientorange, orientorange)
c23 = edge_cube(v23, v23, cube23, orientwhite, orientwhite, orientgreen, orientgreen)
c25 = edge_cube(v25, v25, cube25, orientyellow, orientyellow, orientred, orientred)
clocks = [c1, c2, c3, c4, c6, c7, c8, c9, c10, c11, c13, c14, c15, c16, c17, c19, c20, c21, c23, c25]


# All functions for rotations
# time1 = 0.1
def slider(s):
    time = s


def front_rotation_clock():
    for i in range(len(clocks)):
        clocks[i].front_turn_clock()
    # time.sleep(time1)


def front_rotation_counter():
    for i in range(len(clocks)):
        clocks[i].front_turn_counter()
    # time.sleep(time1)


def back_rotation_clock():
    for i in range(len(clocks)):
        clocks[i].back_turn_clock()
    # time.sleep(time1)


def back_rotation_counter():
    for i in range(len(clocks)):
        clocks[i].back_turn_counter()
    # time.sleep(time1)


def top_rotation_counter():
    for i in range(len(clocks)):
        clocks[i].top_turn_counter()
    # time.sleep(time1)


def top_rotation_clock():
    for i in range(len(clocks)):
        clocks[i].top_turn_clock()
    # time.sleep(time1)


def down_rotation_clock():
    for i in range(len(clocks)):
        clocks[i].down_turn_clock()
    # time.sleep(time1)


def down_rotation_counter():
    for i in range(len(clocks)):
        clocks[i].down_turn_counter()
    # time.sleep(time1)


def right_rotation_clock():
    for i in range(len(clocks)):
        clocks[i].right_turn_clock()
    # time.sleep(time1)


def right_rotation_counter():
    for i in range(len(clocks)):
        clocks[i].right_turn_counter()
    # time.sleep(time1)


def left_rotation_clock():
    for i in range(len(clocks)):
        clocks[i].left_turn_clock()
    # time.sleep(time1)


def left_rotation_counter():
    for i in range(len(clocks)):
        clocks[i].left_turn_counter()
    # time.sleep(time1)


# randomizer
def randomizer():
    random_num1 = random.randint(10, 20)
    while random_num1 > 0:
        random_num2 = random.randint(0, 3)
        random_num3 = random.randint(0, 3)
        random_num4 = random.randint(0, 3)
        random_num5 = random.randint(0, 3)
        random_num6 = random.randint(0, 3)
        random_num7 = random.randint(0, 3)
        while random_num2 > 0:
            front_rotation_clock()
            random_num2 -= 1
        while random_num3 > 0:
            top_rotation_clock()
            random_num3 -= 1
        while random_num4 > 0:
            right_rotation_clock()
            random_num4 -= 1
        while random_num5 > 0:
            left_rotation_clock()
            random_num5 -= 1
        while random_num6 > 0:
            down_rotation_clock()
            random_num6 -= 1
        while random_num7 > 0:
            back_rotation_clock()
            random_num7 -= 1
        random_num1 -= 1


#
#
#
# A.I. algorithems to solve a cube

# Firs layer the cross

def solver():
    start = time.time()  # start mesuring the time to solve the cube

    # algorithems for solving the cross
    def cross_filler(pos):
        if pos == vector(2, 0, -1):
            right_rotation_clock()
            left_rotation_counter()
            front_rotation_counter()
            right_rotation_counter()
            left_rotation_clock()
        elif pos == vector(1, 0, 0):
            back_rotation_counter()
            front_rotation_clock()
            left_rotation_counter()
            back_rotation_clock()
            front_rotation_counter()
        elif pos == vector(0, 0, -1):
            right_rotation_counter()
            left_rotation_clock()
            back_rotation_counter()
            right_rotation_clock()
            left_rotation_counter()
        elif pos == vector(1, 0, -2):
            back_rotation_clock()
            front_rotation_counter()
            right_rotation_counter()
            back_rotation_counter()
            front_rotation_clock()

    def unlocking_for_white_cross(pos):
        if pos == vector(0, 1, -2):
            back_rotation_clock()
            down_rotation_counter()
            back_rotation_counter()
        if pos == vector(2, 1, -2):
            back_rotation_counter()
            down_rotation_counter()
            back_rotation_clock()
        if pos == vector(0, 1, 0):
            front_rotation_counter()
            down_rotation_clock()
            front_rotation_clock()
        if pos == vector(2, 1, 0):
            front_rotation_clock()
            down_rotation_clock()
            front_rotation_counter()

    def bringing_piece_from_the_top(pos):
        if pos == vector(1, 2, 0):
            right_rotation_clock()
            left_rotation_counter()
            front_rotation_counter()
            right_rotation_counter()
            left_rotation_clock()
        if pos == vector(1, 2, -2):
            right_rotation_counter()
            left_rotation_clock()
            back_rotation_clock()
            right_rotation_clock()
            left_rotation_counter()
        if pos == vector(0, 2, -1):
            front_rotation_clock()
            back_rotation_counter()
            left_rotation_clock()
            front_rotation_counter()
            back_rotation_clock()
        if pos == vector(2, 2, -1):
            front_rotation_counter()
            back_rotation_clock()
            right_rotation_clock()
            front_rotation_clock()
            back_rotation_counter()

    def orienting_cross_pieces(pos, name):
        if pos == vector(1, 2, 0):
            right_rotation_clock()
            left_rotation_counter()
            front_rotation_clock()
            front_rotation_clock()
            right_rotation_clock()
            left_rotation_counter()
            down_rotation_clock()
            cross_filler(name.position)
        if pos == vector(0, 2, -1):
            front_rotation_clock()
            back_rotation_counter()
            left_rotation_clock()
            left_rotation_clock()
            front_rotation_counter()
            back_rotation_clock()
            down_rotation_clock()
            cross_filler(name.position)
        if pos == vector(2, 2, -1):
            front_rotation_counter()
            back_rotation_clock()
            right_rotation_clock()
            right_rotation_clock()
            front_rotation_clock()
            back_rotation_counter()
            down_rotation_clock()
            cross_filler(name.position)
        if pos == vector(1, 2, -2):
            right_rotation_clock()
            left_rotation_counter()
            back_rotation_clock()
            back_rotation_clock()
            down_rotation_clock()
            cross_filler(name.position)

    # cross A. I
    while c23.position != c23.correct_position or c2.position != c2.correct_position or c14.position != c14.correct_position or c20.position != c20.correct_position:
        while c2.position != c2.correct_position:
            if c2.position == vector(1, 0, 0):
                front_rotation_clock()
                front_rotation_clock()
            elif c2.position == vector(0, 1, 0):
                front_rotation_clock()
            elif c2.position == vector(2, 1, 0):
                front_rotation_counter()
            elif c2.position == vector(2, 0, -1):
                cross_filler(c2.position)
            elif c2.position == vector(1, 0, -2):
                down_rotation_counter()
                cross_filler(c2.position)
            elif c2.position == vector(0, 0, -1):
                down_rotation_clock()
                cross_filler(c2.position)
            elif c2.position == vector(0, 2, -1):
                top_rotation_counter()
            elif c2.position == vector(2, 2, -1):
                top_rotation_clock()
            elif c2.position == vector(1, 2, -2):
                top_rotation_clock()
                top_rotation_clock()
            elif c2.position == vector(0, 1, -2) or c2.position == vector(2, 1, -2):
                unlocking_for_white_cross(c2.position)
                cross_filler(c2.position)
        if c2.orientation1 != c2.correct_orientation1:
            orienting_cross_pieces(c2.position, c2)
        while c14.position != c14.correct_position:
            if c14.position == vector(0, 1, 0):
                left_rotation_counter()
            elif c14.position == vector(0, 0, -1):
                left_rotation_counter()
                left_rotation_counter()
            elif c14.position == vector(0, 1, -2):
                left_rotation_clock()
            elif c14.position == vector(1, 0, 0):
                cross_filler(c14.position)
            elif c14.position == vector(2, 0, -1):
                down_rotation_counter()
                cross_filler(c14.position)
            elif c14.position == vector(1, 0, -2):
                down_rotation_counter()
                down_rotation_counter()
                cross_filler(c14.position)
            elif c14.position == vector(2, 1, -2) or c14.position == vector(2, 1, 0):
                unlocking_for_white_cross(c14.position)
            else:
                bringing_piece_from_the_top(c14.position)
        if c14.orientation1 != c14.correct_orientation1:
            orienting_cross_pieces(c14.position, c14)

        while c20.position != c20.correct_position:
            if c20.position == vector(2, 1, 0):
                right_rotation_clock()
            elif c20.position == vector(2, 0, -1):
                right_rotation_clock()
                right_rotation_clock()
            elif c20.position == vector(2, 1, -2):
                right_rotation_counter()
            elif c20.position == vector(1, 0, -2):
                cross_filler(c20.position)
            elif c20.position == vector(0, 0, -1):
                down_rotation_counter()
                cross_filler(c20.position)
            elif c20.position == vector(1, 0, 0):
                down_rotation_counter()
                down_rotation_counter()
                cross_filler(c20.position)
            elif c20.position == vector(0, 1, 0) or c20.position == vector(0, 1, -2):
                unlocking_for_white_cross(c20.position)
            else:
                bringing_piece_from_the_top(c20.position)
        if c20.orientation1 != c20.correct_orientation1:
            orienting_cross_pieces(c20.position, c20)
        while c23.position != c23.correct_position:
            if c23.position == vector(0, 1, -2):
                back_rotation_counter()
            elif c23.position == vector(1, 0, -2):
                back_rotation_counter()
                back_rotation_counter()
            elif c23.position == vector(2, 1, -2):
                back_rotation_clock()
            elif c23.position == vector(0, 0, -1):
                cross_filler(c23.position)
            elif c23.position == vector(1, 0, 0):
                down_rotation_counter()
                cross_filler(c23.position)
            elif c23.position == vector(2, 0, -1):
                down_rotation_counter()
                down_rotation_counter()
                cross_filler(c23.position)
            elif c23.position == vector(0, 1, 0) or c23.position == vector(2, 1, 0):
                unlocking_for_white_cross(c23.position)
        if c23.orientation1 != c23.correct_orientation1:
            orienting_cross_pieces(c23.position, c23)

    # first layer algorithems
    def toplayeremaker(pos):
        if pos == vector(2, 0, 0):
            left_rotation_clock()
            down_rotation_counter()
            left_rotation_counter()
        elif pos == vector(2, 0, -2):
            front_rotation_clock()
            down_rotation_counter()
            front_rotation_counter()
        elif pos == vector(0, 0, -2):
            right_rotation_clock()
            down_rotation_counter()
            right_rotation_counter()
        elif pos == vector(0, 0, 0):
            back_rotation_clock()
            down_rotation_counter()
            back_rotation_counter()

    def toplayer_bring_down(pos):
        if pos == vector(2, 2, 0):
            right_rotation_counter()
            down_rotation_clock()
            right_rotation_clock()
        elif pos == vector(2, 2, -2):
            right_rotation_clock()
            down_rotation_clock()
            right_rotation_counter()
        elif pos == vector(0, 2, 0):
            left_rotation_clock()
            down_rotation_clock()
            left_rotation_counter()
        elif pos == vector(0, 2, -2):
            left_rotation_counter()
            down_rotation_clock()
            left_rotation_clock()

    def correctorientation(pos, name):
        if pos == vector(0, 2, 0):
            left_rotation_clock()
            down_rotation_counter()
            left_rotation_counter()
            down_rotation_clock()
            toplayeremaker(name.position)
        elif pos == vector(2, 2, 0):
            front_rotation_clock()
            down_rotation_counter()
            front_rotation_counter()
            down_rotation_clock()
            toplayeremaker(name.position)
        elif pos == vector(2, 2, -2):
            right_rotation_clock()
            down_rotation_counter()
            right_rotation_counter()
            down_rotation_clock()
            toplayeremaker(name.position)
        elif pos == vector(0, 2, -2):
            back_rotation_clock()
            down_rotation_counter()
            back_rotation_counter()
            down_rotation_clock()
            toplayeremaker(name.position)

    # first layer A.I.
    while c1.position != c1.correct_position or c21.position != c21.correct_position or c3.position != c3.correct_position or c15.position != c15.correct_position:
        while c1.position != c1.correct_position:
            if c1.position == vector(2, 0, 0):
                toplayeremaker(c1.position)
            elif c1.position == vector(2, 0, -2):
                down_rotation_counter()
                toplayeremaker(c1.position)
            elif c1.position == vector(0, 0, -2):
                down_rotation_counter()
                down_rotation_counter()
                toplayeremaker(c1.position)
            elif c1.position == vector(0, 0, 0):
                down_rotation_clock()
                toplayeremaker(c1.position)
            elif c1.position == vector(2, 2, 0) or c1.position == vector(2, 2, -2) or c1.position == vector(0, 2, -2):
                toplayer_bring_down(c1.position)
        while c1.orientation1 != c1.correct_orientation1:
            correctorientation(c1.position, c1)

        while c3.position != c3.correct_position:
            if c3.position == vector(2, 0, -2):
                toplayeremaker(c3.position)
            elif c3.position == vector(0, 0, -2):
                down_rotation_counter()
                toplayeremaker(c3.position)
            elif c3.position == vector(0, 0, 0):
                down_rotation_counter()
                down_rotation_counter()
                toplayeremaker(c3.position)
            elif c3.position == vector(2, 0, 0):
                down_rotation_clock()
                toplayeremaker(c3.position)
            elif c3.position == vector(2, 2, -2) or c3.position == vector(0, 2, -2):
                toplayer_bring_down(c3.position)
        while c3.orientation1 != c3.correct_orientation1:
            correctorientation(c3.position, c3)

        while c21.position != c21.correct_position:
            if c21.position == vector(0, 0, -2):
                toplayeremaker(c21.position)
            elif c21.position == vector(0, 0, 0):
                down_rotation_counter()
                toplayeremaker(c21.position)
            elif c21.position == vector(2, 0, 0):
                down_rotation_counter()
                down_rotation_counter()
                toplayeremaker(c21.position)
            elif c21.position == vector(2, 0, -2):
                down_rotation_clock()
                toplayeremaker(c21.position)
            elif c21.position == vector(0, 2, -2):
                toplayer_bring_down(c21.position)
        while c21.orientation1 != c21.correct_orientation1:
            correctorientation(c21.position, c21)

        while c15.position != c15.correct_position:
            if c15.position == vector(0, 0, 0):
                toplayeremaker(c15.position)
            elif c15.position == vector(2, 0, 0):
                down_rotation_counter()
                toplayeremaker(c15.position)
            elif c15.position == vector(2, 0, -2):
                down_rotation_counter()
                down_rotation_counter()
                toplayeremaker(c15.position)
            elif c15.position == vector(0, 0, -2):
                down_rotation_clock()
                toplayeremaker(c15.position)
        while c15.orientation1 != c15.correct_orientation1:
            correctorientation(c15.position, c15)

    # second layer algorithems
    def algorithem_for_positioning(pos):
        if pos == vector(2, 0, -1):
            back_rotation_counter()
            left_rotation_clock()
            front_rotation_counter()
            back_rotation_clock()
            down_rotation_counter()
            front_rotation_clock()
            down_rotation_clock()
            front_rotation_clock()
            back_rotation_counter()
            left_rotation_counter()
            back_rotation_clock()
            front_rotation_counter()

        if pos == vector(1, 0, -2):
            left_rotation_counter()
            front_rotation_clock()
            left_rotation_clock()
            right_rotation_counter()
            down_rotation_counter()
            right_rotation_clock()
            down_rotation_clock()
            right_rotation_clock()
            left_rotation_counter()
            front_rotation_counter()
            right_rotation_counter()
            left_rotation_clock()

        if pos == vector(0, 0, -1):
            front_rotation_counter()
            right_rotation_clock()
            front_rotation_clock()
            back_rotation_counter()
            down_rotation_counter()
            back_rotation_clock()
            down_rotation_clock()
            back_rotation_clock()
            front_rotation_counter()
            right_rotation_counter()
            back_rotation_counter()
            front_rotation_clock()

        if pos == vector(1, 0, 0):
            right_rotation_counter()
            back_rotation_clock()
            left_rotation_counter()
            right_rotation_clock()
            down_rotation_counter()
            left_rotation_clock()
            down_rotation_clock()
            right_rotation_counter()
            left_rotation_clock()
            back_rotation_counter()
            right_rotation_clock()
            left_rotation_counter()

    def algorithem_for_positioning_second(pos):
        if pos == vector(2, 0, -1):
            front_rotation_clock()
            left_rotation_counter()
            front_rotation_counter()
            back_rotation_clock()
            down_rotation_clock()
            back_rotation_counter()
            down_rotation_clock()
            front_rotation_clock()
            back_rotation_counter()
            left_rotation_counter()
            back_rotation_clock()
            front_rotation_counter()

        if pos == vector(1, 0, -2):  # c4
            right_rotation_clock()
            front_rotation_counter()
            left_rotation_clock()
            right_rotation_counter()
            down_rotation_clock()
            left_rotation_counter()
            down_rotation_clock()
            right_rotation_clock()
            left_rotation_counter()
            front_rotation_counter()
            right_rotation_counter()
            left_rotation_clock()

        if pos == vector(0, 0, -1):  # c6
            back_rotation_clock()
            right_rotation_counter()
            front_rotation_clock()
            back_rotation_counter()
            down_rotation_clock()
            front_rotation_counter()
            down_rotation_clock()
            back_rotation_clock()
            front_rotation_counter()
            right_rotation_counter()
            back_rotation_counter()
            front_rotation_clock()

        if pos == vector(1, 0, 0):  # c19
            left_rotation_clock()
            back_rotation_counter()
            left_rotation_counter()
            right_rotation_clock()
            down_rotation_clock()
            right_rotation_counter()
            down_rotation_clock()
            right_rotation_counter()
            left_rotation_clock()
            back_rotation_counter()
            right_rotation_clock()
            left_rotation_counter()

    # second layer A.I
    while c4.position != c4.correct_position or c6.position != c6.correct_position or c19.position != c19.correct_position or c13.position != c13.correct_position:
        for x in range(6):
            if c4.position != c4.correct_position:
                if c4.position == vector(2, 0, -1) or c4.position == vector(1, 0, -2) or c4.position == vector(0, 0,
                                                                                                               -1) or c4.position == vector(
                        1, 0, 0):
                    while c4.orientation1 != c4.correct_orientation1 and c4.orientation2 != c4.correct_orientation2:
                        down_rotation_clock()
                    if c4.position == vector(0, 0, -1):
                        down_rotation_counter()
                        algorithem_for_positioning_second(c4.position)
                    if c4.position == vector(1, 0, 0):
                        down_rotation_clock()
                        algorithem_for_positioning(c4.position)

            if c6.position != c6.correct_position:
                if c6.position == vector(2, 0, -1) or c6.position == vector(1, 0, -2) or c6.position == vector(0, 0,
                                                                                                               -1) or c6.position == vector(
                        1, 0, 0):
                    while c6.orientation1 != c6.correct_orientation1 and c6.orientation2 != c6.correct_orientation2:
                        down_rotation_clock()
                    if c6.position == vector(1, 0, 0):
                        down_rotation_counter()
                        algorithem_for_positioning_second(c6.position)
                    if c6.position == vector(2, 0, -1):
                        down_rotation_clock()
                        algorithem_for_positioning(c6.position)

            if c19.position != c19.correct_position:
                if c19.position == vector(2, 0, -1) or c19.position == vector(1, 0, -2) or c19.position == vector(0, 0,
                                                                                                                  -1) or c19.position == vector(
                        1, 0, 0):
                    while c19.orientation1 != c19.correct_orientation1 and c19.orientation2 != c19.correct_orientation2:
                        down_rotation_clock()
                    if c19.position == vector(2, 0, -1):
                        down_rotation_counter()
                        algorithem_for_positioning_second(c19.position)
                    if c19.position == vector(1, 0, -2):
                        down_rotation_clock()
                        algorithem_for_positioning(c19.position)

            if c13.position != c13.correct_position:
                if c13.position == vector(2, 0, -1) or c13.position == vector(1, 0, -2) or c13.position == vector(0, 0,
                                                                                                                  -1) or c13.position == vector(
                        1, 0, 0):
                    x = 0
                    while c13.orientation1 != c13.correct_orientation1 and c13.orientation2 != c13.correct_orientation2:
                        down_rotation_clock()
                    if c13.position == vector(1, 0, -2):
                        down_rotation_counter()
                        algorithem_for_positioning_second(c13.position)
                    if c13.position == vector(0, 0, -1):
                        down_rotation_clock()
                        algorithem_for_positioning(c13.position)

        if c4.position != c4.correct_position or c4.orientation1 != c4.correct_orientation1:
            algorithem_for_positioning(vector(1, 0, 0))
        if c6.position != c6.correct_position or c6.orientation1 != c6.correct_orientation1:
            algorithem_for_positioning(vector(1, 0, -2))
        if c19.position != c19.correct_position or c19.orientation1 != c19.correct_orientation1:
            algorithem_for_positioning(vector(0, 0, -1))
        if c13.position != c13.correct_position or c13.orientation1 != c13.correct_orientation1:
            algorithem_for_positioning(vector(1, 0, 0))

    # last layer cross algorithems
    def fruruf():
        front_rotation_clock()
        left_rotation_clock()
        down_rotation_clock()
        left_rotation_counter()
        down_rotation_counter()
        front_rotation_counter()

    def fururf():
        front_rotation_clock()
        down_rotation_clock()
        left_rotation_clock()
        down_rotation_counter()
        left_rotation_counter()
        front_rotation_counter()

    def rururuur():
        left_rotation_clock()
        down_rotation_clock()
        left_rotation_counter()
        down_rotation_clock()
        left_rotation_clock()
        down_rotation_clock()
        down_rotation_clock()
        left_rotation_counter()

    # last layer cross A.I
    if c7.orientation1 != c7.correct_orientation1 or c9.orientation1 != c9.correct_orientation1 or c11.orientation1 != c11.correct_orientation1 or c17.orientation1 != c17.correct_orientation1:
        x = 0
        debug = 0
        while c8.orientation1 != c8.correct_orientation1 or c10.orientation1 != c10.correct_orientation1 or c16.orientation1 != c16.correct_orientation1 or c25.orientation1 != c25.correct_orientation1:
            fruruf()
            x += 1
            debug += 1
            if x == 4:
                down_rotation_clock()
                x = 0
            if debug == 10:
                fururf()
            if debug == 20:
                break
        y = 0
        while c7.orientation1 != c7.correct_orientation1 or c9.orientation1 != c9.correct_orientation1 or c11.orientation1 != c11.correct_orientation1 or c17.orientation1 != c17.correct_orientation1:
            if c7.orientation1 != c7.correct_orientation1 and c9.orientation1 != c9.correct_orientation1 and c11.orientation1 != c11.correct_orientation1 and c17.orientation1 != c17.correct_orientation1:
                while c7.orientation1 != vector(1, 0, 0) and c9.orientation1 != vector(1, 0,
                                                                                       0) and c11.orientation1 != vector(
                        1, 0, 0) and c17.orientation1 != vector(1, 0, 0):
                    down_rotation_clock()
                rururuur()
            if (
                    c7.orientation1 == c7.correct_orientation1 and c9.orientation1 != c9.correct_orientation1 and c11.orientation1 != c11.correct_orientation1 and c17.orientation1 != c17.correct_orientation1) or (
                    c7.orientation1 != c7.correct_orientation1 and c9.orientation1 == c9.correct_orientation1 and c11.orientation1 != c11.correct_orientation1 and c17.orientation1 != c17.correct_orientation1) or (
                    c7.orientation1 != c7.correct_orientation1 and c9.orientation1 != c9.correct_orientation1 and c11.orientation1 == c11.correct_orientation1 and c17.orientation1 != c17.correct_orientation1) or (
                    c7.orientation1 != c7.correct_orientation1 and c9.orientation1 != c9.correct_orientation1 and c11.orientation1 != c11.correct_orientation1 and c17.orientation1 == c17.correct_orientation1):
                check_for_orient = [c7, c9, c11, c17]
                for x in range(len(check_for_orient)):
                    if check_for_orient[x].orientation1 == check_for_orient[x].correct_orientation1:
                        while check_for_orient[x].position != vector(2, 0, 0):
                            down_rotation_clock()
                        rururuur()
                        break
            g = 0
            check_for_orient = [c7, c9, c11, c17]
            for x in range(len(check_for_orient)):
                if check_for_orient[x].orientation1 == check_for_orient[x].correct_orientation1:
                    g += 1
            if g == 2:
                for x in range(len(check_for_orient)):
                    if check_for_orient[x].orientation1 != check_for_orient[x].correct_orientation1:
                        debug = 0
                        while check_for_orient[x].position != vector(2, 0, 0) and check_for_orient[
                            x].orientation1 != vector(0, 0, 1):
                            down_rotation_clock()
                            debug += 1
                            if debug == 4:
                                break
                rururuur()
    corners = [c7, c9, c11, c17]

    # last layer corners
    def ruur():
        left_rotation_clock()
        down_rotation_clock()
        down_rotation_clock()
        left_rotation_counter()
        down_rotation_counter()
        left_rotation_clock()
        down_rotation_clock()
        down_rotation_clock()
        right_rotation_counter()
        down_rotation_clock()
        left_rotation_counter()
        down_rotation_counter()
        right_rotation_clock()

    def ruur2():
        right_rotation_clock()
        down_rotation_clock()
        down_rotation_clock()
        right_rotation_counter()
        down_rotation_counter()
        right_rotation_clock()
        down_rotation_clock()
        down_rotation_clock()
        left_rotation_counter()
        down_rotation_clock()
        right_rotation_counter()
        down_rotation_counter()
        left_rotation_clock()

    def ruur3():
        front_rotation_clock()
        down_rotation_clock()
        down_rotation_clock()
        front_rotation_counter()
        down_rotation_counter()
        front_rotation_clock()
        down_rotation_clock()
        down_rotation_clock()
        back_rotation_counter()
        down_rotation_clock()
        front_rotation_counter()
        down_rotation_counter()
        back_rotation_clock()

    def ruur1():
        left_rotation_counter()
        front_rotation_clock()
        left_rotation_counter()
        back_rotation_clock()
        back_rotation_clock()
        left_rotation_clock()
        front_rotation_counter()
        left_rotation_counter()
        back_rotation_clock()
        back_rotation_clock()
        left_rotation_clock()
        left_rotation_clock()
        down_rotation_counter()

    # positioning the last layer corners
    for x in range(5):
        while c9.position != c9.correct_position or c17.position != c17.correct_position or c7.position != c7.correct_position or c11.position != c11.correct_position:
            num_of_correct_corrners = 0
            while num_of_correct_corrners < 2:
                down_rotation_clock()
                for x in range(len(corners)):
                    if corners[x].position == corners[x].correct_position:
                        num_of_correct_corrners += 1
            if c9.position == c9.correct_position and c17.position == c17.correct_position:
                ruur()
                break
            elif c11.position == c11.correct_position and c17.position == c17.correct_position:
                ruur1()
                break
            elif c7.position == c7.correct_position and c9.position == c9.correct_position:
                ruur2()
                break
            elif c7.position == c7.correct_position and c11.position == c11.correct_position:
                ruur3()
                break
            else:
                ruur()

    def lastlayer_position():
        front_rotation_clock()
        front_rotation_clock()
        down_rotation_clock()
        right_rotation_clock()
        left_rotation_counter()
        front_rotation_clock()
        front_rotation_clock()
        right_rotation_counter()
        left_rotation_clock()
        down_rotation_clock()
        front_rotation_clock()
        front_rotation_clock()

    def lastlayer_position1():
        back_rotation_clock()
        back_rotation_clock()
        down_rotation_clock()
        right_rotation_counter()
        left_rotation_clock()
        back_rotation_clock()
        back_rotation_clock()
        right_rotation_clock()
        left_rotation_counter()
        down_rotation_clock()
        back_rotation_clock()
        back_rotation_clock()

    def lastlayer_position2():
        right_rotation_clock()
        right_rotation_clock()
        down_rotation_clock()
        back_rotation_clock()
        front_rotation_counter()
        right_rotation_clock()
        right_rotation_clock()
        back_rotation_counter()
        front_rotation_clock()
        down_rotation_clock()
        right_rotation_clock()
        right_rotation_clock()

    def lastlayer_position3():
        left_rotation_clock()
        left_rotation_clock()
        down_rotation_clock()
        back_rotation_counter()
        front_rotation_clock()
        left_rotation_clock()
        left_rotation_clock()
        back_rotation_clock()
        front_rotation_clock()
        down_rotation_clock()
        left_rotation_clock()
        left_rotation_clock()

    debug = 0
    # positioning the last layer edges
    while c8.position != c8.correct_position or c10.position != c10.correct_position or c16.position != c16.correct_position or c25.position != c25.correct_position:

        if c8.position != c8.correct_position and c10.position != c10.correct_position and c16.position != c16.correct_position and c25.position != c25.correct_position:
            lastlayer_position()
        if c25.position == c25.correct_position:
            lastlayer_position()
        elif c8.position == c8.correct_position:
            lastlayer_position1()
        elif c10.position == c10.correct_position:
            lastlayer_position2()
        elif c16.position == c16.correct_position:
            lastlayer_position3()
        debug += 1
        if debug == 10:
            break
    end = time.time()
    print(end - start)


# control buttons
button(bind=randomizer, text="Randomize")
button(bind=solver, text="Solver")
scene.append_to_caption('\n\n')
scene.append_to_caption(
    '<a href="https://www.youtube.com/watch?v=q2vJTjzdNPA&t=1s"><h2>Make sure you check the video on how i did it here</h2></a>')
scene.append_to_caption('\n')
scene.append_to_caption('<a href="http://bit.do/e6c6X>"><h2>And sub to my channel for more here</h2></a>')
scene.append_to_caption('\n\n')
button(bind=front_rotation_clock, text="Front Clock")
button(bind=back_rotation_clock, text="Back Clock")
button(bind=right_rotation_clock, text="right Clock")
button(bind=left_rotation_clock, text="left Clock")
button(bind=top_rotation_clock, text="top Clock")
button(bind=down_rotation_clock, text="down Clock")