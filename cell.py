from tkinter import Button
import random

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>', self.left_blick_actions) # Left click
        btn.bind('<Button-3>', self.right_blick_actions) # Right click
        self.cell_btn_object = btn

    def left_blick_actions(self, event):
        print(event)
        print("I am left clicked!")

    def right_blick_actions(self, event):
        print(event)
        print("I am right clicked!")

    @staticmethod
    def randomize_mines():
        my_list = ['Jim', 'Michael', 'Paul']
        picked_names = random.sample(my_list, 2)
        print(picked_names)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
