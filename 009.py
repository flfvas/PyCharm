import pyautogui
import os
# 引入pynput库
from pynput import keyboard

# 定义按键映射后的动作
def 按住放大():
    # pyautogui.scroll(1)
    # pyautogui.hotkey('ctrl', 'shift')
    # 滚轮向上滚动多少行
    pyautogui.keyDown('ctrl')
    pyautogui.scroll(100)
    pyautogui.keyUp('ctrl')

# 定义函数
def 快捷键():
    按住放大()


# 定义快捷键
# with keyboard.GlobalHotKeys({'<ctrl>+k':on_activate_p_0_0}) as h:
# with keyboard.GlobalHotKeys({'你定义是快捷键':激活的函数不带括号}) as h:
with keyboard.GlobalHotKeys({'1': 快捷键}) as h:
    h.join()