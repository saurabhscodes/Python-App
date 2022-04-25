import tkinter as tk


root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Calculator")
message.pack()

def sum(*args):
    for arg in args:
        print(arg)


# keep the window displaying
root.mainloop()