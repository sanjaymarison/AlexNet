import os
import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
from pynput.keyboard import Controller, Key
from PIL import Image
import time
import random

keyboard = Controller()

def open_simulator(path="C:\\Users\\sanja\\Documents\\Unreal Projects\\CityScape\\Packaged\\Windows\\CityScape.exe"):
    os.startfile(path)



def get_unreal_bbox(title_keyword="CityScape (64-bit Development PCD3D_SM6) "):
    windows = gw.getWindowsWithTitle(title_keyword)
    if not windows:
        return None
    win = windows[0]
    if not win.isActive:
        win.activate()
    return (win.left, win.top, win.width, win.height)


def get_unreal_frame(bbox):
    screenshot = pyautogui.screenshot(region=bbox)
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return frame
'''
def is_path_clear(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)

    h, w = edges.shape
    center = edges[h//2:h//2+50, w//2-50:w//2+50]
    obstacle_density = np.mean(center)

    cv2.rectangle(edges, (w//2-50, h//2), (w//2+50, h//2+50), 255, 2)
    cv2.imshow("Edges", edges)

    return obstacle_density < 10 
'''

def move(key, duration=0.3):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def world_model_loop():
    bbox = get_unreal_bbox()
    if bbox is None:
        print("Unreal window not found.")
        try:
            open_simulator()
        except:
            return

    print("Starting robot control loop. Press ESC in the window to exit.")

    try:
        while True:
            frame = get_unreal_frame(bbox)
            if frame is None:
                continue

            #cv2.imshow("Unreal View", frame)

            

    finally:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    world_model_loop()

