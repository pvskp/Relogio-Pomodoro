from datetime import *
import time
from tkinter import *
from tkinter import ttk

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300 

TIME_WINDOW_WIDTH = 400 
TIME_WINDOW_HEIGHT = 200

time_to_work = int()
time_to_rest = int()
time_display_work = '00:00'
time_display_rest = str()

def save_time(event, time_window, work_time, rest_time):
    global time_to_work
    global time_to_rest
    global time_display
    global time_display_work, time_to_rest
    wks = work_time.get()
    rst = rest_time.get()

    if (wks == '') or (rst == ''):
        error_label = ttk.Label(time_window, text= 'Fill all fields!').place(x=160, y=120)
    else:
        time_to_work = int(wks)
        time_to_rest = int(rst)
        
        time_window.destroy()
        time_window.update()

        seconds_to_work = time_to_work*60
        seconds_to_rest = time_to_rest*60

        minutes, seconds = divmod(seconds_to_work, 60)

        time_display_work = f'{minutes:02d}:{seconds:02d}'
        
        print(time_display_work)

def time_window_buttons(time_window, work_time_entry, rest_time_entry):
    apply_button = ttk.Button(time_window, text='Apply', width=5)
    apply_button.place(x=175,y=150)
    apply_button.bind('<Button-1>', lambda event, time_window=time_window, wkt = work_time_entry, rst = rest_time_entry :save_time(event, time_window, wkt, rst))

def root_buttons(root):
    set_time_button = ttk.Button(root, text='set time')
    set_time_button.place(y=50, relx=.5, rely=.5, anchor=CENTER)
    set_time_button.bind('<Button-1>', set_time_window)

    go_button = ttk.Button(root, text='Go!', width=3)
    go_button.place(y=90, relx=.5, rely=.5, anchor=CENTER)


def set_time_window(event):
    time_window = Toplevel()
    time_window.title('Time')
    time_window.minsize(width=TIME_WINDOW_WIDTH, height=TIME_WINDOW_HEIGHT)
    time_window.maxsize(width=TIME_WINDOW_WIDTH, height=TIME_WINDOW_HEIGHT)

    work_time_label = ttk.Label(time_window, text='Minutes you want to spend working:')
    work_time_label.place(x=20, y=30)
    work_time_entry = ttk.Entry(time_window, width=5)
    work_time_entry.place(x=265, y=30)

    rest_time_label = ttk.Label(time_window, text='Minutes you want to spend resting: ')
    rest_time_label.place(x=20, y=90)
    rest_time_entry = ttk.Entry(time_window, width=5)
    rest_time_entry.place(x=265, y=90)

    time_window_buttons(time_window, work_time_entry, rest_time_entry)

def create_main_window():
    global time_display_work

    root = Tk()
    style = ttk.Style(root)
    style.theme_use('clam')
    root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    root.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
    root.title('Pomodoro')

    display = ttk.Label(root, text=time_display_work, font='roboto 40 bold')

    display.place(y=-40, relx=.5, rely=.5, anchor=CENTER)

    return root

def main():
    root = create_main_window()
    root_buttons(root)
    root.mainloop()

if __name__ == '__main__':
    main()