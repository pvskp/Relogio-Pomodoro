import time
from tkinter import *
from tkinter import ttk

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300 

TIME_WINDOW_WIDTH = 200
TIME_WINDOW_HEIGHT = 200

def map_buttons(root):
    button = ttk.Button(root, text='set time')
    button.place(y=50, relx=.5, rely=.5, anchor=CENTER)
    button.bind('<Button-1>', set_time_window)

def set_time_window(event):
    time_window = Toplevel()
    time_window.title('Time')
    time_window.minsize(width=TIME_WINDOW_WIDTH, height=TIME_WINDOW_HEIGHT)
    time_window.maxsize(width=TIME_WINDOW_WIDTH, height=TIME_WINDOW_HEIGHT)

    work_time = ttk.Entry(time_window)
    work_time.grid()

def create_buttons_database():
    buttons = dict()
    return buttons

def create_main_window():

    root = Tk()
    style = ttk.Style(root)
    style.theme_use('clam')
    root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    root.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

    # root_entry = ttk.Entry(root, textvariable=IntVar())

    # root_entry.place(y=40, relx=.5, rely=.5, anchor=CENTER)

    root.title('Pomodoro')

    return root

def main():
    root = create_main_window()
    # buttons = create_buttons_database()
    map_buttons(root)
    root.mainloop()

if __name__ == '__main__':
    main()