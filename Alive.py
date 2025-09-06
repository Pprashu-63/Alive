#import pyautogui
#import time

#interval_seconds = 60

#move_amount = 5

##try:
#    while True:
        
  #      x, y = pyautogui.position()
#
        
  #      pyautogui.moveTo(x + move_amount, y + move_amount, duration=0.25)
   #     pyautogui.moveTo(x, y, duration=0.25) 

    #    print(f"Mouse moved at {time.ctime()}")
     #   time.sleep(interval_seconds)

#except KeyboardInterrupt:
     #   print("Script terminated by user.")



import pyautogui
import time

interval_seconds = 4

try:
    while True:
        pyautogui.press("shift")  # Simulate Shift key press
        print(f"Shift pressed at {time.ctime()}")
        time.sleep(interval_seconds)
except KeyboardInterrupt:
    print("Script stopped.")
