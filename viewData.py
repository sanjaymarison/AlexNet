import numpy as np
import cv2
import time
import os

file_options = [f for f in ['training_data.npy', 'balanced_data.npy'] if os.path.isfile(f)]

if not file_options:
    print("No .npy data files found in the current directory.")
    exit(1)

print("Available data files:")
for idx, fname in enumerate(file_options):
    print(f"{idx + 1}: {fname}")

while True:
    try:
        choice = int(input(f"Select a file to view (1-{len(file_options)}): "))
        if 1 <= choice <= len(file_options):
            file_name = file_options[choice - 1]
            break
        else:
            print("Invalid selection. Try again.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    print("Loading data...")
    data = np.load(file_name, allow_pickle=True)

    print(f"Total samples loaded: {len(data)}")
    print("Press 'n' for next image, 'q' to quit.")

    index = 0
    while index < len(data):
        screen, output = data[index]

        # Show image
        cv2.imshow('Screen', screen)
        print(f"Sample {index + 1}/{len(data)} - Output: {output}")

        key = cv2.waitKey(0) & 0xFF

        if key == ord('n'):  # Next sample
            index += 1
        elif key == ord('q'):  # Quit
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
