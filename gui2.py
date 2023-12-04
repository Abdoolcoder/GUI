from tkinter import *
def callback(): 
    global num_clicks 
    num_clicks = num_clicks * 2 
    label.configure(text='Clicked {} times.'.format(num_clicks))
    if num_clicks >= 500:
        label.configure(text='Clicked over')
    
        
num_clicks = 1 
root = Tk()
label = Label(text='Not clicked') 
button = Button(text='Click me', command=callback)
label.grid(row=0, column=0) 
button.grid(row=1, column=0)
mainloop()
