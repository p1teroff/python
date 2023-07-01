import time
import mouse
import keyboard

def stop_script(e):
    # This function will be called when 'esc' is pressed
    global booli
    booli = False

# When 'esc' is pressed, call the function stop_script
keyboard.on_press_key('esc', stop_script)

time.sleep(4)  # Wait 4 seconds before starting the script
print("Starting script...")

booli = True
while booli:
    mouse.click()
    time.sleep(0.01)