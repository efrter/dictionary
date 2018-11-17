import tkinter 
import sys

class Application(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quit = tkinter.Button(self, text="QUIT", command=self.master.destroy)
        self.quit.pack(side="bottom")

def selectMode():
	if val.get() == 1:
		label.configure(text='Search')
	elif val.get() == 2:
		label.configure(text='Write')
	elif val.get() == 3:
		label.configure(text='Delete')
	elif val.get() == 4:
		label.configure(text='Edit')
	else:
		label.configure(text='error: you miss mode checking')


root = tkinter.Tk()
root.title("Own Dictionary")
root.geometry("400x300")
app = Application(master=root)
status = tkinter.Label(root, text="Now processing..",
                           borderwidth=2, relief="groove")
status.pack(side=tkinter.BOTTOM, fill=tkinter.X)

# -------------------------- #
# ラジオボタン
# -------------------------- #
# valの初期設定
val = tkinter.IntVar()
val.set(0)

label = tkinter.Label(root, text='please check the mode')
label.pack()
s_mode = tkinter.Radiobutton(text = 'Search', variable = val, value = 1)
s_mode.pack()
w_mode = tkinter.Radiobutton(text = 'Write', variable = val, value = 2)
w_mode.pack()
d_mode = tkinter.Radiobutton(text = 'Delete', variable = val, value = 3)
d_mode.pack()
e_mode = tkinter.Radiobutton(text = 'Edit', variable = val, value = 4)
e_mode.pack()
b = tkinter.Button(root, text='Decide Mode', command=selectMode)
b.pack()

# -------------------------- #


Lb1 = tkinter.Listbox(root, selectmode=tkinter.MULTIPLE)
Lb1.insert(1, "TOKYO")
Lb1.insert(2, "KYOTO")
Lb1.insert(3, "OSAKA")
Lb1.insert(4, "GUNMA")
Lb1.insert(5, "GIFU")
Lb1.insert(6, "EHIME")
Lb1.pack()

app.mainloop()