from tkinter import *

window = Tk()
window.title('Temperature Converter')
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

label = Label(text='Convert from fahrenheit to celcius :',
              font=('arial', 25, 'bold'))
label.grid(column=2, row=0)
label.config(pady=10)

input = Entry()
input.grid(row=2, column=2)

ans = Label(text='  ', font=('arial', 10, 'bold'))
ans.grid(row=4, column=2)


# 5 * (f-32) / 9       -->> c*9/5+32
def convert():
    temp = float(input.get())
    temp_c = 5 * (temp-32)/9
    ans['text'] = 'Temperature in celcius is :' + str(int(temp_c))


btn = Button(text='Convert', command=convert)
btn.grid(row=2, column=3)


window.mainloop()
