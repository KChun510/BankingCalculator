import tkinter as tk
from tkinter import *
import os


root = tk.Tk()

#---------------Funtion for Apr own window----------------------------------#
def createApr():
	global entry, entry2, entry3, blank
	win = Toplevel()
	win.title('APR')
	canvas1 = tk.Canvas(win, height = 350, width = 350, bg = "#8b0000" )
	canvas1.create_text(125 , 25, text = 'Annual Percentage Rate', fill = 'black', font = 'bold')
	canvas1.pack()

	#Create an input frame
	Iframe = tk.Frame(win, bg = "white")
	Iframe.place(relwidth = 0.75, relheight = 0.35, relx = .05 , rely = .15)


	#Create and Entry widget for user input
	#entry 1 -- P/ amount borrowed
	Label(Iframe, text = 'Amount borrowed:').grid(row = 1, column = 0)
	entry = Entry(Iframe, width = 20)
	entry.focus_set()
	entry.grid(row = 1, column = 1, pady = 2.5)

	#entry 2 -- R/ interest rate
	Label(Iframe, text = 'Annual % rate: ').grid(row = 2, column = 0)
	entry2 = Entry(Iframe, width = 20)
	entry2.focus_set()
	entry2.grid(row = 2, column = 1, pady = 2.5)

	#entry 3 -- T/ time
	Label(Iframe, text = 'Time in Years:').grid(row = 3, column = 0)
	entry3 = Entry(Iframe, width = 20)
	entry3.focus_set()
	entry3.grid(row = 3, column = 1, pady = 2.5)

	#Blank - where result is displayed
	Label(Iframe, text = 'Total Amount:').grid(row = 4, column = 0)
	blank = Entry(Iframe, width = 20 )
	blank.grid(row = 4, column = 1, pady = 10)

	aprGet = Button(win, text = 'Get APR Val', font = ("calibri", 10, "bold"),  command = apr).pack()

#Returns APR total// Edit
def apr():
	p = float(entry.get())
	r = float(entry2.get())
	t = float(entry3.get())
	a = (p * (1 + (r * t)))#figure out how to display val3
	apr = a - p
	blank.insert(0, apr)



#--------------- Other Funtions to create New Window----------------------------------#
def createSimpInt():
	win = Toplevel()
	win.title('Simple Interest')
	canvas = tk.Canvas(win, height = 350, width = 350, bg = "#8b0000" )
	canvas.pack()


def createComInt():
	win = Toplevel()
	win.title('Compounding Interest')
	canvas1 = tk.Canvas(win, height = 500, width = 500, bg = "#8b0000" )
	canvas1.pack()


#---------------Funtion for Monthly Pay---------------------------------#

def createMonPay():
	global entry, entry2, entry3, blank
	win = Toplevel()
	win.title('Monthly Payment')
	canvas1 = tk.Canvas(win, height = 350, width = 350, bg = "#8b0000" )
	canvas1.create_text(125 , 25, text = 'Monthly Payments', fill = 'black', font = 'bold' )
	canvas1.pack()


	Iframe = tk.Frame(win, bg = "white")
	Iframe.place(relwidth = 0.75, relheight = 0.35, relx = .05 , rely = .15)

	#entry1 == total
	Label(Iframe, text = 'Amount Due:').grid(row = 1, column = 0)
	entry = Entry(Iframe, width = 20)
	entry.grid(row = 1, column = 1, pady = 2.5)

	#entry2 == months
	Label(Iframe, text = 'Months:').grid(row = 2, column = 0)
	entry2 = Entry(Iframe, width = 20)
	entry2.grid(row = 2, column = 1, pady = 2.5)


	#blank ==  monthly payment
	Label(Iframe, text = 'Payment total:').grid(row = 3, column = 0)
	blank = Entry(Iframe, width = 20)
	blank.grid(row = 3, column = 1, pady = 10)


	Button(win, text = 'Monthly Payemnt', font = ("calibri", 10, "bold"),  command = MonthlyPayment).pack()


def MonthlyPayment():
	amount = int(entry.get()) / int(entry2.get())
	blank.insert(0, amount)





#Function closes window
def close():
	root.quit()


#--------------- Canvas for Main ----------------------------------#
canvas = tk.Canvas(root, height = 300, width = 300, bg = "#8b0000" )
root.title('Bank App')
#Header
canvas.create_text( 150, 50, text = "Banking Calculator", fill = "black", font = ('bold') )
canvas.pack()




#Frame outlining buttons in main
frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.45, relheight = 0.35, relx = .28 , rely = .25)





#Buttons on a grid
btn1 = tk.Button(frame, text = 'Annual Percentage Rate', command = createApr)
btn1.grid(row = 1, column = 0)

btn2 = tk.Button(frame, text = 'Simple Interest', command = createSimpInt)
btn2.grid(row = 2, column = 0)

btn3 = tk.Button(frame, text = 'Compounding Interest', command = createComInt)
btn3.grid(row = 3, column = 0)

btn3 = tk.Button(frame, text = 'Monthly Payment', command = createMonPay)
btn3.grid(row = 4, column = 0)


#Button that exits
exit = tk.Button(root, text = "Exit", font = ("calibri", 14, "bold"), command = close)
exit.pack()




root.mainloop()