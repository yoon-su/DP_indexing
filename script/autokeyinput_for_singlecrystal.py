from pynput.keyboard import Key, Controller
import time
time.sleep(3)

keyboard = Controller()
for i in range(360):

    for j in range(360):
        keyboard.press(Key.alt)
        keyboard.release(Key.alt)
        time.sleep(0.5)
        keyboard.press("f")
        keyboard.release("f")
        time.sleep(0.5)
        keyboard.press("e")
        keyboard.release("e")
        time.sleep(0.5)
        keyboard.press("p")
        keyboard.release("p")
        time.sleep(0.5)
        for title in f"_{i}_{j}_":
            keyboard.type(title)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
        for l in range(10):
            keyboard.press(Key.up)
            keyboard.release(Key.up)

    for k in range(10):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
