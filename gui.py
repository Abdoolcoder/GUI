from tkinter import * 
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ012345'
def callback(x): 
    label.configure(text='Button {} clicked'.format(alphabet[x]))
root = Tk()
label = Label() 
label.grid(row=1, column=0, columnspan=26)
buttons = [0]*32 
# create a list to hold 26 buttons 
for i in range(32): 
    buttons[i] = Button(text=alphabet[i], command =callback(i))
    buttons[i].grid(row=0, column=i)
mainloop()
