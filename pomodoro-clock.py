import time
from tkinter import *
from tkinter import ttk

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300 

def map_buttons(root):
    button = ttk.Button(root, text='set time')
    button.place(y=50, relx=.5, rely=.5, anchor=CENTER)
    button.bind('<Button-1>', set_time_window)
    
    pass

def set_time_window(event):
    time_window = Toplevel()
    time_window.title('Time')

def create_buttons_database():
    buttons = dict()
    return buttons

def create_main_window():

    root = Tk()
    style = ttk.Style(root)
    style.theme_use('clam')
    root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    root.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

    root_entry = ttk.Entry(root, textvariable=IntVar())

    # root_entry.place(y=40, relx=.5, rely=.5, anchor=CENTER)

    root.title('Pomodoro')

    return root

def main():
    root = create_main_window()
    buttons = create_buttons_database()
    map_buttons(root, buttons)
    root.mainloop()

if __name__ == '__main__':
    main()