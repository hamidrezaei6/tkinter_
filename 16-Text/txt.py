from tkinter import * 


win = Tk()

txt = Text(win,bg='#abcabc')
txt.pack()

txt.insert(INSERT,'www.')
txt.insert(CURRENT,'TOPLEARN')
txt.insert(END,'.com')

win.mainloop()