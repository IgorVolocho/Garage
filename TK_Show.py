import tkinter.ttk
from tkinter import *
import sqlite_BD as sm


def new_person():
    def clicked():
        info = []
        info.append(str(txt.get()))
        info.append(int(txt1.get()))
        info.append(str(txt2.get()))
        info.append(str(txt3.get()))
        info = tuple(info)
        sm.add_person(info)
        for object in [lbl, txt, lbl1, txt1, lbl2, txt2, lbl3, txt3, btn]:
            object.destroy()
        lbll = Label(window1, text="Водитель успешно добавлен")
        lbll.grid(column=0, row=0)
        butt = Button(window1, text="Выйти", command=window1.destroy)
        butt.grid(column=0, row=1)
    window1 = Tk()
    window1.title("Добавление водителя")
    window1.geometry('400x250')
    lbl = Label(window1, text="ФИО")
    lbl.grid(column=0, row=0)
    txt = Entry(window1, width=20,)
    txt.grid(column=1, row=0)
    lbl1 = Label(window1, text="Возраст")
    lbl1.grid(column=0, row=1)
    txt1 = Entry(window1, width=20)
    txt1.grid(column=1, row=1)
    lbl2 = Label(window1, text="Дата рождения")
    lbl2.grid(column=0, row=2)
    txt2 = Entry(window1, width=20)
    txt2.grid(column=1, row=2)
    lbl3 = Label(window1, text="Машина")
    lbl3.grid(column=0, row=3)
    txt3 = Entry(window1, width=20)
    txt3.grid(column=1, row=3)
    btn = Button(window1, text="Клик!", command=clicked)
    btn.grid(column=2, row=3)
    window.mainloop()


def new_car():
    def clicked():
        info = []
        info.append(str(txt.get()))
        info.append(str(txt1.get()))
        info = tuple(info)
        sm.add_car(info)
        for object in [lbl, txt, lbl1, txt1, btn]:
            object.destroy()
        lbll = Label(window1, text="Машина успешно добавлена")
        lbll.grid(column=0, row=0)
        butt = Button(window1, text="Выйти", command=window1.destroy)
        butt.grid(column=0, row=1)
    window1 = Tk()
    window1.title("Добавление машины")
    window1.geometry('400x250')
    lbl = Label(window1, text="Машина")
    lbl.grid(column=0, row=0)
    txt = Entry(window1, width=10)
    txt.grid(column=1, row=0)
    lbl1 = Label(window1, text="Номер")
    lbl1.grid(column=0, row=1)
    txt1 = Entry(window1, width=10)
    txt1.grid(column=1, row=1)
    btn = Button(window1, text="Клик!", command=clicked)
    btn.grid(column=2, row=2)
    window.mainloop()


def show_people():
    #but1.destroy()
    combo = tkinter.ttk.Combobox(window)
    result = sm.show_people()
    names = []
    for res in result:
        names.append(res[0])
    names = list(names)
    if len(names) == 0:
        text = Label(window, text='Список пуст')
        text.grid(column=0, row=1)
    else:
        combo['values'] = names
        combo.current(0)  # По умолчанию
        combo.grid(column=0, row=1)


def show_cars():
    #but1.destroy()
    combo = tkinter.ttk.Combobox(window)
    result = sm.show_cars()
    cars = []
    for res in result:
        cars.append(res[0])
    cars = list(cars)
    if len(cars) == 0:
        text = Label(window, text='Список пуст')
        text.grid(column=1, row=1)
    else:
        combo['values'] = cars
        combo.current(0)  # По умолчанию
        combo.grid(column=1, row=1)




window = Tk()
window.title("Гараж")
window.geometry('750x500')
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Добавление водителя', command=new_person)
new_item.add_separator()
new_item.add_command(label='Добавление машины', command=new_car)
new_item.add_separator()
new_item.add_command(label='Удаление водителя')
new_item.add_separator()
new_item.add_command(label='Удаление машины')
menu.add_cascade(label='Файл', menu=new_item)
but1 = Button(window, text="Список водителей", command=show_people, width=20, height=2)
but1.grid(column=0, row=0)
but2 = Button(window, text="Список машин", command=show_cars, width=20, height=2)
but2.grid(column=1, row=0)
window.config(menu=menu)
window.mainloop()