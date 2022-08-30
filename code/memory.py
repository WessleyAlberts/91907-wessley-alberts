from time import sleep
from tkinter import *

def close_window():
    """Closes the window when called"""
    master.destroy()

"""Creates the Main Menu"""
#Sets background colour to a variable
bg_colour = "#858585"
button_colour = "#707070"
toolbar_colour = "#5c5c5c"
text_colour = "#f5f5f5"

#Sets the main menu window
master = Tk()
master.attributes("-fullscreen", True)
master.geometry("1600x900")
master.title("Main Menu")

#Creates an "image" of a pixel
pixel = PhotoImage(width = 1, height = 1)

#Creates the area for the toolbar
toolbar = Frame(master, bg = toolbar_colour, width = 1600, height = 200)
toolbar.place(x = 0, y = 0)

#Creates the title for the game
game_title = Label(toolbar, bg = toolbar_colour, fg = text_colour, text = "Memory Test", font = ("TkDefaultFont", 36), image = pixel, width = 600, height = 150, compound = "c")
game_title.place(x = 500, y = 20)

#Creates the close button (Needed because of -fullscreen being True)
close_button = Button(toolbar, bg = toolbar_colour, fg = text_colour, text = "Close", font = ("TkDefaultFont", 24), command = close_window, image = pixel, height = 160, width = 160, compound = "c")
close_button.place(x = 1420, y = 20)

#Creates the area for the main content
body = Frame(master, bg = bg_colour, width = 1600, height = 700)
body.place(x = 0, y = 200)

correct_num = [1, 3, 8, 2]

number = Label(body, bg = bg_colour, width = len(correct_num), height = 1, text = ''.join([str(x) for x in correct_num]), font = ("TkDefaultFont", 24), compound = "c")
number.place(relx = 0.5, rely = 0.5, anchor = CENTER)

master.mainloop()