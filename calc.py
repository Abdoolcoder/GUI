from tkinter import *
def calc():
    num = int(input_tag.get())
    converted = num*60
    if converted >= 20000:
        output_label.configure(text='Oh syntax error')
    else:
        output_label.configure(text='Your answer is {}'.format(converted))





root = Tk()
label_text = Label(text='enter a number to convert')
input_tag = Entry()
button_tag = Button(text='ok' ,command=calc)
output_label = Label(text='')

label_text.grid(row=0,column=0)
input_tag.grid(row=0,column=2)
button_tag.grid(row=1,column=1)
output_label.grid(row=2,column=0)
mainloop()
