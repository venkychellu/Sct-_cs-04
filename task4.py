import tkinter as tk

def log_key(event):
    key = event.char
    with open("key_log.txt", "a") as f:
        f.write(key)

root = tk.Tk()
root.title("Safe Key Logger Demo")

label = tk.Label(root, text="Type here (your keys will be logged):")
label.pack()

text_box = tk.Text(root, width=50, height=10)
text_box.pack()
text_box.bind("<Key>", log_key)

root.mainloop()