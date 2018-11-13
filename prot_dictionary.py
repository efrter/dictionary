# -------------------- #
# import library
# -------------------- #
import sys
import tkinter as tk

# -------------------- #
# Tinter's init
# -------------------- #
root = tk.Tk()
root.title(u"Private Dictionary")
root.geometry("400x300")

# -------------------- #
# Main Loop start
# -------------------- #
status = tk.Label(root, text="Now processing...", borderwidth=2, relief="groove")
status.pack(side=tk.BOTTOM, fill=tk.X)


mg1 = tk.Label(text=u'This is your private Dictionary.\n')
mg1.pack()

eb = tk.Entry()
eb.pack()
data1 = eb.get()


# -------------------- #
# Main Loop end
# -------------------- #


# -------------------- #
# Tinter's loop
# -------------------- #
root.mainloop()
