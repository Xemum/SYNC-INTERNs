# Import Required Library
import tkinter as tk
import datetime
import time
from threading import Thread
import os

# Create Object
root = tk.Tk()

# Set geometry
root.geometry("400x200")

# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            os.system("afplay '/Users/youcefs/Desktop/Alarm-Clock Sound!!!.mp3'")


# Add Labels, Frame, Button, Optionmenus
tk.Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
tk.Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()
frame = tk.Frame(root)
frame.pack()

hour = tk.StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
hrs = tk.OptionMenu(frame, hour, *hours)
hrs.pack(side=tk.LEFT)

minute = tk.StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
mins = tk.OptionMenu(frame, minute, *minutes)
mins.pack(side=tk.LEFT)

second = tk.StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
secs = tk.OptionMenu(frame, second, *seconds)
secs.pack(side=tk.LEFT)

tk.Button(root, text="Set Alarm", font=("Helvetica", 15), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
