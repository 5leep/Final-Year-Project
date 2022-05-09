import time
import tkinter as tk
import tkinter.font as font
from datetime import date, datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import db


class App(tk.Tk):
    def __init__(self, userDataBase, timerDataBase):
        super().__init__()

        # Begin "loop" of interface:
        self.title('FETT - Focus Enhancement and Tracking Tool')
        self.iconbitmap('media/fet.ico')

        # Designate height and width of app:
        appWidth = 1300
        appHeight = 700

        # Get screen width and height:
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        # Create x and y coordinates for window centering:
        x = (screenWidth / 2) - (appWidth / 2)
        y = (screenHeight / 2) - (appHeight / 2)

        # Formulae for centering window:
        self.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

        # Setting DataBase
        self.userDB = userDataBase
        self.timeDB = timerDataBase

        # Configuring Rows and Columns for window
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Notebook init:
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="snew")

        # Configuring Rows and Columns for Notebook
        self.notebook.rowconfigure(0, weight=1)
        self.notebook.columnconfigure(0, weight=1)
        # Preliminary variables:
        self.today = date.today()
        self.date = [self.today.strftime("%B %d, %Y")]
        self.terminate = 0

        # Print date:
        print("Today is:")
        print(self.date)

        # Creating tabs:
        self.tab1 = Frame(self.notebook, bg="#333333")
        self.tab2 = Frame(self.notebook, bg="#807c74")
        self.tab3 = Frame(self.notebook, bg="#707c74")
        self.tab4 = Frame(self.notebook, bg="#ffffff")

        # Placing tabs with grid:
        self.tab1.grid(row=0, column=0, sticky="snew")
        self.tab2.grid(row=0, column=0, sticky="snew")
        self.tab3.grid(row=0, column=0, sticky="snew")
        self.tab4.grid(row=0, column=0, sticky="snew")

        # Configuring rows and Columns in all tabs
        self.tab1.rowconfigure(0, weight=1)
        self.tab1.columnconfigure(0, weight=1)
        self.tab2.rowconfigure(0, weight=1)
        self.tab2.columnconfigure(0, weight=1)
        self.tab3.rowconfigure(0, weight=1)
        self.tab3.columnconfigure(0, weight=1)
        self.tab4.rowconfigure(0, weight=1)
        self.tab4.columnconfigure(0, weight=1)

        # Adding tabs, allowing functionality and title:
        self.notebook.add(self.tab1, text="Registration")
        self.notebook.add(self.tab2, text="Login")
        self.notebook.add(self.tab3, text="Timer")
        self.notebook.add(self.tab4, text="Statistics")
        self.notebook.hide(self.tab3)
        self.notebook.hide(self.tab4)

        # Adding Frames in all tabs
        self.frame1 = Frame(self.tab1, bg="#333333")
        self.frame1.grid(row=0, column=0, sticky="snew", padx=(20, 20), pady=(20, 150))
        self.frame2 = Frame(self.tab2, bg="#807c74")
        self.frame2.grid(row=0, column=0, sticky="snew", padx=(20, 20), pady=(20, 100))
        self.frame3 = Frame(self.tab3, bg="#707c74")
        self.frame3.grid(row=0, column=0, sticky="snew", padx=(20, 20))
        self.frame4 = Frame(self.tab4, bg="#ffffff")
        self.frame4.grid(row=0, column=0, sticky="snew", pady=(100, 0))
        self.frame4.rowconfigure(0, weight=1)
        self.frame4.rowconfigure(1, weight=1)
        self.frame4.columnconfigure(0, weight=1)
        # Setting up fonts:
        self.buttonFont2 = font.Font(family='Helvetica', size=10)
        self.timerFont1 = font.Font(family='Calibri', size=40, weight='bold')
        self.userFont1 = font.Font(family='Helvetica', size=25, weight='bold')

        # Setting images for buttons and labels:
        self.startButton = PhotoImage(file='media/Start_btn.png')
        self.stopButton = PhotoImage(file='media/Stop_btn.png')
        self.thirtyMinButton = PhotoImage(file='media/30mins_btn.png')
        self.oneHourButton = PhotoImage(file='media/1hour_btn.png')
        self.pomodoroButton = PhotoImage(file='media/Pomodoro_btn.png')
        self.customButton = PhotoImage(file='media/Custom_btn.png')
        self.baseLabel = PhotoImage(file='media/base.png')
        self.exitButton = PhotoImage(file='media/exit_btn.png')
        self.nextButton = PhotoImage(file='media/nextButton.png')

        # Configuring Rows and Columns for Registration Page
        for i in range(3):
            self.frame1.rowconfigure(i, weight=1)
        self.frame1.columnconfigure(0, weight=1)

        # User Registration Page
        Label(self.frame1, text="Enter Your Name to Register", font=self.userFont1, bg="#333333", fg="Black").grid(row=0, column=0, sticky='s')
        self.userRegister = StringVar()
        self.registerEntry = Entry(self.frame1, textvariable=self.userRegister, bd=5, relief=SUNKEN, font="Helvetica 20 bold", fg="Black")
        self.registerEntry.grid(row=1, column=0)
        Button(self.frame1, image=self.nextButton, bg="#333333", fg="Black", borderwidth=0, command=self.register).grid(row=2, column=0, sticky='n')
        self.user = self.registerEntry.get()

        # Configuring Rows and Columns for Login Page
        for i in range(4):
            self.frame2.rowconfigure(i, weight=1)
        self.frame2.columnconfigure(0, weight=1)

        # User Login Page
        Label(self.frame2, text="Please Enter Your Name", font=self.userFont1, bg="#807c74", fg="Black").grid(row=0, column=0, sticky='s')
        self.userLogin = StringVar()
        Entry(self.frame2, textvariable=self.userLogin, bd=5, relief=SUNKEN, font="Helvetica 20 bold", fg="Black").grid(row=1, column=0)
        Button(self.frame2, image=self.nextButton, bg="#807c74", fg="Black", borderwidth=0, command=self.login).grid(row=2, column=0)
        Button(self.frame2, image=self.exitButton, borderwidth=0, bg="#707c74", highlightthickness=0, bd=0, command=self.exit).grid(row=3, column=0, sticky="n")

        # Configuring Rows and Columns for Timer Page
        for i in range(3):
            self.frame3.rowconfigure(i, weight=1)

        for i in range(4):
            self.frame3.columnconfigure(i, weight=1)
        self.frame3.columnconfigure(4, weight=3)

        self.point = 0
        self.level = 0

        # Timer Page Widgets:

        Label(self.frame3, image=self.baseLabel, bg="#707c74").grid(row=0, column=1, columnspan=2)
        Button(self.frame3, image=self.startButton, command=self.start, bg="#707c74", borderwidth=0).grid(row=0, column=0)
        Button(self.frame3, image=self.stopButton, command=self.stop, bg="#707c74", borderwidth=0).grid(row=0, column=3)
        Button(self.frame3, image=self.thirtyMinButton, command=self.thirtyMin, bg="#707c74", borderwidth=0).grid(row=1, column=0)
        Button(self.frame3, image=self.oneHourButton, command=self.oneHour, bg="#707c74", borderwidth=0).grid(row=1, column=1)
        Button(self.frame3, image=self.pomodoroButton, command=self.pomodoro, bg="#707c74", borderwidth=0).grid(row=1, column=2)
        Button(self.frame3, image=self.customButton, command=self.custom, bg="#707c74", borderwidth=0).grid(row=1, column=3)
        Button(self.frame3, image=self.exitButton, bg="#707c74", borderwidth=0, command=self.exit).grid(row=2, column=1, columnspan=2)

        # Assigning variables:

        self.minute = StringVar()
        self.minute.set("00")
        self.second = StringVar()
        self.second.set("00")

        self.minuteEntry = Entry(self.frame3, width=2, font=self.timerFont1, textvariable=self.minute, fg="white", bg="#3b3838", borderwidth=0).grid(row=0, column=1, sticky="E", padx=15)
        self.secondEntry = Entry(self.frame3, width=2, font=self.timerFont1, textvariable=self.second, fg="white", bg="#3b3838", borderwidth=0).grid(row=0, column=2, sticky="W", padx=15)
        Label(self.frame3, text=":", fg="#ffffff", bg="#3b3838", font=self.timerFont1).grid(row=0, column=1, columnspan=2, pady=(0, 8))

        self.pointsFrame = Frame(self.frame3, bg="#707c74", highlightbackground="#000000", highlightthickness=2)
        self.pointsFrame.grid(row=0, column=4, rowspan=3, sticky="snew", pady=(80, 80))

        # Configuring Rows and Columns for Points Frame:

        for i in range(4):
            self.pointsFrame.rowconfigure(i, weight=1)
        self.pointsFrame.columnconfigure(0, weight=1)

        Label(self.pointsFrame, text="Points", fg="#000000", bg="#707c74", font=self.timerFont1).grid(row=0, column=0, sticky='s')
        Label(self.pointsFrame, text=self.point, fg="#000000", bg="#707c74", font=self.timerFont1).grid(row=1, column=0, sticky='n')
        Label(self.pointsFrame, text="Level", fg="#000000", bg="#707c74", font=self.timerFont1).grid(row=2, column=0, sticky='s')
        Label(self.pointsFrame, text=self.level, fg="#000000", bg="#707c74", font=self.timerFont1).grid(row=3, column=0, sticky='n')

        # Statistics Page Widgets
        self.figure, (self.points_ax, self.time_spent_ax) = plt.subplots(1, 2)

    # -----------------FUNCTIONS-----------------------

    # Register Function

    def register(self):
        self.user = self.userRegister.get()
        try:
            self.userDB.insert_user(self.user)
            self.notebook.select(self.tab2)
        except:
            messagebox.showerror("ERROR", "USER ALREADY EXISTS")

    # Login Function

    def login(self):
        self.user = self.userLogin.get()
        for users in self.userDB.list_user():
            if str(self.user) == str(users[1]):
                break
        else:
            messagebox.showerror("ERROR", "INVALID USER")
            return
        self.notebook.add(self.tab3)
        self.notebook.add(self.tab4)
        self.notebook.select(self.tab3)
        self.plot_data()

    # Start function

    def start(self):
        self.initial_time = time.time()
        self.terminate = 0
        try:
            # the input provided by the user is
            # stored in here :self.temp
            self.temp = int(self.minute.get()) * 60 + int(self.second.get())
        except:
            print("Please input the right value")

        self.time_incremented = 0
        self.time_assign = self.temp

        while self.temp > -1 or self.time_incremented <= self.temp:

            self.final_time = time.time()
            self.time_spent = self.final_time - self.initial_time
            # divmod(first value = self.temp//60, second value = self.temp%60)
            self.mins, self.secs = divmod(self.temp, 60)
            # Converting the input entered in mins or secs
            # mins ,secs(input = 110 min --> 120*60 = 6600:
            # 50min: 0sec)
            if self.mins > 60:
                # divmod(first value = self.temp//60, second value
                # = self.temp%60)
                self.hours, self.mins = divmod(self.mins, 60)

            # using format () method to store the value up to 2 decimal places:

            self.minute.set("{0:2d}".format(self.mins))
            self.second.set("{0:2d}".format(self.secs))

            # updating the GUI window after decrementing the self.temp value every time:

            try:
                self.update()
            except:
                self.temp = -1
            time.sleep(1)

            if self.terminate == 1:
                self.mins, self.secs, self.hours = 0, 0, 0
                self.mins, self.secs = divmod(self.time_spent, 60)
                self.mins = int(self.mins)
                self.secs = int(self.secs)
                messagebox.showinfo("FETT", "You have stopped the timer!")
                self.minute.set("00")
                self.second.set("00")
                self.userId = self.userDB.get_user_id(self.user)
                self.currentDate = datetime.now().strftime("%Y-%m-%d")
                self.level = 0
                points = 0
                self.timeDB.insert_record(
                    self.userId, self.currentDate, points, self.time_spent, self.level)
                self.allPoints, self.allTimeSpent, self.allDates = self.timeDB.get_users_stats(
                    self.userId)
                self.figure.clear()
                self.figure = None
                self.points_ax.clear()
                self.points_ax = None
                self.time_spent_ax.clear()
                self.time_spent_ax = None
                self.plot_data()

                return

            # After every second the value of self.temp will be decremented by one:

            if self.temp == 0:
                self.mins, self.secs, self.hours = 0, 0, 0
                self.mins, self.secs = divmod(self.time_spent, 60)
                self.mins = int(self.mins)
                self.secs = int(self.secs)
                messagebox.showinfo("FETT", "Time's up")
                self.minute.set("00")
                self.second.set("00")
                if self.mins > 60:
                    self.hours, self.mins = divmod(self.mins, 60)
                    self.hours = int(self.secs)
                print(f"You spent {self.hours}:{self.mins}:{self.secs}")

                self.minute.set("00")
                self.second.set("00")
                points = 0
                levels = 0
                temp1 = self.time_assign
                print(temp1)
                while temp1 >= 59:
                    temp1 -= 60
                    points += 1
                self.point += points
                temp = self.point
                while temp > 59:
                    self.level += 1
                    temp -= 60
                self.changePoints()
                self.userId = self.userDB.get_user_id(self.user)
                self.currentDate = datetime.now().strftime("%Y-%m-%d")
                self.timeDB.insert_record(
                    self.userId, self.currentDate, points, self.time_spent, self.level)
                self.allPoints, self.allTimeSpent, self.allDates = self.timeDB.get_users_stats(
                    self.userId)
                self.figure.clear()
                self.figure = None
                self.points_ax.clear()
                self.points_ax = None
                self.time_spent_ax.clear()
                self.time_spent_ax = None
                self.plot_data()
                return

            # Incrementing level every 60 self.point:
            self.temp -= 1
            self.time_incremented += 1

    def changePoints(self):
        Label(self.pointsFrame, text=self.point, fg="#000000", bg="#707c74", font=self.timerFont1).grid(row=1, column=0, sticky='n')
        Label(self.pointsFrame, text=self.level, fg="#000000", bg="#707c74", font=self.timerFont1).grid(row=3, column=0, sticky='n')

    def stop(self):
        self.terminate = 1

    def thirtyMin(self):
        self.minute.set("30")
        self.second.set("00")

    def oneHour(self):
        self.minute.set("60")
        self.second.set("00")

    def pomodoro(self):
        self.minute.set("25")
        self.second.set("00")

    def custom(self):
        self.minute.set("15")
        self.second.set("00")
        messagebox.showinfo(
            "Enter Time", "Please Set You Timer In The Clock, Thank you!")

    def exit(self):
        self.destroy()

    def plot_points(self, df, axes):
        axes.plot(df['points'])

        # Change the tick interval
        axes.xaxis.set_major_locator(mdates.DayLocator(interval=5))

        # Puts x-axis labels on an angle
        axes.xaxis.set_tick_params(rotation=5)
        axes.set_xlabel("Date")
        axes.set_ylabel("Points")

    def plot_time_spent(self, df, axes):
        axes.plot(df['time_spent'])

        # Change the tick interval
        axes.xaxis.set_major_locator(mdates.DayLocator(interval=5))

        # Puts x-axis labels on an angle
        axes.xaxis.set_tick_params(rotation=5)
        axes.set_xlabel("Date")
        axes.set_ylabel("Time Spent")

    def groupData(self, key, value):
        vote_dict = {}

        for index, j in enumerate(key):
            if j in vote_dict:
                vote_dict[j] += value[index]
            else:
                vote_dict[j] = value[index]

        myList = sorted(vote_dict.items())
        x, y = zip(*myList)
        return x, y

    def plot_data(self):
        print(self.user)
        print(self.userDB.get_user_id(self.user))

        new_df = pd.read_sql(
            f"SELECT SUM(time_spent) as time_spent, SUM(points) as points, dateAdded FROM TimerRecord WHERE personID = {self.userDB.get_user_id(self.user)} GROUP BY dateAdded",
            self.timeDB.conn)

        new_df = new_df.set_index('dateAdded')

        if not new_df.empty:
            self.figure, (self.points_ax,
                          self.time_spent_ax) = plt.subplots(1, 2)

            self.plot_points(new_df, self.points_ax)
            self.plot_time_spent(new_df, self.time_spent_ax)

            self.figure.tight_layout()

            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame4)
            self.canvas.draw()

            self.canvas.get_tk_widget().grid(row=0, column=0, sticky="snew")


if __name__ == "__main__":
    userDataBase = db.UsersDataBase()
    timerDatabase = db.TimerDatabase()
    app = App(userDataBase, timerDatabase)
    app.mainloop()
