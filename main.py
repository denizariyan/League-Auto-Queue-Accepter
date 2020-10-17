import cv2
import numpy as np
import pyautogui
import time

template = cv2.imread("template.png", cv2.IMREAD_GRAYSCALE)

active = True
while active:
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    location = np.where(result >= 0.9)
    time.sleep(2) # To not hog all the CPU resources while searching
    if location[0].any():
        active = False
location = np.where(result >= 0.9)
w, h = template.shape[::-1]

for pt in zip(*location[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)

pyautogui.click(location[1][0], location[0][0])
