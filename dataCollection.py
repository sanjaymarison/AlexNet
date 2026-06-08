# -*- coding: utf-8 -*-


import win32api as wapi
import time
import numpy as np
import cv2
import os
from control import get_unreal_bbox, get_unreal_frame, open_simulator

# Define the key list to monitor
keyList = ["\b"] + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\")

def key_check():
    """Returns a list of keys currently pressed."""
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def keys_to_output(keys):
    """
    Converts key presses into a multi-hot output:
    [A, W, D, S, SPACE]
    """
    output = [0, 0, 0, 0, 0]
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    elif 'S' in keys:
        output[3] = 1
    elif ' ' in keys:
        output[4] = 1
    elif 'W' in keys:
        output[1] = 1
    return output

# File to save/load training data
file_name = 'training_data.npy'

# Load or initialize training data
if os.path.isfile(file_name):
    print('File exists, loading previous data...')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('File does not exist, starting fresh...')
    training_data = []

def main():
    option = input('''
    Open Simulator:
    1) CityScape
    2) CitySample
    ''')
    if option == '1':
        open_simulator()
    elif option == '2':
        pass
    else:
        print("Invalid option")
        return

    print("Starting in:")
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print("Recording started. Press 'Q' to quit.")

    while True:
        if option == '1':
            bbox = get_unreal_bbox()
        elif option == '2':
            bbox = get_unreal_bbox(title_keyword="CitySample2 (64-bit Development PCD3D_SM6) ")
        screen = get_unreal_frame(bbox)

        # Preprocess the image
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80, 60))

        keys = key_check()
        output = keys_to_output(keys)

        training_data.append([screen, output])

        # Display frame for debugging (optional)
        # cv2.imshow("Screen", screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("Exiting and saving data...")
            break

        if len(training_data) % 500 == 0:
            print(f"Saving {len(training_data)} samples...")
            np.save(file_name, np.array(training_data, dtype=object))

    # Final save
    np.save(file_name, np.array(training_data, dtype=object))
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
