import keyboard
from PIL import ImageGrab
import time
import pyautogui
import mouse
from pynput.mouse import Listener
from pynput.mouse import Button, Controller
#import PYGLET

# 关键字 函数名(传递的参数):
def screen():
    #'''保存截图'''
    print('代码执行到这里了')
    #keyboard.wait(hotkey='ctrl+alt+a')
    #print('我按了ctrl+alt+a键')
    keyboard.wait(hotkey='enter')
    print('我按了enter键')
    #pyautogui.press('o', 'i')
    #pyautogui.hotkey('c', 's', 'e')
    # left click
    #mouse.click('x')
    #time.sleep(0.5)



    #mouse = Controller()


    #mouse.click(Button.x1)     # 鼠标下侧键(靠近手腕和拱起方向); 后退返回
    #time.sleep(1)
    #mouse.click(Button.x2)      # 鼠标上侧键(靠近手指和线缆方向); 前进
    #time.sleep(1)


    #mouse.wheel(1)  # scroll up
    pyautogui.scroll(500)
    pyautogui.alert(text='提示信息', title='窗口标题', button='按钮标题')


screen()
