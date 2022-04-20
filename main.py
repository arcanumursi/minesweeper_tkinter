from tkinter import *
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
    bg='red', # Change later to black
    width=settings.WIDTH,
    height=utilities.height_percentage(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root, 
    bg='blue', # Change later to black
    width=utilities.height_percentage(25),
    height=utilities.height_percentage(75)
)

left_frame.place(x=0, y=utilities.height_percentage(25))
# Run the window
root.mainloop()