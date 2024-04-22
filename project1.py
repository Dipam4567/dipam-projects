#Tkinter Widgets
#Widgets in tkinter are the elements of GUI applications which provides several controls (such as -buttons ,Labels,CHeckbox etc)to users to interact with GUI applications
#Simple application with tkinter widgets :
from tkinter import* 
root=Tk()
root.title ("welcome to tkinter.")
lbl= Label(root, text="Hello! World", fg="red", font=("Arial", 20))
lbl.pack()
root.mainloop()#to run gui application 
label=Label(root,text="Hi!students",fg="red",font=("Arial",20))
label.pack()
def clicked():
 label.configure(tent="How are all of you?",fg="blue",font=("Arial",15))
btn=Button(root,tent="clickme!",fg="red",font=("Arial",9),command=clicked)  
btn.pack()
root.mainloop()
