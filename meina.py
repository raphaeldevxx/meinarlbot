import pyautogui
import time
import random

def bring_window_to_front(window_name):
    while True:
        try:
            window = pyautogui.getWindowsWithTitle(window_name)[0]
            window.activate()
            print(f"Window '{window_name}' found and brought to the front.")
            break
        except IndexError:
            print(f"Window '{window_name}' not found. Retrying in 1 second...")
            time.sleep(1)

window_name = "Rocket League"

bring_window_to_front(window_name)

print("Waiting 5 seconds to start the script...")
time.sleep(5)

print("Holding the 'W' key down permanently.")
pyautogui.keyDown('w')

next_space_press = time.time() + random.uniform(0.5, 29)

next_left_click = time.time() + random.uniform(0.01, 3)

next_w_release = time.time() + random.uniform(21, 40)

while True:
    
    print("Performing a double jump.")
    pyautogui.click(button='right')
    time.sleep(0.0000000001)
    pyautogui.click(button='right')

    wait_time = random.uniform(0.01, 2)
    print(f"Waiting {wait_time:.2f} seconds before the next double jump.")
    time.sleep(wait_time)
    
    pyautogui.keyDown('w')
    
    if time.time() >= next_space_press:
        print("Pressing the spacebar.")
        pyautogui.press('space')
        next_space_press = time.time() + random.uniform(0.5, 29)

    if time.time() >= next_left_click:
        print("Holding the left mouse button.")
        pyautogui.mouseDown(button='left')
        time.sleep(random.uniform(0.01, 3))
        pyautogui.mouseUp(button='left')
        next_left_click = time.time() + random.uniform(0.01, 3)
    
    if time.time() >= next_w_release:
        print("Releasing the 'W' key and holding the 'S' key.")
        pyautogui.keyUp('w')
        pyautogui.keyDown('s')
        s_hold_time = random.uniform(1, 7)
        print(f"Holding the 'S' key for {s_hold_time:.2f} seconds.")
        time.sleep(s_hold_time)
        pyautogui.keyUp('s')
        next_w_release = time.time() + random.uniform(21, 40)
        print("Holding the 'W' key down again.")
        pyautogui.keyDown('w')