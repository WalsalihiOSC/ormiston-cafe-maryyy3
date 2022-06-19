from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
from tkinter import ttk 




class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('680x350')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 680, height = 350)
        self.image1 = Canvas(self.w1, bg = '#dcb68a')
        self.image1.place(x = -20, y = 0, width = 700, height = 460)
        self.label1 = Label(self.w1, text = "     Ormiston Senior College Cafe\n             Ordering system", fg = "#060606", bg = "#FFFFFF", font = tkinter.font.Font(family = "Cooper Black", size = 18, weight = "normal"), cursor = "arrow", state = "normal")
        self.label1.place(x = 40, y = 20, width = 600, height = 132)
        self.button1 = Button(self.w1, text = "Start ordering!", bg = "#FFFFFF", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal",command=self.start)
        self.button1.place(x = 290, y = 180, width = 90, height = 22)
        self.button2 = Button(self.w1, text = "Exit", bg = "#FFFFFF", fg = "#040404", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal", command=self.exit)
        self.button2.place(x = 290, y = 230, width = 90, height = 22)

    def exit(self):
        self.w1.destroy()

    def start(self):
        self.w1.destroy()
        a = CafeMenu(0)
        a.w1.mainloop()
            

        
#creates class menu
class CafeMenu():
    def __init__(self, parent):
        self.gui(parent)
    #creates gui for widgets for FIRST menu page only 
    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#FFFFFF')
            self.w1.geometry('680x350')
            self.w = StringVar()
            self.americano = IntVar()
            self.cuppacino = IntVar()
            self.latte = IntVar()
            self.mocha = IntVar()
            self.espresso = IntVar()
        
            self.vtotal = IntVar()

            self.var1 = IntVar()
            self.var2 = IntVar()
            self.var3 = IntVar()
            self.var4 = IntVar()
            self.var5 = IntVar()

            self.txt = StringVar()

            
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#FFFFFF')
            self.w1.place(x = 0, y = 0, width = 680, height = 350)
        self.image1 = Canvas(self.w1, bg = '#DCB68A')
        self.image1.place(x = 0, y = 0, width = 150, height = 350)
        self.label2 = Label(self.w1, text = "Coffee ", fg = "#080808", bg = "#FFFFFF", font = tkinter.font.Font(family = "Harlow Solid Italic", size = 28), cursor = "arrow", state = "normal")
        self.label2.place(x = 170, y = 50, width = 120, height = 162)
        self.label5 = Label(self.w1, text = "Menu ", fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "Script MT Bold", size = 28, weight = "normal"), cursor = "arrow", state = "normal")
        self.label5.place(x = 320, y = 40, width = 120, height = 42)
        self.label4 = Label(self.w1, text = "$", fg = "#080808",bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14), cursor = "arrow", state = "normal")
        self.label4.place(x = 420, y = 110, width = 90, height = 22)
        
        self.radio6 = Label(self.w1, text = "3.00",  fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio6.place(x = 480, y = 150, width = 90, height = 22) 
        self.radio7 = Label(self.w1, text = "3.50", fg = "#000000", bg = "#FFFFFF",font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio7.place(x = 480, y = 170, width = 90, height = 22)
        self.radio8 = Label(self.w1, text = "4.30",  fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio8.place(x = 480, y = 190, width = 90, height = 22)
        self.radio9 = Label(self.w1, text = "4.20", fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio9.place(x = 480, y = 210, width = 90, height = 22)
        self.radio10 = Label(self.w1, text = "4.50", fg = "#000000", bg = "#FFFFFF",font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio10.place(x = 480, y = 230, width = 90, height = 22)

        
        self.check1 = Checkbutton(self.w1, text = "Americano ", fg = "#070707", bg = "#FFFFFF",  variable=self.var1, onvalue=1, offvalue=0,font = tkinter.font.Font(family = "Arial Black", size = 12, weight = "normal"), cursor = "arrow", state = "normal", command=self.check1)
        self.check1.place(x = 380, y = 148, width = 120, height = 22)
        self.check1.deselect()
        
        self.check2 = Checkbutton(self.w1, text = "Cupaccino", fg = "#070707", bg = "#FFFFFF", variable=self.var2, onvalue=1, offvalue=0,font = tkinter.font.Font(family = "Arial Black", size = 12, weight = "normal"), cursor = "arrow", state = "normal", command=self.check2)
        self.check2.place(x = 378, y = 170, width = 120, height = 22)
        self.check2.deselect()

        self.check3 = Checkbutton(self.w1, text = "Latte", fg = "#070707", bg = "#FFFFFF", variable=self.var3, onvalue=1, offvalue=0,  font = tkinter.font.Font(family = "Arial Black", size = 12, weight = "normal"), cursor = "arrow", state = "normal", command=self.check3)
        self.check3.place(x = 355, y = 190, width = 120, height = 22)
        self.check3.deselect()

        self.check4 = Checkbutton(self.w1, text = "Mocha", fg = "#070707", bg = "#FFFFFF",variable=self.var4,onvalue=1, offvalue=0, font = tkinter.font.Font(family = "Arial Black", size = 12, weight = "normal"), cursor = "arrow", state = "normal",command=self.check4)
        self.check4.place(x = 360, y = 210, width = 120, height = 22)
        self.check4.deselect()

        self.check5 = Checkbutton(self.w1, text = "Espresso", fg = "#070707", bg = "#FFFFFF", variable=self.var5,onvalue=1, offvalue=0, font = tkinter.font.Font(family = "Arial Black", size = 11, weight = "normal"), cursor = "arrow", state = "normal", command=self.check5)
        self.check5.place(x = 368, y = 230, width = 120, height = 22)
        self.check5.deselect()

        
        
        self.button3 = Button(self.w1, text = ">", bg = "#ffaa7f", fg = "#ffffff", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button3.place(x = 380, y = 310, width = 40, height = 22)
        self.button3['command'] = self.forward
        
        self.text1 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8),textvariable=self.americano, cursor = "arrow", state = NORMAL)
        self.text1.place(x = 560, y = 150, width = 50, height = 20)
        self.text2 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8),textvariable=self.cuppacino, cursor = "arrow", state = NORMAL)
        self.text2.place(x = 560, y = 170, width = 50, height = 20)
        self.text3 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8),textvariable=self.latte, cursor = "arrow", state = NORMAL)
        self.text3.place(x = 560, y = 190, width = 50, height = 20)
        self.text4 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8),textvariable=self.mocha, cursor = "arrow", state = NORMAL)
        self.text4.place(x = 560, y = 210, width = 50, height = 20)
        self.text5 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), textvariable=self.espresso, cursor = "arrow", state = NORMAL)
        self.text5.place(x = 560, y = 230, width = 50, height = 20)
        
        self.label10 = Label(self.w1, text = "Order:", fg = "#000000", bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label10.place(x = 30, y = 20, width = 90, height = 22)
        
        self.button1 = Button(self.w1, text = "Confirm Order", bg = "#FFFFFF", fg = "#090909", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button1.place(x = 30, y = 280, width = 90, height = 22)
        self.button1['command'] = self.confirm
        
        self.button2 = Button(self.w1, text = "Reset", bg = "#FFFFFF", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal", command=self.reset)
        self.button2.place(x = 30, y = 310, width = 90, height = 22)
        
        self.button2 = Button(self.w1, text = "Total", bg = "#FFFFFF", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), command = self.total, cursor = "arrow", state = "normal")
        self.button2.place(x = 170, y = 250, width = 90, height = 22)

        self.button3 = Button(self.w1, text = "Exit", bg = "#FFFFFF", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal", command=self.exit)
        self.button3.place(x = 590, y = 310, width = 50, height = 22)

        self.text3 = Entry(self.w1, bg = "#ffffff", fg = "#090909", textvariable=self.vtotal, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14, weight = "bold"), cursor = "arrow", state = "normal")
        self.text3.place(x = 170, y = 170, width = 70, height = 50)

        self.tree = Frame(self.w1, bg = "#ffffff")
        self.tree.place(x = 20, y = 50, width = 110, height = 220)
        
        

        global count
        count = 0
        count += 1

#define functions section
         
#define forward button
    def forward(self):
        self.w1.destroy()
        a = CafeMenu2(0)
        a.w1.mainloop()
        
    def confirm(self):
        self.w1.destroy()
        a = Orderpage(0)
        a.w1.mainloop()

    def reset(self):
        self.lbl1.destroy()
        self.lbl2.destroy()
        self.lbl3.destroy()
        self.lbl4.destroy()
        self.lbl5.destroy()
    
    def total(self):
        meal1 = float(self.americano.get())
        meal2 = float(self.cuppacino.get())
        meal3 = float(self.latte.get())
        meal4 = float(self.mocha.get())
        meal5 = float(self.espresso.get())

        itotal =((meal1 * 3.00) + (meal2 * 3.50) + (meal3 * 4.30) + (meal4 * 4.20) + (meal5 * 4.50))
        self.vtotal.set(itotal)

    def check1(self):
        if (self.var1.get() == 1):
            self.lbl1 = Label(self.w1, text="Americano", bg = "#FFFFFF")
            self.lbl1.place(x = 30, y = 50)

            
    def check2(self):
        if (self.var2.get() == 1):
            self.lbl2 = Label(self.w1, text="Cuppacino", bg = "#FFFFFF")
            self.lbl2.place(x = 30, y = 70)

    def check3(self):
        if (self.var3.get() == 1):
            self.lbl3 = Label(self.w1, text="Latte", bg = "#FFFFFF")
            self.lbl3.place(x = 30, y = 90)

    def check4(self):
        if (self.var4.get() == 1):
            self.lbl4 = Label(self.w1, text="Mocha", bg = "#FFFFFF")
            self.lbl4.place(x = 30, y = 110)

    def check5(self):
        if (self.var5.get() == 1):
            self.lbl5 = Label(self.w1, text="Espresso", bg = "#FFFFFF")
            self.lbl5.place(x = 30, y = 130)
            
    def exit(self):
        self.w1.destroy()
        

#creates page for menu two
class CafeMenu2():
    def __init__(self, parent):
        self.gui(parent)
   #creates interface for second page, widgets, functions for widgets        
    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#FFFFFF')
            self.w1.geometry('680x350')
            self.v = IntVar(value=0)
            self.v.set(0)
            self.w = StringVar()
            self.americano = IntVar()
            self.cuppacino = IntVar()
            self.latte = IntVar()
            self.mocha = IntVar()
            self.espresso = IntVar()
        
            self.vtotal = IntVar()

            self.var1 = IntVar()
            self.var2 = IntVar()
            self.var3 = IntVar()
            self.var4 = IntVar()
            self.var5 = IntVar()

            
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 410, height = 370)
        self.image1 = Canvas(self.w1, bg = '#DCB68A')
        self.image1.place(x = 0, y = 0, width = 150, height = 350)
        self.label1 = Label(self.w1, text = "Sandwiches", fg = "#000000", bg = "#FFFFFF", font = tkinter.font.Font(family = "Harlow Solid Italic", size = 20, weight = "normal"), cursor = "arrow", state = "normal")
        self.label1.place(x = 170, y = 120, width = 130, height = 32)
        self.label5 = Label(self.w1, text = "Menu ", fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "Script MT Bold", size = 28, weight = "normal"), cursor = "arrow", state = "normal")
        self.label5.place(x = 320, y = 40, width = 120, height = 42)
        self.label4 = Label(self.w1, text = "$", fg = "#080808",bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14), cursor = "arrow", state = "normal")
        self.label4.place(x = 420, y = 110, width = 90, height = 22)

        
        self.check1 = Checkbutton(self.w1, text = "Chicken ", fg = "#070707", bg = "#FFFFFF",  variable=self.var1, font = tkinter.font.Font(family = "Arial Black", size = 12, weight = "normal"), cursor = "arrow", state = "normal", command=self.check1)
        self.check1.place(x = 360, y = 148, width = 120, height = 22)
        self.check1.deselect()
        self.check2 = Checkbutton(self.w1, text = "Vege", fg = "#070707", bg = "#FFFFFF", variable=self.var2, font = tkinter.font.Font(family = "Arial Black", size = 12, weight = "normal"), cursor = "arrow", state = "normal", command=self.check2)
        self.check2.place(x = 345, y = 170, width = 120, height = 22)
        self.check2.deselect()
        self.check3 = Checkbutton(self.w1, text = "Beef", fg = "#070707", bg = "#FFFFFF", variable=self.var3,  font = tkinter.font.Font(family = "Arial Black", size = 12, weight = "normal"), cursor = "arrow", state = "normal", command=self.check3)
        self.check3.place(x = 343, y = 190, width = 120, height = 22)
        self.check3.deselect()
        self.check4 = Checkbutton(self.w1, text = "Egg", fg = "#070707", bg = "#FFFFFF",variable=self.var4, font = tkinter.font.Font(family = "Arial Black", size = 12, weight = "normal"), cursor = "arrow", state = "normal",command=self.check4)
        self.check4.place(x = 340, y = 210, width = 120, height = 22)
        self.check4.deselect()
        self.check5 = Checkbutton(self.w1, text = "Cheese", fg = "#070707", bg = "#FFFFFF", variable=self.var5, font = tkinter.font.Font(family = "Arial Black", size = 11, weight = "normal"), cursor = "arrow", state = "normal", command=self.check5)
        self.check5.place(x = 355, y = 230, width = 120, height = 22)
        self.check5.deselect()

        self.radio6 = Label(self.w1, text = "4.60",  fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio6.place(x = 480, y = 150, width = 90, height = 22) 
        self.radio7 = Label(self.w1, text = "4.30", fg = "#000000", bg = "#FFFFFF",font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio7.place(x = 480, y = 170, width = 90, height = 22)
        self.radio8 = Label(self.w1, text = "5.00",  fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio8.place(x = 480, y = 190, width = 90, height = 22)
        self.radio9 = Label(self.w1, text = "3.20", fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio9.place(x = 480, y = 210, width = 90, height = 22)
        self.radio10 = Label(self.w1, text = "2.50", fg = "#000000", bg = "#FFFFFF",font = tkinter.font.Font(family = "Arial Black", size = 10), cursor = "arrow", state = "normal")
        self.radio10.place(x = 480, y = 230, width = 90, height = 22)
    
        
        self.button3 = Button(self.w1, text = ">", bg = "#ffaa7f", fg = "#ffffff", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button3.place(x = 380, y = 310, width = 40, height = 22)
        self.button3['command'] = self.forward
        self.button4 = Button(self.w1, text = "<", bg = "#ffaa7f", fg = "#ffffff", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button4.place(x = 290, y = 310, width = 40, height = 22)
        self.button4['command'] = self.backward
        
        self.label10 = Label(self.w1, text = "Your order:    $", fg = "#000000", bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label10.place(x = 30, y = 55, width = 90, height = 22)
        
        self.text1 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8),textvariable=self.americano, cursor = "arrow", state = NORMAL)
        self.text1.place(x = 560, y = 150, width = 50, height = 20)
        self.text2 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8),textvariable=self.cuppacino, cursor = "arrow", state = NORMAL)
        self.text2.place(x = 560, y = 170, width = 50, height = 20)
        self.text3 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8),textvariable=self.latte, cursor = "arrow", state = NORMAL)
        self.text3.place(x = 560, y = 190, width = 50, height = 20)
        self.text4 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8),textvariable=self.mocha, cursor = "arrow", state = NORMAL)
        self.text4.place(x = 560, y = 210, width = 50, height = 20)
        self.text5 = Entry(self.w1, bg = "#dcb68a", fg = "#0b0b0b", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), textvariable=self.espresso, cursor = "arrow", state = NORMAL)
        self.text5.place(x = 560, y = 230, width = 50, height = 20)
        
        self.button2 = Button(self.w1, text = "Total", bg = "#FFFFFF", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal", command=self.total)
        self.button2.place(x = 170, y = 250, width = 90, height = 22)

        self.button1 = Button(self.w1, text = "Confirm Order", bg = "#FFFFFF", fg = "#090909", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button1.place(x = 30, y = 280, width = 90, height = 22)
        self.button1['command'] = self.confirm
        
        self.button2 = Button(self.w1, text = "Reset", bg = "#FFFFFF", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal", command=self.reset)
        self.button2.place(x = 30, y = 310, width = 90, height = 22)

        self.button3 = Button(self.w1, text = "Exit", bg = "#FFFFFF", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button3.place(x = 590, y = 310, width = 50, height = 22)

        self.tree = Frame(self.w1, bg = "#ffffff")
        self.tree.place(x = 20, y = 50, width = 110, height = 220)

        
        self.text3 = Entry(self.w1, bg = "#ffffff", fg = "#090909", textvariable=self.vtotal, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14, weight = "bold"), cursor = "arrow", state = "normal")
        self.text3.place(x = 170, y = 170, width = 70, height = 50)

        

        
        
#define functions
    def backward(self):
        self.w1.destroy()
        a = CafeMenu(0)
        a.w1.mainloop()

    def total(self):
        meal1 = float(self.americano.get())
        meal2 = float(self.cuppacino.get())
        meal3 = float(self.latte.get())
        meal4 = float(self.mocha.get())
        meal5 = float(self.espresso.get())

        itotal =((meal1 * 3.00) + (meal2 * 3.50) + (meal3 * 4.30) + (meal4 * 4.20) + (meal5 * 4.50))
        self.vtotal.set(itotal)

    def forward(self):
        self.w1.destroy()
        a = Orderpage(0)
        a.w1.mainloop()

    def confirm(self):
        self.w1.destroy()
        a = Orderpage(0)
        a.w1.mainloop()

    def reset(self):
        self.lbl1.destroy()
        self.lbl2.destroy()
        self.lbl3.destroy()
        self.lbl4.destroy()
        self.lbl5.destroy()
    
    def check1(self):
        if (self.var1.get() == 1):
            self.lbl1 = Label(self.w1, text="Chicken", bg = "#FFFFFF")
            self.lbl1.place(x = 30, y = 50)

    def check2(self):
         if (self.var2.get() == 1):
            self.lbl2 = Label(self.w1, text="Vegeterian", bg = "#FFFFFF")
            self.lbl2.place(x = 30, y = 70)


    def check3(self):
         if (self.var3.get() == 1):
            self.lbl3 = Label(self.w1, text="Beef", bg = "#FFFFFF")
            self.lbl3.place(x = 30, y = 90)

    def check4(self):
        if (self.var4.get() == 1):
            self.lbl4 = Label(self.w1, text="Egg", bg = "#FFFFFF")
            self.lbl4.place(x = 30, y = 110)

        
    def check5(self):
         if (self.var5.get() == 1):
            self.lbl5 = Label(self.w1, text="Cheese", bg = "#FFFFFF")
            self.lbl5.place(x = 30, y = 130)

    def exit(self):
        self.w1.destroy()
        
    
class Orderpage():
    def __init__(self, parent):
        self.gui(parent)
   #creates interface for third page, widgets, functions for widgets        
    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#FFFFFF')
            self.w1.geometry('680x350')
            self.v = IntVar(value=0)
            self.v.set(0)
            self.w = StringVar()
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 410, height = 370)
        self.image2 = Canvas(self.w1, bg = '#dcb68a')
        self.image2.place(x = -10, y = 70, width = 720, height = 280)
        self.label3 = Label(self.w1, text = "Order details", fg = "#040404", bg = "#FFFFFF", font = tkinter.font.Font(family = "Script MT Bold", size = 22, weight = "normal"), cursor = "arrow", state = "normal")
        self.label3.place(x = 255, y = 20, width = 160, height = 42)


        
        

        

        

if __name__ == '__main__':
    a = Widget1(0)
    a.w1.mainloop()
