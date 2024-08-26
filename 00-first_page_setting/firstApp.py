from tkinter import *

win = Tk()
# عنوان صفحه
win.title('First App')

# اندازه صفحه و محل باز شدن آن در صفحه نمایش
win.geometry('600x400+400+150')

# حداقل و حداکثر اندازه ای که صفحه میتواند تغییر کند
win.minsize(200,200)
win.maxsize(600,400)


# win.resizable(width=False,height=False)
# win.resizable(False,False)



# مسیر ذخیره سازی عکس در کامپیوتر خود را وارد کنید
win.iconbitmap(r'E:\TopLearn\Tkinter_Course\2-ساخت اولین صفحه و تنظیمات آن\first_page_setting\images\python.ico')


# mainloop() برای اجرای پنجره گرافیکی
win.mainloop()



