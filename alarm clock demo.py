# Python alarm clock
import time #the time module will help with updating the clock every second
import datetime #the datetime module will help me work with string representations of a time
import pygame #the easiest way to use sfx


def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    sound_file = "clock-alarm.mp3"
    is_running = True

    while  is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)