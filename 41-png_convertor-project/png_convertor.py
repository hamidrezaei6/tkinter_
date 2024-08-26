import tkinter as tk
from tkinter import filedialog
# pip install PIL-Tools
from PIL import Image

root = tk.Tk()
root.title('Image Converter')
can = tk.Canvas(root, width=300, height=250, bg='purple', relief='raised')
can.pack()

lbl = tk.Label(root, text='Image Converter', bg='purple')
lbl.config(font=('arial', 20))
can.create_window(150, 60, window=lbl)


def getPng():
    global img
    import_file_path = filedialog.askopenfilenames()
    img = Image.open(import_file_path)


browse_png = tk.Button(text='Select PNG file', command=getPng,
                       bg='royalblue', fg='white', font=('arial', 12, 'bold'))
can.create_window(150, 130, window=browse_png)


def convert():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    img.save(export_file_path)


save_btn = tk.Button(text='Convert PNG to JPG', command=convert,
                     bg='royalblue', fg='white', font=('arial', 12, 'bold'))

can.create_window(150,180,window=save_btn)


root.mainloop()
