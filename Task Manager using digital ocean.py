from tkinter import *
import requests
import time
import tkinter.messagebox as tmsg
def home():
    global start
    start = Tk()
    start.title("Task Saver")

    start.geometry("720x400")
    start.minsize(720, 400)
    maxwidth = start.winfo_screenwidth()
    maxheight = start.winfo_screenheight()
    frame = Frame(start, bg="grey")

    start.maxsize(maxwidth, maxheight)
    logo = Frame(start, bg="grey", borderwidth=2)
    logo.pack(side=TOP, fill=X)
    logotext = Label(logo, text="Welcome to Task Saver", fg="green",
                     font="vardana 15 bold", bg="lightblue")
    logotext.pack(fill=X)
    space = Label(start, text="")
    space.pack()
    space2 = Label(start, text="")
    space2.pack()
    space2 = Label(start, text="")
    space2.pack()

    getpasswordbutton = Button(start, text="Save Task", bg="grey", font="vardana 20 bold", fg="black", command=savetasks)
    getpasswordbutton.pack()

    space3 = Label(start, text="")
    space3.pack()
    enterpasswordbutton = Button(start, text="Show Tasks", bg="grey", font="vardana 20 bold", fg="black",
                                 command=showtasks)
    enterpasswordbutton.pack()
    start.mainloop()

def savetasks():

    global savetaskscreen
    savetaskscreen= Tk()
    savetaskscreen.title("Save Tasks")
    savetaskscreen.geometry("720x400")

    r1 = Frame(savetaskscreen)
    r1.pack(fill=Y)
    logo = Label(r1, text="Enter Task to Save ", fg="black", font="verdana 22 bold",
                 bg="lightblue")
    logo.pack(fill=X)
    logo1 = Label(r1, text="")
    logo1.pack()

    n2 = Label(r1, text="Enter Task Details: ")
    n2.pack()
    def submittask():
        url = "" #hidden for security reasons
        task=femailenrty.get()

        data={"task":task}
        r=requests.post(url,json=data)

        a.config(text="Task saved successfully.",fg="green")

    femailidt1 = StringVar()

    femailenrty = Entry(r1, textvariable=femailidt1, font="vardana 20")

    femailenrty.pack(fill=X, pady=20)
    submitcode = Button(r1, text="Save Task", font="vardana 20 bold", bg="#98DBC6", fg="black",
                        command=submittask)
    submitcode.pack(pady=20)
    a=Label(r1,text="Enter Task details and click save",font="vardana 15 ")
    a.pack()
    savetaskscreen.mainloop()


def showtasks():
    global showtask
    showtask = Tk()
    showtask.title("Show Tasks")
    showtask.geometry("720x400")

    r1 = Frame(showtask)
    r1.pack(fill=Y)
    logo = Label(r1, text="Your saved Tasks: ", fg="black", font="verdana 22 bold",
                 bg="lightblue")
    logo.pack(fill=X)
    logo1 = Label(r1, text="")
    logo1.pack()

    url = "" #hidden for security reasons
    r=requests.get(url)
    a=r.json()

    def clicked(event):
        x = mylist.curselection()
        x2 = mylist.get(x)

        for key, value in a.items():
            for i in value:
              if i["task"]==x2:
                  url=""+i["id"] #url is hidden
                  r=requests.delete(url)

                  tmsg.showinfo("Task has been deleted!","Task has been deleted!")
                  showtask.destroy()
                  start.destroy()
                  home()

    sb = Scrollbar(showtask)
    sb.pack(side=RIGHT, fill=Y)
    mylist = Listbox(showtask, width=300, height=300, yscrollcommand=sb.set, bg="lightgrey", font="helvetica 12 bold"
                     , fg="green")

    for key,value in a.items():
        for i in value:

            mylist.insert(END, i["task"])

    mylist.pack(side=LEFT, fill=X)
    mylist.bind("<<ListboxSelect>>", clicked)
    sb.config(command=mylist.yview())
if __name__ == '__main__':
    home()

# curl -X DELETE http://178.128.134.111:8080/task/
