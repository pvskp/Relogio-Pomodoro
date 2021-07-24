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

def seconds_to_string(seconds):
    minute, second = divmod(seconds, 60)
    time_string = f'{minute:02d}:{second:02d}'

    return time_string

def update_time(event, root, display):
    actual_time = display['text']
    if actual_time != '00:00':
        total_seconds = datetime.strptime(actual_time, '%M:%S')
        actual_seconds = total_seconds.minute*60 + total_seconds.second - 1
        actual_time_string = seconds_to_string(actual_seconds)
        display['text'] = actual_time_string
        display.after(1000, lambda event=event, root=root, display=display: update_time(event, root, display))

def save_time(event, root, display, time_window, work_time, rest_time):
    global time_to_work, time_to_rest, time_display, time_display_work, time_to_rest

    wks = work_time.get()
    rst = rest_time.get()

    if (wks == '') or (rst == ''):
        error_label = ttk.Label(time_window, text= 'Fill all fields!').place(x=160, y=120)
    elif (not wks.isdigit()) or (not rst.isdigit()):
        error_label = ttk.Label(time_window, text= 'Only integers!').place(x=160, y=120)
    else:
        time_to_work = int(wks)
        time_to_rest = int(rst)
        
        time_window.destroy()
        time_window.update()

        seconds_to_work = time_to_work*60
        seconds_to_rest = time_to_rest*60

        string_time_work = seconds_to_string(seconds_to_work)

        time_display_work = string_time_work

        display['text'] = time_display_work

        root.update()

        print(time_display_work)

def time_window_buttons(root, display, time_window, work_time_entry, rest_time_entry):
    apply_button = ttk.Button(time_window, text='Apply', width=5)
    apply_button.place(x=175,y=150)
    apply_button.bind('<Button-1>', lambda event,root=root, display=display, time_window=time_window, wkt = work_time_entry, rst = rest_time_entry :save_time(event, root, display, time_window, wkt, rst))

def root_buttons(root, display):
    set_time_button = ttk.Button(root, text='Set time')
    set_time_button.place(y=50, relx=.5, rely=.5, anchor=CENTER)
    set_time_button.bind('<Button-1>', lambda event, root=root, display=display :set_time_window(event, root, display))

    go_button = ttk.Button(root, text='Go!', width=3)
    go_button.place(y=90, relx=.5, rely=.5, anchor=CENTER)
    go_button.bind('<Button-1>', lambda event, root=root, display=display: update_time(event, root, display))

def set_time_window(event, root, display):
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

    time_window_buttons(root, display, time_window, work_time_entry, rest_time_entry)

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

    return root, display

def main():
    root, display = create_main_window()
    root_buttons(root, display)
    root.mainloop()

if __name__ == '__main__':
    main()