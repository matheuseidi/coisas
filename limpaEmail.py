
# Created by Matheus Eidi
# 03/09/2018
# Last update - 03/09/2018
# 
#
# Resume: It's a robot that mark all your email's as read,so you don't have to do it manually.
# 
#
# Requisits: Python and pyautogui 
#
# Important:
#           As it uses pyautogui, it must be adpted to your screen resolution in order to work properly; (to get screen coordenates you can use the 
#           function pyautogui.position() it returns the position in pixels of your mouse actual location).
#           A tutorial to pyautogui can be easily found on the internet, do some research.
#           It is written to work on Gmail, but it can be easily adpted to work on any host.


import pyautogui as cmd
import time

# Use this 3 seconds to focus on the screen
print("Starting in 3 seconds...")
time.sleep(3)

# Put the number of pages the robot has to iterate (the number of pages your inbox have got) inside the "range"
# example: if your email has 20 pages -> range(20)
for i in range(40):

    # Here comes the coordenates of the "3 points" of Gmail where inside it has the option "mark all as read" (or similar)
    cmd.moveTo(380,210, duration=1)
    cmd.click()
    time.sleep(1)

    # Here comes the coordenates of the option "mark all as read" that has been enabled by the "3 points"
    cmd.moveTo(427,241,duration=0.1)
    cmd.click()
    print('Page', i+1, 'cleared!')

    # Here comes the coordenates of the arrow that goes to the next page of emails
    cmd.moveTo(1300, 210, duration=1)
    cmd.click()
    time.sleep(1.5)

print("All done!!!")
    
