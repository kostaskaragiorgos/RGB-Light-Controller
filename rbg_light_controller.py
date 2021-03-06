""" RGB LIGHT CONTROLLER"""
import serial
from tkinter import Menu, Button, messagebox as msg, Tk, Label, END
from tkinter import Text, Scale, HORIZONTAL

from sqlalchemy import except_all

def helpmenu():
    """help menu function"""
    msg.showinfo("HELP", "")

def aboutmenu():
    """about menu function"""
    msg.showinfo("About", "RGB LIGHT CONTROLLER\nVersion 1.0")

class Rbg_Light_Controller():
    def __init__(self, master):
        self.master = master
        self.master.title("RGB LIGHT CONTROLLER")
        self.master.geometry("200x350")
        self.master.resizable(False, False)
        try:
            self.ser = serial.Serial('com3',9600)
        except:
            msg.showerror("ERROR", "UNABLE TO CONNECT")
            self.master.destroy()


        self.menu = Menu(self.master)

        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)

       

        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)

        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)

        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
    
        self.redsliderleb = Label(self.master, text="RED")
        self.redsliderleb.pack()
        self.redslider = Scale(self.master, from_=0, to=255, tickinterval=100, orient=HORIZONTAL)
        self.redslider.pack()

        self.greensliderleb = Label(self.master, text="GREEN")
        self.greensliderleb.pack()
        self.greenslider = Scale(self.master, from_=0, to=255, tickinterval=100, orient=HORIZONTAL)
        self.greenslider.pack()

        self.bluesliderleb = Label(self.master, text="BLUE")
        self.bluesliderleb.pack()
        self.blueslider = Scale(self.master, from_=0, to=255, tickinterval=100, orient=HORIZONTAL)
        self.blueslider.pack()
        
        self.setbutton = Button(self.master, text="SET", command=self.setcolor)
        self.setbutton.pack()

        self.onbutton = Button(self.master, text="ON")
        self.onbutton.pack()

        self.offbutton = Button(self.master, text="OFF")
        self.offbutton.pack()

    def setcolor(self):
        myinput = ""+str(self.redslider.get())+str(self.greenslider.get())+str(self.blueslider.get())+'\r'
        self.ser.write(myinput.encode())
        

    def exitmenu(self):
        """exit menu function"""
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    



def main():
    """main functionn"""
    root = Tk()
    Rbg_Light_Controller(root)
    root.mainloop()

if __name__ == '__main__':
    main()