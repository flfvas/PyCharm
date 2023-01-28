import tkinter
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText

w, h = 480, 360
root = tkinter.Tk()
# 主窗口尺寸和初始位置
root.geometry(f'{w}x{h}+200+100')
# 不允许修改大小
root.resizable(False,False)
my_font = Font(family= 'Consolas',size=12)
stContent = ScrolledText(root,font=my_font )
text = '''学习Python的好资源'''
stContent.insert('0.0', text)
stContent.place(x=2, y=2, width=w-4, height=h-4)
# 鼠标滚轮事件处理函数，绑定到Ctrl+鼠标滚轮事件
def onMouseWheel(event):
    if event.delta > 0:
        # 向上滚动，增大字号
        my_font['size'] = my_font['size'] + 1
    else:
        # 向下滚动，减小字号
        my_font['size'] = my_font['size'] - 1
stContent.bind('<Control-MouseWheel>', onMouseWheel)

root.mainloop()
