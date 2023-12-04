from tkinter import *

def cal():
    principal = int(principal_entry.get())
    rate = int(rate_entry.get())
    time = int(time_entry.get())
    simple_int = (principal*rate*time)/100
    answer.configure(text='the intrest is {}'.format(simple_int))



root = Tk()
cal_name = Label(text='Intrest Calculator')
principal_label = Label(text='Principal:')
principal_entry = Entry()
rate_label = Label(text='Rate:')
rate_entry = Entry()
time_label = Label(text='Time:')
time_entry = Entry()
calc_button = Button(text='calculate', command=cal)
answer = Label(text='')
#arranging
cal_name.grid(row=0,column=1,columnspan=3)
principal_label.grid(row=1,column=1)
principal_entry.grid(row=1,column=2,columnspan=1)
rate_label.grid(row=2,column=1)
rate_entry.grid(row=2,column=2,columnspan=1)
time_label.grid(row=3,column=1)
time_entry.grid(row=3,column=2,columnspan=1)
calc_button.grid(row=4,column=3)
answer.grid(row=4,column=0)
mainloop()