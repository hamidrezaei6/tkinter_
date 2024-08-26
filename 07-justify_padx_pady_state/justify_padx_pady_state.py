from tkinter import * 

root = Tk()
root.geometry('300x300')
btn = Button(root)

# justify -->> CENTER , RIGHT , LEFT
# padx 
# pady
# state -->> ACTIVE , DISABALED

btn.config(text='Enter',justify=RIGHT,padx=2,pady=2,state=DISABLED)
btn.pack()





root.mainloop()