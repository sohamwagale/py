import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entryInt.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)



#window
window = ttk.Window(themename = 'darkly')
window.title('Demo')
window.geometry('400x200')

#title aka text
title_label = ttk.Label(master = window, text = 'Miles to Morales', font= 'Calibiri 24 italic')
title_label.pack()

#input feild
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text ="Convert" , command = convert)
entry.pack(side = 'left', padx = 10)
button.pack()
input_frame.pack(pady = 20)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window,
                         text = 'Output',
                         font = 'Calibri 20',
                         textvariable = output_string)
output_label.pack(pady = 5)


#run 
window.mainloop()
