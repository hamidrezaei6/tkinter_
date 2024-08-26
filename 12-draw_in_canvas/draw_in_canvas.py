from tkinter import * 

window = Tk()

cv = Canvas(window,bg='lime',width=400,height=300)
cv.pack()

# cv.create_line(50,50,350,200,dash={3,3},fill='white',width=10)

# cv.create_arc(50,50,350,200,start=50,extent=80,fill='white')

# cv.create_oval(50,50,350,200,fill='white')

cv.create_rectangle(50,50,350,200,fill='red')





window.mainloop()