from tkinter import *

root = Tk()
root.geometry('350x250+100+120')


msg = StringVar()

# relief -- >> RAISED , SUNKEN , GROOVE , RIDGE
message = Message(root, textvariable=msg, relief=RAISED)

msg.set('Lorem ipsum dolor sit amet, id semper dolorum quaestio est. Facer adipiscing nam id, ex cibo mentitum duo, quo vocent facilisis eloquentiam ei. Per modus soluta honestatis te. Assentior comprehensam nam et, vocent appellantur sit ne.')

message.pack()

root.mainloop()
