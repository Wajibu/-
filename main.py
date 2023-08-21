"""
作者：哇叽
写代码不加备注，第二天就看不懂了
"""
import time
import tkinter
from tkinter import *
import os

def gettime():
    timestr = time.strftime("%X")
    #获取当前时间，格式为24：59
    lb.config(text=timestr)
    #把timestr的值赋予给lb中的text
    w.after(10, gettime)
    #每10毫秒返回一次
def def_dingzhi():
    global dingzhi
    if not dingzhi:
        #if dingzhi == False:
        sz[0] = sz[0][:10]+"True"
        dingzhi = bool(sz[0][10:])
    else:
        sz[0] = sz[0][:10]
        dingzhi = bool(sz[0][10:])

    a = ""
    for i in sz:
        a = a + i + "\n"
    f = open(lujing, "w+", encoding="GBK")
    f.write(a)
    f.close()
    # 保存设置文件

    w.attributes('-topmost', dingzhi)
    #修改dingzhi的是否，来改变是否顶置
def def_touming():
    global touming,lb_bg
    lb_bg = sz[5][8:]
    if not touming:
        #if touming == False:
        sz[1] = sz[1][:10]+"True"
        touming = bool(sz[1][10:])
    else:
        sz[1] = sz[1][:10]
        touming = bool(sz[1][10:])

    a = ""
    for txt in sz:
        a = a + txt + "\n"
    f = open(lujing, "w+", encoding="GBK")
    f.write(a)
    f.close()
    # 保存设置文件

    if touming:
        w.attributes('-transparentcolor',lb_bg)
        w.overrideredirect(True)
    else:
        w.attributes('-transparentcolor',"")
        w.overrideredirect(False)
    #是否透明窗口
def createContextMenu(event):
   menu.post(event.x_root, event.y_root)
   # 在鼠标右键的位置显示菜单
def def_shezhi():
    global lb_size,lb_fg,lb_bg
    #设置窗口
    sz2 = Tk()#创建窗口sz
    def def_yy():
        lb_size = e1.get()
        lb_fg = e2.get()
        lb_bg = e3.get()
        sz[3] = sz[3][:10] +lb_size
        sz[4] = sz[4][:8] + lb_fg
        sz[5] = sz[5][:8] + lb_bg

        a = ""
        for i in sz:
            a = a + i + "\n"
        f = open(lujing, "w+", encoding="GBK")
        f.write(a)
        f.close()
        # 保存设置文件
        try:
            lb.config(font=(lb_ziti, lb_size))
            lb.config(fg=lb_fg)
            lb.config(bg=lb_bg)
        except:
            cw = Tk()
            cw.title("错误提示")  # 标题
            cwts1 = tkinter.Label(cw, text="设置参数错误!", fg="red", font=("黑体", 30))
            cwts2 = tkinter.Label(cw, text="请输入正确数值并应用后", fg="red", font=("黑体", 30))
            cwts3 = tkinter.Label(cw, text="再关闭程序", fg="red", font=("黑体", 30))
            cwts1.pack()
            cwts2.pack()
            cwts3.pack()
            cw.attributes('-topmost', True)
            cw.mainloop()
        #使输入框中的数值被应用到w窗口上
    def break_sz():
        sz2.destroy()#关闭窗口
    sz2.title("设置")  # 窗口标题
    sz2.iconbitmap(os.path.split(os.path.realpath(__file__))[0] + "\\tubiao.ico")
    #设置图标
    sz2.attributes('-topmost', True)  # 是否顶置

    Label(sz2, text="字体大小").grid(row=0)#文本框1的标签
    Label(sz2, text="字体颜色").grid(row=1)#文本框2的标签
    Label(sz2, text="背景颜色").grid(row=2)#文本框3的标签
    e1 = Entry(sz2)  # 文本框1
    e2 = Entry(sz2)  # 文本框2
    e3 = Entry(sz2)  # 文本框3
    lb_size = sz[3][10:]  # lb中字体大小，更新变量
    lb_fg = sz[4][8:]  # lb变量的字体颜色，更新变量
    lb_bg = sz[5][8:]  # lb变量的背景颜色,更新变量
    e1.insert(1,lb_size)
    e2.insert(1,lb_fg)
    e3.insert(1,lb_bg)
    #预设文本框1、2、3的内容
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2,column=1)
    #确定文本框1、2、3的位置

    btn1 = Button(sz2, text="应用",command=def_yy)#创建按钮1"应用"
    btn1.grid(row=3, column=0)#确定按钮1位置
    btn2 = Button(sz2, text="取消",command=break_sz)
    #创建按钮2"取消"，按下运行break_sz
    btn2.grid(row=3, column=1)#确定按钮2位置

