from PIL import ImageGrab
import time
import win32api
import win32con
import win32gui
import os
import autopy
import math
import random
import sys

def play():
    #查找窗口
    window_name=u'梦幻模拟战'
    win=win32gui.FindWindow(None,window_name)
    left, top, right, bottom = win32gui.GetWindowRect(win)
    print("left:",left)
    print("top:",top)
    print("right:",right)
    print("bottom:",bottom)
    #鼠标移动到绝对位置
    mijinglist=[1088,257]
    headImg=[62,71]
    mousemove_click(headImg)
    #autopy.mouse.click()

    win32api.SetCursorPos(headImg)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

#鼠标移动并点击
def mousemove_click(list):
     print(list[0])
     print(list[1])
     autopy.mouse.smooth_move(list[0], list[1])
     autopy.mouse.click()
     #autopy.mouse.toggle('LEFT',True)  # 按下左键
     #autopy.mouse.toggle(False)  # 松开左键

def click_position(hwd, x_position, y_position, sleep):
    long_position = win32api.MAKELONG(x_position, y_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
    time.sleep(int(sleep))


def sine_mouse_wave():
    """
    Moves the mouse in a sine wave from the left edge of
    the screen to the right.
    """
    width, height = autopy.screen.size()
    height /= 2
    height -= 10  # Stay in the screen bounds.
    TWO_PI = math.pi * 2.0
    for x in range(int(width)):
        y = int(height * math.sin((TWO_PI * x) / width) + height)
        autopy.mouse.move(x, y)
        time.sleep(random.uniform(0.001, 0.003))

if __name__ == '__main__':
    #sine_mouse_wave()
    play()