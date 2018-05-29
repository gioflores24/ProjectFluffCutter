from tkinter import filedialog, END, messagebox, Tk, Text, Menu

f = None #this will change

def newFile():
    global f
    f = "Untitled"
    text.delete(0.0,END)

def saveFile():
    global f
    t = text.get(0.0, END) #stores all text to text box
    #opens and stores file as if you're hitting save
    file = open(f, 'w')
    file.write(t)
    file.close()

def saveAs():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.docx')
    t = text.get(0.0,END)
    try:
        file.write(t.rstrip())
    except:
        messagebox.showerror(title='Oops!', message='Unable to save file...')

def openFile():
    file = filedialog.askopenfile(mode='r')
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def highlight():
    print("Highlight!")


root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=600)


text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
editmenu = Menu(menubar)
editmenu.add_command(label="Highlight", command=highlight)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()