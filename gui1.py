
uname = input("Please input your name: ")
ucolors = input("Please input your favorite color: ")

if ucolors == "black":
	fgcolor = "white"
elif ucolors == "white":
	fgcolor = "black"
else:
	fgcolor = "white"


from tkinter import *

root = Tk()

nametext = 'Hi There! :), ' + uname
widget = Label(root, text= nametext, bg="black", fg="white", font = "Courier 18 bold")
widget.pack(fill=X,padx=50, ipady=25) #bg fill with padding on x(hor) and internal padding on y(vert)
widget = Label(root, text='It is very nice to see you', bg=ucolors, fg=fgcolor)
widget.pack(fill=X,ipadx=20, ipady=25)

mainloop()

