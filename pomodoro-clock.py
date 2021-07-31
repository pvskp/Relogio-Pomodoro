import threading
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

        ## signals

        self.is_running = False
        self.pause_signal = False

        ## display

        self.display = ttk.Label(self.root, text='00:00', font='roboto 40 bold')
        self.display.place(y=-40, relx=.5, rely=.5, anchor=CENTER)

        ## message

        self.message = ttk.Label(self.root)
        self.message.place(y=-100, relx=.5, rely=.5, anchor=CENTER)

        ## set time button

        self.set_time_button = ttk.Button(root, text='Set time')
        self.set_time_button.place(y=50, relx=.5, rely=.5, anchor=CENTER)
        self.set_time_button.bind('<Button-1>', self.set_time_window)

        ## Go! button

        self.go_button = ttk.Button(self.root, width=3)
        self.go_button.place(y=90, relx=.5, rely=.5, anchor=CENTER)
        self.go_button.bind('<Button-1>', self.run_work_time)

        ## Threading 

        self.check = threading.Thread(target=self.running_check)
        self.check.start()

    def set_time_window(self, event):
        """
        Create a set-time window, where the user can input two integers: the time to rest
        and the time to work.

        Receive: the click button event.
        Return: nothing.
        """
        
        ## Set time window configuration
        
        self.time_window = Toplevel()
        self.time_window.title('Time')
        self.time_window.minsize(width=TIME_WINDOW_WIDTH, height=TIME_WINDOW_HEIGHT)
        self.time_window.maxsize(width=TIME_WINDOW_WIDTH, height=TIME_WINDOW_HEIGHT)

        ## time to work entry

        self.work_time_label = ttk.Label(self.time_window, text='Minutes you want to spend working:')
        self.work_time_label.place(x=20, y=30)
        self.work_time_entry = ttk.Entry(self.time_window, width=5)
        self.work_time_entry.place(x=265, y=30)

        ## time to rest entry

        self.rest_time_label = ttk.Label(self.time_window, text='Minutes you want to spend resting: ')
        self.rest_time_label.place(x=20, y=90)
        self.rest_time_entry = ttk.Entry(self.time_window, width=5)
        self.rest_time_entry.place(x=265, y=90)

        ## Apply button

        self.apply_button = ttk.Button(self.time_window, text='Apply', width=5)
        self.apply_button.place(x=175,y=150)
        self.apply_button.bind('<Button-1>', self.save_time)

    def save_time(self, event):
        """
        Saves the time inputed by the user on the Set Time window.

        Receive: the click button event.
        Return: nothing.
        """

        ## Get the work time and the rest time

        work_time = self.work_time_entry.get()
        rest_time = self.rest_time_entry.get()
        
        ### ERROR MESSAGES

        if (work_time == '') or (rest_time == ''):
            self.error_label = ttk.Label(self.time_window, text= 'Fill all fields!').place(x=160, y=120)
        elif (not work_time.isdigit()) or (not rest_time.isdigit()):
            self.error_label = ttk.Label(self.time_window, text= 'Only integers!').place(x=160, y=120)

        ### in case everything is ok
           
        else:
            self.times = [int(work_time)*60, int(rest_time)*60] # save the time in seconds
            self.times_backup = (int(work_time)*60, int(rest_time)*60) # store the intial values to restart the time
            self.work_time = self.seconds_to_string(self.times[0])
            self.display.config(text=self.work_time) # updates the display with the 'work time'
            self.time_window.destroy() 
            self.root.update()

    def run_work_time(self, event):
        """
        Starts the work time on the Pomodoro Clock.

        Receive: button click event.
        Return: nothing.
        """

        if self.times[0] >= 0:
            self.is_running = True # tells the other thread that the time is running
            self.message.config(text='Time to work!')
            work_time = self.times[0]
            self.times[0] -= 1 # reduce 1 second on the count  
            work_time_string = self.seconds_to_string(work_time)
            self.display.config(text=work_time_string)
            if not self.pause_signal:
                self.display.after(1000, lambda event=event: self.run_work_time(event))
                self.go_button_event = event
            else:
                self.is_running = False
        else:
            self.times[1] = self.times_backup[1]
            time.sleep(1) # time to play a sound
            self.run_rest_time() # Start the time to rest

    def run_rest_time(self):
        """
        Starts the rest time on the Pomodoro clock.

        Receive: nothing.
        Return: nothing.
        """

        if self.times[1] >= 0:
            self.is_running = True # tells the other thread that the time is running
            self.message.config(text='Time to rest. Take a break!')
            rest_time = self.times[1]
            self.times[1] -= 1 # reduce 1 second on the count  
            rest_time_string = self.seconds_to_string(rest_time)
            self.display.config(text=rest_time_string)
            self.display.after(1000, self.run_rest_time)
        else:
            self.times[0] = self.times_backup[0]
            time.sleep(1) # time to play a sound
            self.run_work_time(self.go_button_event) # starts, again, the time to work

    def pause_time(self, event):
        """
        Send a signal to pause the timer.

        Receive: button click event.
        Return: nothing.
        """

        self.pause_signal = True

    def seconds_to_string(self, seconds):
        """
        Converts seconds (integer) into the MM:SS format.

        Receive: Integers that represent the seconds.
        Return: a string that represents the time in the MM:SS format.
        """

        minute, second = divmod(seconds, 60)
        time_string = f'{minute:02d}:{second:02d}'

        return time_string

    def running_check(self):
        """
        Checks if the time is running. If it is, changes the "Go!" button to "Pause" button.

        Receive: nothing.
        Return: nothing.
        """

        while True:
            if self.is_running:
                self.go_button.config(text='Pause', width=5)
                self.go_button.bind('<Button-1>', self.pause_time)
            else:
                self.go_button.config(text='Go!', width=3)
                self.go_button.bind('<Button-1>', self.run_work_time)
                self.pause_signal = False
            time.sleep(0.1) 

def main():
    root = Tk()
    style = ttk.Style(root)
    style.theme_use('clam')
    pomodoro_clock = Pomodoro(root)
    root.mainloop()

if __name__ == '__main__':
    main()
