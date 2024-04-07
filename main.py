import numpy as np
import pyautogui
import win32api
import win32con
import cv2

import keyboard

# SETTINGS
auto_aim_size = 200
step_size = 3

screenshot = pyautogui.screenshot()

screen_width, screen_height = pyautogui.size()

region_x = auto_aim_size
region_y = auto_aim_size

region = (int((screen_width/2-(region_x/2))),
          int((screen_height/2-(region_y/2))), region_x, region_y)

while True and keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=region)

    width, height = pic.size

    # Search image for pixel color
    for x in range(0, width, step_size):
        for y in range(0, height, step_size):

            r, g, b = pic.getpixel((x, y))

            if r > 140 and b < 40 and g < 40:  # Adjust color to search for here
                flag = 1

                x -= int((region_x/2))
                y -= int((region_y/2))

                print('located')

                # Over compensate to adjust for movement speed
                x *= 2
                y *= 2

                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)

                break

        if flag == 1:
            break

    # Show image
    ori_img = np.array(pic)
    ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
    cv2.imshow("ori_img", ori_img)
    cv2.waitKey(1)
