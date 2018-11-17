# -*- coding: utf8 -*-
import sys
import tkinter as tk

#`----------------------------- #`
# Initialize
#`----------------------------- #
root = tk.Tk()
root.title("Own Dictionary")
root.geometry("400x600+0+0")
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
frame4.place(width=300, height=90, x=0, y=60)
label2 = tk.Label(frame4, text="Explain\t: ")
label2.pack(anchor="nw", side="left")
entry2 = tk.Entry(frame4, justify="left",width=20)
entry2.pack(anchor="nw", side="left")

#`----------------------------- #`
# Frame3
#`----------------------------- #
frame3 = tk.Frame(root, bd=2,relief="ridge")
frame3.place(width=100, height=120, x=300, y=30)

s_mode = tk.Radiobutton(frame3, text = 'Search', variable = val, value = 1)
s_mode.pack(anchor="nw")
w_mode = tk.Radiobutton(frame3, text = 'Write', variable = val, value = 2)
w_mode.pack(anchor="w")
d_mode = tk.Radiobutton(frame3, text = 'Delete', variable = val, value = 3)
d_mode.pack(anchor="w")
e_mode = tk.Radiobutton(frame3, text = 'Edit', variable = val, value = 4)
e_mode.pack(anchor="w")



root.mainloop()