lujing = os.path.split(os.path.realpath(__file__))[0]+"\\shezhi.txt"
#获取当前文件地址并加上想设置文件的文件啊名

if not os.path.exists(lujing):#判断是否存在shezhi.txt,如果没有，创建并写入
    with open(lujing, "w") as f:
        f.write('''dingzhi = True
touming = 
lb_ziti = 黑体
lb_size = 80
lb_fg = #222222
lb_bg = #FFFFFF
''')
        f.close()

f = open(lujing, "r+", encoding="GBK")  # 打开文件
shezhi = f.readlines()# 读取文件
sz = [s.replace('\n', '') for s in shezhi]#去除换行符
"""
    c = []
    i = 0
    for s in shezhi:
        c.append(str(s.replace('\n', '')))
        i+=1
"""
#这是上一行代码的不简写状态的注释的 注释，上面那个绿色的是注释
try:
    dingzhi = bool(sz[0][10:])  # 是否顶置,有字符串表示为True
    touming = bool(sz[1][10:])  # 是否透明背景并隐藏窗口边框，无字符串表示为False
    lb_ziti = sz[2][10:]  # lb中的字体，目前改不了
    lb_size = sz[3][10:]  # lb中字体大小
    lb_fg = sz[4][8:]  # lb变量的字体颜色
    lb_bg = sz[5][8:]  # lb变量的背景颜色
    # 预定设置中的所有变量对应到文本里的位置
except:
    cw = Tk()
    cw.title("错误提示")#标题
    cwts1 = tkinter.Label(cw,text="设置文件错误!",fg="red",font=("黑体",30))
    cwts2 = tkinter.Label(cw,text="请尝试删除文件目录下的",fg="red",font=("黑体",30))
    cwts3 = tkinter.Label(cw,text="shezhi.txt文件,以重置设置",fg="red",font=("黑体",30))
    cwts1.pack()
    cwts2.pack()
    cwts3.pack()
    cw.attributes('-topmost', True)
    cw.mainloop()
f.close()

w = Tk()#创建窗口w
w.title('当前时间')#标题
w.iconbitmap(os.path.split(os.path.realpath(__file__))[0]+"\\7.ico")
w.attributes('-topmost', dingzhi)#是否顶置
if touming:
    #if touming == True:
    w.overrideredirect(True)
    #创建窗口时判断touming是否为True，如果是，透明标题栏
    w.attributes('-transparentcolor',lb_bg)#是否透明背景

menu = tkinter.Menu(w,tearoff=0)
#c创建与w窗口关联的菜单，不能独立为一个窗口
menu.add_command(label="是/否 顶置",command=def_dingzhi)
#给菜单添加普通的菜单项1，显示"是/否 顶置"，运行def_dingzhi
menu.add_command(label="是/否 透明背景并隐藏标题栏",command=def_touming)
#菜单选项2
menu.add_command(label="更多设置",command=def_shezhi)
#菜单选项3
w.bind("<Button-3>", createContextMenu)
#当鼠标右键被按下时运行createContextMenu
#创建右键菜单
try:
    lb = tkinter.Label(w, text='', fg=lb_fg, bg=lb_bg, font=(lb_ziti, lb_size))
    # 标签lb的样式，lb即实时时间
except:
    cw = Tk()
    cw.title("错误提示")  # 标题
    cwts1 = tkinter.Label(cw, text="设置文件错误!", fg="red", font=("黑体", 30))
    cwts2 = tkinter.Label(cw, text="请尝试删除文件目录下的", fg="red", font=("黑体", 30))
    cwts3 = tkinter.Label(cw, text="shezhi.txt文件,以重置设置", fg="red", font=("黑体", 30))
    cwts1.pack()
    cwts2.pack()
    cwts3.pack()
    cw.attributes('-topmost', True)
    cw.mainloop()
f.close()
lb.pack()#显示lb的方式
gettime()

w.mainloop()


