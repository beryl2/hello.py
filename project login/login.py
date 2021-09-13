from tkinter import *
class login:
    def __init__(self, root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        self.root.frame(x=330, y=150, width=500, height=400)


        #login frame
        #frame_login = Frame(self.root, bg="white")
        #Frame_login.place(x=330, y=150, width=500,height=400)


        






root = Tk()
obj = login(root)
root.mainloop()
