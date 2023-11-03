import datetime
import tkinter
import playsound
import time
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from threading import *
clock = Tk()
clock.geometry("450x250")
clock.title("Alarm Clock")
def Threading():
    t1 = Thread(target=alarm)
    t1.start()
def alarm():
    set_hour = hour.get()
    set_minute = minute.get()
    set_second = second.get()
    set_alarm_time = f"{set_hour}:{set_minute}:{set_second}"
    messagebox.showinfo("Alarm Clock",
                        f"Timer is set for {set_hour} : {set_minute} : {set_second} ")
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Alarm Time")
            playsound.playsound("alarm.mp3")
            messagebox.showinfo("Alarm Clock", "Time to Wake up")
            break
lc = Label(clock, text="Alarm Clock", font=("Arial", 20, "bold"), fg="red", pady=20)
lc.pack(pady=10)
ls = Label(clock, text="Set Time", font=("Arial", 15, "bold"), pady=20)
ls.pack()
fm = Frame(clock)
fm.pack(pady=20)
hour = StringVar(clock)
minute = StringVar(clock)
second = StringVar(clock)
hours = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20", "21", "22", "23", "24")
minutes = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39","40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
seconds = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39","40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
Label(fm, text="Hour:", font=("Arial", 12)).pack(side=LEFT)
hours_menu = OptionMenu(fm, hour, *hours)
hours_menu.pack(side=LEFT)
Label(fm, text="Minute:", font=("Arial", 12)).pack(side=LEFT)
minutes_menu = OptionMenu(fm, minute, *minutes)
minutes_menu.pack(side=LEFT)
Label(fm, text="Second:", font=("Arial", 12)).pack(side=LEFT)
seconds_menu = OptionMenu(fm, second, *seconds)
seconds_menu.pack(side=LEFT)
Button(clock, text="Set Alarm", font=("Arial", 10, "bold"), fg="blue", command=Threading).place(x=180, y=200)
clock.mainloop()
