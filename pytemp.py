# -*- coding: utf8 -*-
import sys
import tkinter as tk

def modeChange():
	entry3.delete(0, tk.END)
	entry2.delete(0, tk.END)
	entry2.insert(tk.END, entry1.get())

	if val.get() == 1:
		entry3.insert(tk.END, "search")
	elif val.get() == 2:
		entry3.insert(tk.END, "Write")
	elif val.get() == 3:
		entry3.insert(tk.END, "Delete")
	elif val.get() == 4:
		entry3.insert(tk.END, "Edit")
	else:
		entry3.insert(tk.END, "Error")
	
	entry1.delete(0, tk.END)

#`----------------------------- #`
# Initialize
#`----------------------------- #
root = tk.Tk()
root.title("Own Dictionary")
root.geometry("400x850+0+0")
val = tk.IntVar()
val.set(0)

#`----------------------------- #`
# Frame1
#`----------------------------- #
# フレームの作成（フレームをrootに配置,フレーム淵を2pt,フレームの形状をridge）
frame1 = tk.Frame(root,bd=2,relief="ridge")
# フレームを画面に配置し、横方向に余白を拡張する
frame1.place(width=400, height=30, x=0, y=0)

label1 = tk.Label(frame1, text="Menu\t: ")
label1.pack(side="left")
# 作成したフレームにボタン1を配置
button1 = tk.Button(frame1,text=u'終了', command=sys.exit)
# ボタン1を右から配置する
button1.pack(side="left")

#`----------------------------- #`
# Frame2
#`----------------------------- #
frame2 = tk.Frame(root, bd=2,relief="ridge")
frame2.place(width=300, height=30, x=0, y=30)

label1 = tk.Label(frame2, text="Words\t: ")
label1.pack(side="left")
entry1 = tk.Entry(frame2, justify="left",width=20)
entry1.pack(side="left")

#`----------------------------- #`
# Frame4
#`----------------------------- #
frame4 = tk.Frame(root, bd=2,relief="ridge")
frame4.place(width=300, height=120, x=0, y=60)
label2 = tk.Label(frame4, text="Explain\t: ")
label2.pack(anchor="nw", side="left")
text1 = tk.Text(frame4, bd=2, width=25, height=6, wrap="word")
text1.pack(anchor="nw", side="left")

#`----------------------------- #`
# Frame3
#`----------------------------- #
frame3 = tk.Frame(root, bd=2,relief="ridge")
frame3.place(width=100, height=150, x=300, y=30)

s_mode = tk.Radiobutton(frame3, text = 'Search', variable = val, value = 1)
s_mode.pack(anchor="nw")
w_mode = tk.Radiobutton(frame3, text = 'Write', variable = val, value = 2)
w_mode.pack(anchor="w")
d_mode = tk.Radiobutton(frame3, text = 'Delete', variable = val, value = 3)
d_mode.pack(anchor="w")
e_mode = tk.Radiobutton(frame3, text = 'Edit', variable = val, value = 4)
e_mode.pack(anchor="w")

button2 = tk.Button(frame3,text=u'Do', command=modeChange)
button2.pack(side="left")

#`----------------------------- #`
# Frame7
#`----------------------------- #
frame7 = tk.Frame(root, bd=2,relief="ridge")
frame7.place(width=400, height=30, x=0, y=180)

label6 = tk.Label(frame7, text="Mode\t: ")
label6.pack(anchor="nw", side="left")

entry3 = tk.Entry(frame7)
entry3.pack(anchor="nw", side="left")

#`----------------------------- #`
# Frame5
#`----------------------------- #
frame5 = tk.Frame(root, bd=2,relief="ridge")
frame5.place(width=400, height=30, x=0, y=210)

label4 = tk.Label(frame5, text="Words\t: ")
label4.pack(anchor="nw", side="left")
entry2 = tk.Entry(frame5)
entry2.pack(anchor="nw", side="left")

#`----------------------------- #`
# Frame6
#`----------------------------- #
frame6 = tk.Frame(root, bd=2,relief="ridge")
frame6.place(width=400, height=150, x=0, y=240)

label5 = tk.Label(frame6, text="Explain\t: ")
label5.pack(anchor="nw", side="left")
text2 = tk.Text(frame6, bd=2, width=25, height=6, wrap="word")
text2.pack(anchor="nw", side="left")

#`----------------------------- #`
# Finalize
#`----------------------------- #
root.mainloop()