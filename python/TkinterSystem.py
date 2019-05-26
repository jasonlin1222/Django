import tkinter as tk

window = tk.Tk()
window.geometry("400*400")
window.title("system")
id = tk.StringVar()
title = tk.Label(window, text="label", font=("Times",20))
title.place(x=100, y=30)
button = tk.Button(x=300, y=80, command = callfile(id))
intext = tk.Entry(window.textvariable = id)

def callfile(id):
    
window.mainloop()
