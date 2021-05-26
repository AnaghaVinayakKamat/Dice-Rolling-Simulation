from tkinter import *  
from PIL import ImageTk,Image  
from random import *

#create basic tkinter window
root = Tk()  
root.geometry('600x600')
root.resizable(0,0)                           
root.title('Dice Rolling Simulation')
root.config(bg ='light blue')
Label(root, text = 'Dice Rolling Simulation' , font='arial 20 bold', bg = 'light blue', fg='red', anchor=CENTER)

#label for dice
l1=Label(root, font='times 200 bold', bg='light blue', fg='red', height='50', width='0',text='')

#function definition
def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{choice(dice)}')
    l1.pack()
#Button
b1=Button(root, text=('Roll The Dice'), font='Helvetica 40 bold', anchor=CENTER, fg='black', bg='gray',command=roll).pack()

#img = ImageTk.PhotoImage(Image.open("D:\\Anagha\\Python Projects\\die1.png"))
root.mainloop() 