import pyautogui
import os
# 引入pynput库
from pynput import keyboard
import mouse

# 定义按键映射后的动作
def 按住放大():
    # pyautogui.scroll(1)
    # pyautogui.hotkey('ctrl', 'shift')
    # 滚轮向上滚动多少行
    #pyautogui.keyDown('ctrl')
    #pyautogui.scroll(100)
    #pyautogui.keyUp('ctrl')
    #pyautogui.keyUp('ctrl')
    pyautogui.alert('这个消息弹窗是文字+OK按钮')
    pyautogui.hotkey('ctrl', 'v')  # 粘贴
    mouse.wheel(1)  # scroll down

# 定义函数
def 快捷键():
    按住放大()


# 定义快捷键
# with keyboard.GlobalHotKeys({'<ctrl>+k':on_activate_p_0_0}) as h:
# with keyboard.GlobalHotKeys({'你定义是快捷键':激活的函数不带括号}) as h:
with keyboard.GlobalHotKeys({'<ctrl>+k': 快捷键}) as h:
    h.join()