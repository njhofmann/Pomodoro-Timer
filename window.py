import tkinter as tk
from tkinter.font import Font


class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        # Fonts for different labels and buttons
        self.font = tk.font.Font(family="Helvetica", size=50)
        self.button_font = tk.font.Font(family="Helvetica", size=10, weight="bold")
        self.status_font = tk.font.Font(family="Helvetica", size=12, weight="bold")

        # Placeholders
        self.is_working = "Work!"
        self.state = False  # False if timer is paused, True if timer should be running
        self.mins = 25
        self.secs = 0

        # Dummy label for spacing
        self.placeholder = tk.Label(master, height=3)
        self.placeholder.grid(row=0)

        # Tells if someone should be working or on break
        self.status = tk.Label(master, textvariable="", font=self.status_font)
        self.status.config(text="Press Start")
        self.status.grid(row=1, column=1)

        # Displays the time left in any mode in "00:00" format
        self.display = tk.Label(master, height=3, textvariable="", font=self.font)
        self.display.config(text='{:02} : {:02}'.format(self.mins, self.secs))
        self.display.grid(row=2, column=0, columnspan=3)

        # Button to start timer
        self.start_button = tk.Button(master, bg="Green", activebackground="Dark Green", text="Start", width=13,
                                      height=5, font=self.button_font, command=self.start)
        self.start_button.grid(row=3, column=0)

        # Button to pause the timer
        self.pause_button = tk.Button(master, bg="Red", activebackground="Dark Red", text="Pause", width=13,
                                      height=5, font=self.button_font, command=self.pause)
        self.pause_button.grid(row=3, column=1)

        # Button to reset the timer to starting time
        self.restart_button = tk.Button(master, bg="Yellow", activebackground="Gold", text="Restart", width=13,
                                        height=5, font=self.button_font, command=self.restart)
        self.restart_button.grid(row=3, column=2)

        self.countdown()

    # Checks if the Timer should be running or not
    # Displays a clock starting at min:sec to 00:00, ex: 25:00 -> 00:00"""
    def countdown(self):
        if self.state:
            if (self.mins == 0) and (self.secs == 0):  # When timer gets to 00:00, switches modes
                self.display.config(text="Done!")
                self.status.config(text="")
                self.master.after(5000, self.change_is_working)
            else:  # Takes 1 second away from current time
                self.display.config(text='{:02} : {:02}'.format(self.mins, self.secs))
                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1
                self.master.after(1000, self.countdown)
        else:
            self.master.after(1, self.countdown)

    # If timer is paused, starts timer
    def start(self):
        if not self.state:
            self.state = True
            self.status.config(text=self.is_working)

    # If timer is running, pauses timer
    def pause(self):
        if self.state:
            self.state = False
            self.status.config(text="Paused")

    # Resets timer back to default starting time
    def restart(self):
        self.mins = 25
        self.secs = 0
        self.display.config(text='{:02} : {:02}'.format(self.mins, self.secs))
        self.state = False

    # Changes between "Work" and "Break" modes
    def change_is_working(self):
        if self.is_working == "Work!":
            self.is_working = "Break!"
            self.mins = 5
            self.secs = 0
            self.status.config(text=self.is_working)
            self.countdown()
        else:
            self.is_working = "Break!"
            self.mins = 25
            self.secs = 0
            self.status.config(text=self.is_working)
            self.countdown()


if __name__ == '__main__':
    root = tk.Tk()
    my_timer = Timer(root)
    root.mainloop()
