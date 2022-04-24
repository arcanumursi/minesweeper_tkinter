from tkinter import *
from cell import Cell
import settings
import utilities

root = Tk()
# Override the settings of the window
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root, 
    bg='black',
    width=settings.WIDTH,
    height=utilities.height_percentage(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root, 
    bg='black', 
    width=utilities.width_percentage(25),
    height=utilities.height_percentage(75)
)
left_frame.place(x=0, y=utilities.height_percentage(25))

center_frame = Frame(
    root,
    bg='black',  
    width=utilities.width_percentage(75),
    height=utilities.height_percentage(75)
)
center_frame.place(
    x=utilities.width_percentage(25), 
    y=utilities.height_percentage(25)
)

# Create cells
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, 
    y=0
)

Cell.randomize_mines()

# Run the window
root.mainloop()