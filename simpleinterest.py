from tkinter import *
window = Tk()

window.title('Simple Interest Calculator')
window.geometry('380x400')
window.configure(bg='lightcyan')


# Calculate Interest Function

def calculateinterest():
    principal=float(principal_entry.get())
    rateofinterest=float(rateofinterest_entry.get())
    time=float(time_entry.get())
    simpleinterest = (principal*rateofinterest*time)/100
    
    name = username_entry.get()
    result_label.destroy()
    


    output_message = Label(result_frame,text=name+", your simple interest is "+str(simpleinterest),bg = "lightcyan", font=("Calibri", 12), width=42  )
    output_message.place(x=20,y=40)
    output_message.pack()



username_label = Label(window,text='Username',fg='black',bg='lightcyan',bd=1)
username_label.place(x=30,y=80)

username_entry=Entry(window,text='',bd=2,width=22)
username_entry.place(x=150,y=80)

heading = Label(window, text='Simple Interest Calculator', fg='black', bg='lightcyan', font=("Calibri", 12),bd=10)
heading.place(x=90, y=20)

principal_label = Label(window, text='Principal', fg='black', bg='lightcyan', font=("Calibri", 12),bd=1)
principal_label.place(x=30, y=120)

principal_entry=Entry(window,text='', bd=2, width=22)
principal_entry.place(x=150,y=120)

rateofinterest_label = Label(window, text='Rate Of Interest', fg='black', bg='lightcyan', font=("Calibri", 12),bd=1)
rateofinterest_label.place(x=30, y=160)

rateofinterest_entry=Entry(window,text='', bd=2, width=22)
rateofinterest_entry.place(x=150,y=160)

time_label = Label(window, text='Time', fg='black', bg='lightcyan', font=("Calibri", 12),bd=1)
time_label.place(x=30, y=200)

time_entry=Entry(window,text='', bd=2, width=22)
time_entry.place(x=150,y=200)

calculatebutton = Button(window,text='Calculate', fg='black',bg='lightcyan',bd=4, command=calculateinterest)
calculatebutton.place(x=40,y=240)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=320)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()