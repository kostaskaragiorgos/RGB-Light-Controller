""" RGB LIGHT CONTROLLER"""

from tkinter import Menu, Button, messagebox as msg, Tk, Label, END
from tkinter import Text, Scale, HORIZONTAL

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
        self.master.geometry("250x250")
        self.master.resizable(False, False)



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