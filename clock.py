import tkinter as tk
import time
from PIL import Image,ImageTk


root = tk.Tk()
root.title('Digital Clock')
root.geometry('800x400')
root.config(bg='sky blue')

label_hrs = tk.Label(text='12',font=('Times new roman',30,'bold'),bg='sky blue')
label_hrs.place(x=50,y=40,width=60)

label_hrs1 = tk.Label(text='Hours',font=('Times new roman',15),bg='sky blue')
label_hrs1.place(x=50,y=100,width=60)

label_colon = tk.Label(text=":",font=('Times new roman',30,'bold'),bg='sky blue')
label_colon.place(x=100,y=40,width=60)

label_min = tk.Label(text='12',font=('Times new roman',30,'bold'),bg='sky blue')
label_min.place(x=150,y=40,width=60)

label_min1 = tk.Label(text='Minutes',font=('Times new roman',15),bg='sky blue')
label_min1.place(x=150,y=100,width=60)

label_colon1 = tk.Label(text=":",font=('Times new roman',30,'bold'),bg='sky blue')
label_colon1.place(x=200,y=40,width=60)


label_sec = tk.Label(text='12',font=('Times new roman',30,'bold'),bg='sky blue')
label_sec.place(x=250,y=40,width=60)

label_sec1 = tk.Label(text='Seconds',font=('Times new roman',15),bg='sky blue')
label_sec1.place(x=250,y=100,width=65)

label_am = tk.Label(text='AM',font=('Times new roman',30,'bold'),bg='sky blue')
label_am.place(x=310,y=40)


label_date = tk.Label(text='Date',font=('Times new roman',20,'bold'),bg='sky blue')
label_date.place(x=50,y=200)
label_date1 = tk.Label(text='12/12/12',font=('Times new roman',20,'bold'),bg='sky blue')
label_date1.place(x=50,y=230)


label_timez = tk.Label(text='Time Zone',font=('Times new roman',20,'bold'),bg='sky blue')
label_timez.place(x=200,y=200)
label_timez1 = tk.Label(text='12/12/12',font=('Times new roman',20,'bold'),bg='sky blue')
label_timez1.place(x=200,y=230)


label_day = tk.Label(text='Day',font=('Times new roman',20,'bold'),bg='sky blue')
label_day.place(x=500,y=200)
label_day1 = tk.Label(text='Monday',font=('Times new roman',20,'bold'),bg='sky blue')
label_day1.place(x=500,y=230)

img = Image.open('clock_img.jpg')
img = img.resize((150,150))
clock_img = ImageTk.PhotoImage(img)
x = tk.Label(image=clock_img)
x.place(x=550,y=30)
def updateTime():
	Hrs = time.strftime("%I")
	label_hrs.config(text=Hrs)

	Min = time.strftime("%M")
	label_min.config(text=Min)

	Sec = time.strftime("%S")
	label_sec.config(text=Sec)

	AMPM =time.strftime('%p')
	label_am.config(text=AMPM)

	Date = time.strftime("%x")
	label_date1.config(text=Date)

	Timezone = time.strftime("%Z")
	label_timez1.config(text=Timezone)

	Day = time.strftime("%A")
	label_day1.config(text=Day)
	root.after(1000,updateTime)
updateTime()
root.mainloop()