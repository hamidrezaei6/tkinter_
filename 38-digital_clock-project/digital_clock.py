from tkinter import Label,Tk
import time

app = Tk()
app.title('Digital Clock')
app.geometry('420x150')
app.resizable(False,False)

text_font = ('Arial',68,'bold')
background = '#f2e750'
foreground = '#363529'
border_width = 25

label = Label(app,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def digital_clock():
    time_live = time.strftime('%H:%M:%S')
    label.config(text=time_live)
    label.after(1000,digital_clock)


digital_clock()



app.mainloop()