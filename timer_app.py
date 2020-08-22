import tkinter as tk
from tkinter import messagebox
import datetime


class TimerApp(tk.Tk):
    def __init__(self):
        self.s = int(60 * float(input("input minute:")))
        tk.Tk.__init__(self)
        self.title("{}m {}s".format(self.s // 60, self.s % 60))
        self.geometry("150x30")
        self.label = tk.Label(self, text="", width=10)
        self.time_end = (
            datetime.datetime.now() + datetime.timedelta(seconds=self.s)
        ).strftime("%I:%M %p")
        self.label.pack()
        self.remaining = 0
        self.countdown(self.s)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            messagebox.showerror(
                title="time is up",
                message="time is up for {}m {}s".format(self.s // 60, self.s % 60),
            )
            self.label.configure(text="time's up!")
        else:

            self.label.configure(
                text="{}m {}s \n-> {}".format(
                    self.remaining // 60, self.remaining % 60, self.time_end
                )
            )
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)


if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()
