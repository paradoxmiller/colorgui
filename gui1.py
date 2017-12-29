import sys
import os
from tkinter import *
os.system('clear')

def do_stuff():
	
	uname = input("Please input your name: ")
	print()
	ucolors = input("Please input your favorite color: ")
	
	if ucolors == "black":
		fgcolor = "white"
	elif ucolors == "white":
		fgcolor = "black"
	else:
		fgcolor = "white"
	
						
	root = Tk()
	print()
	nametext = 'Hi There! :), ' + uname
	widget = Label(root, text= nametext, bg="black", fg="white", font = "Courier 18 bold")
	print()
	widget.pack(fill=X,padx=50, ipady=25) #bg fill with padding on x(hor) and internal padding on y vert) 			
	widget = Label(root, text='It is very nice to see you', bg=ucolors, fg=fgcolor)
	widget.pack(fill=X,ipadx=20, ipady=25)
		
	mainloop()
		
	
	
try:
	do_stuff()
except TclError:
		print()
		print("Improper Value Entered, please input colors only")
		print()
		#sys.exit()
		do_stuff()

