from datetime import *
import time
from tkinter import *
from tkinter import ttk

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300 

TIME_WINDOW_WIDTH = 400 
TIME_WINDOW_HEIGHT = 200

class Pomodoro:
    def __init__(self, root) -> None:
        self.root = root
        self.times = []
        self.root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.root.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.root.title('Pomodoro')
        self.display = ttk.Label(self.root, text='00:00', font='roboto 40 bold')
        self.display.place(y=-40, relx=.5, rely=.5, anchor=CENTER)
        self.set_time_button = ttk.Button(root, text='Set time')
        self.set_time_button.place(y=50, relx=.5, rely=.5, anchor=CENTER)
        self.set_time_button.bind('<Button-1>', self.set_time_window)

        self.go_button = ttk.Button(self.root, text='Go!', width=3)
        self.go_button.place(y=90, relx=.5, rely=.5, anchor=CENTER)
        self.go_button.bind('<Button-1>', self.run_work_time)

    def set_time_window(self, event):
        self.time_window = Toplevel()
        self.time_window.title('Time')
        self.time_window.minsize(width=TIME_WINDOW_WIDTH, height=TIME_WINDOW_HEIGHT)
        self.time_window.maxsize(width=TIME_WINDOW_WIDTH, height=TIME_WINDOW_HEIGHT)

        self.work_time_label = ttk.Label(self.time_window, text='Minutes you want to spend working:')
        self.work_time_label.place(x=20, y=30)
        self.work_time_entry = ttk.Entry(self.time_window, width=5)
        self.work_time_entry.place(x=265, y=30)

        self.rest_time_label = ttk.Label(self.time_window, text='Minutes you want to spend resting: ')
        self.rest_time_label.place(x=20, y=90)
        self.rest_time_entry = ttk.Entry(self.time_window, width=5)
        self.rest_time_entry.place(x=265, y=90)

        self.apply_button = ttk.Button(self.time_window, text='Apply', width=5)
        self.apply_button.place(x=175,y=150)
        self.apply_button.bind('<Button-1>', self.save_time)

    def save_time(self, event):
        work_time = self.work_time_entry.get()
        rest_time = self.rest_time_entry.get()
        self.times = [int(work_time)*60, int(rest_time)*60] # save the time in seconds
        self.times_backup = (int(work_time)*60, int(rest_time)*60) # store the intial values to restart the time
        seconds = int(work_time)*60
        self.work_time = self.seconds_to_string(seconds)
        self.display['text'] = self.work_time
        self.time_window.destroy()
        self.root.update()

    def run_work_time(self, event):
        if self.times[0] >= 0:
            work_time = self.times[0]
            self.times[0] -= 1
            work_time_string = self.seconds_to_string(work_time)
            self.display['text'] = work_time_string
            self.display.after(50, lambda event=event: self.run_work_time(event))
            self.go_button_event = event

        else:
            self.times[1] = self.times_backup[1]
            time.sleep(1)
            self.run_rest_time()

    def run_rest_time(self):
        if self.times[1] >= 0:
            rest_time = self.times[1]
            self.times[1] -= 1
            rest_time_string = self.seconds_to_string(rest_time)
            self.display['text'] = rest_time_string
            self.display.after(50, self.run_rest_time)
        else:
            self.times[0] = self.times_backup[0]
            time.sleep(1)
            self.run_work_time(self.go_button_event)

    def seconds_to_string(self, seconds):
        minute, second = divmod(seconds, 60)
        time_string = f'{minute:02d}:{second:02d}'

        return time_string

def main():
    root = Tk()
    style = ttk.Style(root)
    style.theme_use('clam')
    pomodoro_clock = Pomodoro(root)
    root.mainloop()

if __name__ == '__main__':
    main()