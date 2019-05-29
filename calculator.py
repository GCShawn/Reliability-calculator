
from tkinter import *
from tkinter import ttk # 导入ttk模块，因为下拉菜单控件在ttk中
import numpy as np
from tkinter import messagebox

#窗口大小
root = Tk()
root.title("calculator")
root.geometry("360x180+600+200")
#统一组件宽度
width1_set = 10

#标签设置，第一排和第三排
label1 = Label(root,text = "应力")
label1.grid(row = 0,column = 1)
label2 = Label(root,text = "强度")
label2.grid(row = 2,column = 1)

label11 = Label(root,text = "参数1")
label11.grid(row = 0,column = 2)
label12 = Label(root,text = "参数2")
label12.grid(row = 0,column = 3)
label13 = Label(root,text = "参数3")
label13.grid(row = 0,column = 4)

label21 = Label(root,text = "参数1")
label21.grid(row = 2,column = 2)
label22 = Label(root,text = "参数2")
label22.grid(row = 2,column = 3)
label23 = Label(root,text = "参数3")
label23.grid(row = 2,column = 4)

#下拉框设置
choose_type1 = ttk.Combobox(root,textvariable=StringVar(),width = width1_set,state = 'readonly')
choose_type1["values"] = ("正态分布","对数正态分布","指数分布","威布尔分布")
choose_type1.grid(row = 1,column = 1)
choose_type1.current(0)

choose_type2 = ttk.Combobox(root,textvariable=StringVar(),width = width1_set,state = 'readonly')
choose_type2["values"] = ("正态分布","对数正态分布","指数分布","威布尔分布")
choose_type2.grid(row = 3,column = 1)
choose_type2.current(0)

#输入框和输出框
entry11 = Entry(root,width = width1_set,text = 0)
entry11.grid(row = 1,column = 2)
entry11.insert(0,"0")

entry12 = Entry(root,width = width1_set,text = 1)
entry12.grid(row = 1,column = 3)
entry12.insert(0,"1")
entry13 = Entry(root,width = width1_set)
entry13.grid(row = 1,column = 4)

entry21 = Entry(root,width = width1_set)
entry21.insert(0,"0")
entry21.grid(row = 3,column = 2)
entry22 = Entry(root,width = width1_set)
entry22.insert(0,"1")
entry22.grid(row = 3,column = 3)
entry23 = Entry(root,width = width1_set)
entry23.grid(row = 3,column = 4)

entry41 = Entry(root,width = width1_set,state = 'normal')
entry41.grid(row = 4,column = 2)

#根据下拉菜单调整标签以及输入框状态
def choosing_type1(event):
    print("choosing type 1")
    if choose_type1.get() == "正态分布":
        label11["text"] = "均值μ"
        label12["text"] = "方差σ^2"
        label13["text"] = ""
        entry12["state"] = "normal"
        entry13["state"] = "disable"
    elif choose_type1.get() == "对数正态分布":
        label11["text"] = "均值μ"
        label12["text"] = "方差σ^2"
        label13["text"] = ""
        entry12["state"] = "normal"
        entry13["state"] = "disable"
    elif choose_type1.get() == "指数分布":
        label11["text"] = "参数λ"
        label12["text"] = ""
        label13["text"] = ""
        entry12["state"] = "disable"
        entry13["state"] = "disable"
    elif choose_type1.get() == "威布尔分布":
        label11["text"] = "形状参数k"
        label12["text"] = "比例参数λ"
        label13["text"] = ""
        entry12["state"] = "normal"
        entry13["state"] = "disable"

def choosing_type2(event):
    print("choosing type 2")
    if choose_type2.get() == "正态分布":
        label21["text"] = "均值μ"
        label22["text"] = "方差σ^2"
        label23["text"] = ""
        entry22["state"] = "normal"
        entry23["state"] = "disable"
    elif choose_type2.get() == "对数正态分布":
        label21["text"] = "均值μ"
        label22["text"] = "方差σ^2"
        label23["text"] = ""
        entry22["state"] = "normal"
        entry23["state"] = "disable"
    elif choose_type2.get() == "指数分布":
        label21["text"] = "参数λ"
        label22["text"] = ""
        label23["text"] = ""
        entry22["state"] = "disable"
        entry23["state"] = "disable"
    elif choose_type2.get() == "威布尔分布":
        label21["text"] = "形状参数k"
        label22["text"] = "比例参数λ"
        label23["text"] = ""
        entry22["state"] = "normal"
        entry23["state"] = "disable"

#对自带的weibull函数重定义，加上尺度参数
def Nweibull(a,scale,size):
     return scale*np.random.weibull(a,size)

#计算模块
def calculate():
    print("calculate")
    test_number = 1000

#获得四个输入框的值
    a = entry11.get()
    b = entry12.get()
    m = entry21.get()
    n = entry22.get()

#首先判断是否为空字符串，为空则弹出弹窗，不足之处是显得有点乱，应该函数封装下会比较好
    if choose_type1.get() == "正态分布":
        if (a == '')|(b == ''):
            messagebox.showinfo('提示', '请输入正态分布的两个参数')
        else:
            list_of_stress = np.random.normal(float(a),float(b),test_number)
    elif choose_type1.get() == "对数正态分布":
        if (a == '')|(b == ''):
            messagebox.showinfo('提示', '请输入对数正态分布的两个参数')
        else:
            list_of_stress = np.random.lognormal(float(a),float(b),test_number)
    elif choose_type1.get() == "指数分布":
        if (a == ''):
            messagebox.showinfo('提示', '请输入指数分布的参数')
        else:
            list_of_stress = np.random.exponential(float(a),test_number)
    elif choose_type1.get() == "威布尔分布":
        if (a == '')|(b == ''):
            messagebox.showinfo('提示', '请输入威布尔分布的两个参数')
        else:
            list_of_stress = Nweibull(float(a),float(b),test_number)


    if choose_type2.get() == "正态分布":
        if (m == '')|(n == ''):
            messagebox.showinfo('提示', '请输入正态分布的两个参数')
        else:
            list_of_strength = np.random.normal(float(m),float(n),test_number)
    elif choose_type2.get() == "对数正态分布":
        if (m == '')|(n == ''):
            messagebox.showinfo('提示', '请输入对数正态分布的两个参数')
        else:
            list_of_strength = np.random.lognormal(float(m),float(n),test_number)
    elif choose_type2.get() == "指数分布":
        if (m == ''):
            messagebox.showinfo('提示', '请输入指数分布的参数')
        else:
            list_of_strength = np.random.exponential(float(m),test_number)
    elif choose_type2.get() == "威布尔分布":
        if (m == '')|( n == ''):
            messagebox.showinfo('提示', '请输入威布尔分布的两个参数')
        else:
            list_of_strength = Nweibull(float(m),float(n),test_number)

#依次比较
    j = 0
    for i in range(test_number):
        if list_of_strength[i] >= list_of_stress[i]:
            j+=1

#输出概率
    print(j/test_number)
    entry41.delete(0,END)
    entry41.insert(0,str(j/test_number))

#设置按键命令
button1 = Button(root,width = width1_set,text = "计算",command = calculate)
button1.grid(row = 4,column = 1)

#设置下拉框命令，调整标签
choose_type1.bind("<<ComboboxSelected>>",choosing_type1)
choose_type2.bind("<<ComboboxSelected>>",choosing_type2)


mainloop()