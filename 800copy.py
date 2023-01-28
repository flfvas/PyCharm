import tkinter
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText


# 鼠标滚轮事件处理函数，绑定到Ctrl+鼠标滚轮事件
def onMouseWheel(event):
    if event.delta > 0:
        # 向上滚动，增大字号
        print("00")
    else:
        # 向下滚动，减小字号
        print("99")

for i in range(9):
    onMouseWheel()