from tkinter import *
import math as mt
import tkinter.messagebox as mb

mainwindow = Tk()
mainwindow.title("Меню")
mainwindow.geometry('150x130')


def rootcircle():
    root = Tk()
    root.title("Вичислення кола")
    root.geometry('280x180')

    def circle(a, l):
        dele = Tk()
        geo = str(a * 2 * 20+20) + 'x' + str(a * 2 * 20 + 50+20)
        dele.geometry(geo)

        def cic():
            try:
                dele.destroy()
            except:
                pass

        btnc = Button(dele, text="Закрити", command=cic)
        btnc.pack(side=BOTTOM)

        for i in range(a):
            for j in range(int(a - (i ** mt.pi / a * 0.2) / mt.sqrt(i + i + 0.01))):
                lbld = Label(dele, text=l)
                lbld.place(x=(a - j) * 20, y=(a + i) * 20)
        for i in range(a):
            for j in range(int(a - (i ** mt.pi / a * 0.2) / mt.sqrt(i + i + 0.01))):
                lbld = Label(dele, text=l)
                lbld.place(x=(a + j) * 20 + 20, y=(a + i) * 20)
        for i in range(a):
            for j in range(int(a - (i ** mt.pi / a * 0.2) / mt.sqrt(i + i + 0.01))):
                lbld = Label(dele, text=l)
                lbld.place(x=(a - j) * 20, y=(a - i) * 20 - 20)
        for i in range(a):
            for j in range(int(a - (i ** mt.pi / a * 0.2) / mt.sqrt(i + i + 0.01))):
                lbld = Label(dele, text=l)
                lbld.place(x=(a + j) * 20 + 20, y=(a - i) * 20 - 20)

    def btn1():
        if s1.get() == 1:
            l = "."
        elif s1.get() == 2:
            l = "*"
        elif s1.get() == 3:
            l = "@"
        elif s1.get() == 4:
            l = "∎"
        else:
            l = "█"

        a = int(ent.get())
        if 12 <= a <= 24:
            circle(a, l)
            try:
                non.configure(text="")
            except:
                pass
        elif a < 12:
            non.configure(text="Буде дуже малий круг :(")
        else:
            non.configure(text="Буде дуже великий круг :(")

    lbl = Label(root, text="Задайте радіус фігури від 12 до 24")
    lbl.pack()
    ent = Entry(root)
    ent.pack()
    btn = Button(root, text="Створити", command=btn1)
    btn.pack()
    non = Label(root, text="Фігура може бути дуже велика", font=("", 10))
    non.pack()
    s1 = Scale(root, from_=1, to=5, orient=HORIZONTAL, tickinterval=1)
    s1.pack()
    lbllight = Label(root, text="Яскравість фігури")
    lbllight.pack()


def rootcircle1():
    root = Tk()
    root.title("Вичислення кола")
    root.geometry('280x180')

    def circle1(a, l):
        dele = Tk()
        geo = str(a * 2 * 20) + 'x' + str(a * 2 * 20 + 50)
        dele.geometry(geo)

        def cic():
            try:
                dele.destroy()
            except:
                pass

        def line():
            linea = Tk()
            linea.geometry(geo)

            def secr():
                msg = "Куб?"
                mb.showinfo("досягнення получене", msg)
                lab = Label(mainwindow, text="🧊", font=("", 40))
                lab.pack(side=LEFT)
                lab1 = Label(mainwindow, text=": Досягнення")
                lab1.pack(side=LEFT)

            def cic1():
                try:
                    linea.destroy()
                except:
                    pass

            btncl = Button(linea, text="Закрити", command=cic1)
            btncl.pack(side=BOTTOM)

            btnsecret = Button(linea, text="3d?", command=secr)
            btnsecret.pack(side=RIGHT)

            for n in range(a * 2):
                lbld1 = Label(linea, text=l)
                lbld1.place(x=a*20, y=n * 20)

        btnc = Button(dele, text="Закрити", command=cic)
        btnc.pack(side=BOTTOM)

        btn3 = Button(dele, text="1d Квадрат", command=line)
        btn3.pack(side=BOTTOM)

        for i in range(a * 2):
            for j in range(a * 2):
                lbld = Label(dele, text=l)
                lbld.place(x=i * 20, y=j * 20)

    def btn2():
        if s1.get() == 1:
            l = "."
        elif s1.get() == 2:
            l = "*"
        elif s1.get() == 3:
            l = "@"
        elif s1.get() == 4:
            l = "∎"
        else:
            l = "█"

        a = int(ent.get())
        if a <= 24:
            circle1(a, l)
            try:
                non.configure(text="")
            except:
                pass
        else:
            non.configure(text="Буде дуже великий квадрат :(")

    lbl = Label(root, text="Задайте радіус фігури до 24")
    lbl.pack()
    ent = Entry(root)
    ent.pack()
    btn = Button(root, text="Створити", command=btn2)
    btn.pack()
    non = Label(root, text="Фігура може бути дуже велика", font=("", 10))
    non.pack()
    s1 = Scale(root, from_=1, to=5, orient=HORIZONTAL, tickinterval=1)
    s1.pack()
    lbllight = Label(root, text="Яскравість фігури")
    lbllight.pack()


btnmenu = Button(mainwindow, text="Круг", command=rootcircle)
btnmenu.pack()
btnmenu1 = Button(mainwindow, text="Квадрат", command=rootcircle1)
btnmenu1.pack()


mainwindow.mainloop()
