
from tkinter import filedialog, END, messagebox, Tk, Text, Menu
from utils.process import fluffCutter
f = None  # this will change
from utils.preprocess import getText

def newFile():
    global f
    f = "Untitled"
    text.delete(0.0, END)


def saveFile():
    global f
    t = text.get(0.0, END)  # stores all text to text box
    # opens and stores file as if you're hitting save
    file = open(f, 'w')
    file.write(t)
    file.close()


def saveAs():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.docx')
    t = text.get(0.0, END)
    try:
        file.write(t.rstrip())
    except:
        messagebox.showerror(title='Oops!', message='Unable to save file...')


def openFile():
    file = filedialog.askopenfilename()
    #t = file.read()
    t = getText(file)
    #print(t)
    text.delete(0.0, END)
    text.insert(0.0, t)


def highlight():
    word_list = text.get('1.0', END).split()
    tags = ['tg' + str(k) for k in range(len(word_list))]
    selected = fluffCutter(word_list)

    #myword = word_list[0]  # test purposes only. Will change to fit fluff cutter
    #text.delete('1.0', END)
    # for i, word in enumerate(word_list):
    #     if word[:len(myword)] == myword:
    #         color_text(text, tags[i], word, 'black', 'yellow')
    #     else:
    #         color_text(text, tags[i], word)
    '''
    for i, word in enumerate(selected):
        color_text(text, tags[i], word, 'black', 'yellow')
    '''

def color_text(edit, tag, word, fg_color='black', bg_color='white'):
    word = word + ' '
    edit.insert('end', word)
    end_index = edit.index('end')
    begin_index = '%s - %sc' % (end_index, len(word) + 1)
    edit.tag_add(tag, begin_index, end_index)
    edit.tag_config(tag, foreground=fg_color, background=bg_color)


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
