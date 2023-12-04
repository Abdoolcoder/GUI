from tkinter import *
# def calc():
#     num = int(input_tag.get())
#     converted = num*60
#     if converted >= 20000:
#         output_label.configure(text='Oh syntax error')
#     else:
#         output_label.configure(text='Your answer is {}'.format(converted))
def add():
    name = 'abdul'
    first_input = int(input_tag1.get())
    second_input = int(input_tag2.get())
    addition = first_input + second_input
    output_label.configure(text='The sum of {} and {} is {}'.format(first_input,second_input,addition))
    
def sub():
    first_input = int(input_tag1.get())
    second_input = int(input_tag2.get())
    sub = first_input - second_input
    output_label.configure(text='The diff of {} and {} is {}'.format(first_input,second_input,sub))

def mult():
    first_input = int(input_tag1.get())
    second_input = int(input_tag2.get())
    mult = first_input * second_input
    output_label.configure(text='The multiplication of {} and {} is {}'.format(first_input,second_input,mult))
    
def divi():
    first_input = int(input_tag1.get())
    second_input = int(input_tag2.get())
    div = int(first_input / second_input)
    output_label.configure(text='The division of {} and {} is {}'.format(first_input,second_input,div))
    




root = Tk()
#calc Name
label_text = Label(text="Abdul's CALCULATOR")
#input name and tag
input1 = Label(text='Input 1:')
input2 = Label(text='Input 2:')
input_tag1 = Entry()
input_tag2 = Entry()
#operators button
add_button = Button(text='+',command=add)
sub_button = Button(text='-',command=sub)
mult_button = Button(text='*',command=mult)
division_button = Button(text='/',command=divi)
# button_tag = Button(text='ok' ,command=calc)
#answer label
output_label = Label(text='')

label_text.grid(row=0,column=0,columnspan=3)
input1.grid(row=1,column=0)
input2.grid(row=2,column=0)
input_tag1.grid(row=1,column=1)
input_tag2.grid(row=2,column=1)
add_button.grid(row=3,column=2)
sub_button.grid(row=3,column=3)
mult_button.grid(row=3,column=4)
division_button.grid(row=3,column=5)
# button_tag.grid(row=4,column=1)
output_label.grid(row=5,column=0)
mainloop()
