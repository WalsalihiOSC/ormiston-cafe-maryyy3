from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
from tkinter import ttk 


#creates class menu which is first page 
class CafeMenu():
    def __init__(self, parent):
        self.gui(parent)
    #creates gui for widgets for FIRST menu page only 
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
        self.radio6 = Radiobutton(self.w1, text = "3.00", value = 3.00, variable = self.v, fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
        self.radio6.place(x = 420, y = 150, width = 90, height = 22)
        self.radio6['command'] = self.append
        self.radio7 = Radiobutton(self.w1, text = "3.50", value = 3.50,variable = self.v, fg = "#000000", bg = "#FFFFFF",font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
        self.radio7.place(x = 420, y = 170, width = 90, height = 22)
        self.radio7['command'] = self.append
        self.radio8 = Radiobutton(self.w1, text = "4.30", value = 4.30,variable = self.v, fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
        self.radio8.place(x = 420, y = 190, width = 90, height = 22)
        self.radio8['command'] = self.append
        self.radio9 = Radiobutton(self.w1, text = "4.20", value = 4.20, variable = self.v, fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
        self.radio9.place(x = 420, y = 210, width = 90, height = 22)
        self.radio9['command'] = self.append
        self.radio10 = Radiobutton(self.w1, text = "4.50", value = 4.50,variable = self.v, fg = "#000000", bg = "#FFFFFF",font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
        self.radio10.place(x = 420, y = 230, width = 90, height = 22)
        self.radio10['command'] = self.append
        self.radio11 = Radiobutton(self.w1, text = "5.00", value = 5.00, variable = self.v, fg = "#000000",bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
        self.radio11.place(x = 420, y = 250, width = 90, height = 22)
        self.radio11['command'] = self.append
        self.label6 = Label(self.w1, text = "Americano", fg = "#090909",bg = "#FFFFFF", font = tkinter.font.Font(family = "Arial Black", size = 11), cursor = "arrow", state = "normal")
        self.label6.place(x = 310, y = 110, width = 90, height = 92)
        self.label7 = Label(self.w1, text = "Cuppaccino", fg = "#000000", bg = "#FFFFFF", font = tkinter.font.Font(family = "Arial Black", size = 11, weight = "normal"), cursor = "arrow", state = "normal")
        self.label7.place(x = 310, y = 170, width = 97, height = 22)
        self.button3 = Button(self.w1, text = ">", bg = "#ffaa7f", fg = "#ffffff", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button3.place(x = 380, y = 310, width = 40, height = 22)
        self.button3['command'] = self.forward
        self.frame1 = ttk.Treeview(self.w1)
        self.frame1.place(x = 20, y = 50, width = 110, height = 250)
        self.label10 = Label(self.w1, text = "Your order:    $", fg = "#000000", bg = "#FFFFFF", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label10.place(x = 30, y = 55, width = 90, height = 22)



        global count
        count = 0
        count += 1

            
#define forward button
    def forward(self):
        self.w1.destroy()
        a = Cafemenu2(0)
        a.w1.mainloop()

#defines radiobuttons so they are displayed for customers
    def append(self):
        global count
        self.frame1.insert(parent="", index="end", iid=count,text="", values=(self.v.get()))
        count += 1
        

#creates page for menu two
class Cafemenu2():
    def __init__(self, parent):
        self.gui(parent)
        
    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('410x370')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 410, height = 370)
      
        

if __name__ == '__main__':
    a = CafeMenu(0)
    a.w1.mainloop()
