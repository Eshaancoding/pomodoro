import time
import os
import platform

# Note: Supported on Mac, Linux, and Windows Powershell (not command prompt)

# get data + initalized variables
string_print = ""
study_time_dur = input("How long will you study for each session? (Enter in hours : min) ")
break_time_dur = input("How long will you relax for each session? (Enter in hours : min) ")
session_num = input("How many sessions will you take? (Enter an integer. You can type 'None' if you want to repeat until Ctrl+C is pressed) ")
tips = input("Any tips you would like to give? (You could type 'None' if you would not like to give a tip) ") 
string_print += "Make sure you turn up your volume so you could hear the bell! Press Ctrl + C to stop the program at any time. \n"
session_num_counter = 1
state = "Study"

# parse data
if tips != "None":
    string_print += "Tip: " + tips + "\n"

study_time_hours = int(study_time_dur.split(":")[0])
study_time_min = int(study_time_dur.split(":")[1])
break_time_hours = int(break_time_dur.split(":")[0])
break_time_min = int(break_time_dur.split(":")[1])

timer_hour = study_time_hours
timer_min = study_time_min 

if (study_time_hours == 0 and study_time_min == 0) or (break_time_hours == 0 and break_time_min == 0):
    print("Must input a valid time")
    exit(0) 

string_print += state + " session " + str(session_num_counter) + " -"

seconds = 0

while True:
    # update timer
    if seconds == -1: 
        timer_min -= 1
        seconds = 59

    if timer_min == -1: 
        timer_hour -= 1
        timer_min = 59
    
    if timer_hour == -1:
        # timer done
        if platform.system() == 'Windows':
            directory = os.getcwd() + '\\sound.wav'
            os.system("$PlayWav=New-Object System.Media.SoundPlayer")
            os.system("$PlayWav.SoundLocation='" + directory+"'")
            os.system("$PlayWav.playsync()")
        else:
            os.system("play ")


        string_print += " 00:00:00 \n"
        if state == "Study":
            state = "Break"
            timer_hour = break_time_hours
            timer_min = break_time_min
            seconds = 0
        else:
            state = "Study"
            timer_hour = study_time_hours
            timer_min = study_time_min
            seconds = 0
            session_num_counter += 1

        string_print += state + " session " + str(session_num_counter) + " -"
        if session_num != "None":
            if (session_num_counter > int(session_num)):
                print("Great job studying!")
                exit(0)

    # print everything
    if platform.system() == 'Windows':
        os.system("cls") 
    else:
        os.system("clear")

    print(string_print, end = " ")
    if seconds < 10:
        sec_string_split = ":0"
    else: 
        sec_string_split = ":"
    if timer_min < 10:
        min_string_split = ":0"
    else:
        min_string_split = ":"
    if timer_hour < 10:
        hour_string_split = "0"
    else: 
        hour_string_split = ""

    print(hour_string_split + str(timer_hour) + min_string_split + str(timer_min) + sec_string_split + str(seconds))

    # wait
    time.sleep(1)
    seconds -= 1