import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*10))
    name = '{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take ScreenShot",
    command = screenshot
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text = "Exit",
    command = quit
)
close.pack(side=tk.LEFT)

root.mainloop()