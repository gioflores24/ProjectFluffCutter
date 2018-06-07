from tkinter import filedialog, END, messagebox, Tk, Text, Menu
from utils.process import fluff_cutter

f = None  # this will change
from utils.preprocess import get_text


def new_file():
    global f
    f = "Untitled"
    text.delete(0.0, END)


def save_file():
    global f
    t = text.get(0.0, END)  # stores all text to text box
    # opens and stores file as if you're hitting save
    file = open(f, 'w')
    file.write(t)
    file.close()


def save_as():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.docx')
    t = text.get(0.0, END)
    try:
        file.write(t.rstrip())
    except:
        messagebox.showerror(title='Oops!', message='Unable to save file...')


def open_file():
    file = filedialog.askopenfilename()
    # t = file.read()
    t = get_text(file)
    # print(t)
    text.delete(0.0, END)
    text.insert(0.0, t)


def highlight():
    word_list = text.get('1.0', END).split()

    tags = ['tag' + str(i) for i in range(len(word_list))]

    selected = fluff_cutter(word_list)
    text.delete('1.0', END)
    # for i, word in enumerate(word_list):
    #     if word[:len(myword)] == myword:
    #         color_text(text, tags[i], word, 'black', 'yellow')
    #     else:
    #         color_text(text, tags[i], word)

    # for i, word in enumerate(selected):
    #     color_text(text, tags[i], word, 'black', 'yellow')
    # for i in selected:
    #     text.insert(END, ' ' + i)
    print(word_list)
    print(selected)
    i = 0
    # for _ in enumerate(word_list):
    #     if selected[i] == word_list[j]:  # highlight
    #         color_text(text, tags[i], selected[i], 'black', 'yellow')
    #         i += 1
    #
    #     else:  # don't highlight
    #         color_text(text, tags[j], word_list[j])
    #         print(word_list[j])
    #     j += 1
    for ix, word in enumerate(word_list):
        myword = selected[i]
        if word[:len(myword)] == myword:
            color_text(text, tags[ix], word, 'black', 'yellow')
            i += 1
        else:
            color_text(text, tags[ix], word)




def color_text(edit, tag, word, fg_color='black', bg_color='white'):
    word = word + ' '
    edit.insert('end', word)
    end_index = edit.index('end')
    begin_index = '%s - %sc' % (end_index, len(word) + 1)
    edit.tag_add(tag, begin_index, end_index)
    edit.tag_config(tag, foreground=fg_color, background=bg_color)


root = Tk()
root.title("Fluff Cutter")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=600)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save As...", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
editmenu = Menu(menubar)
editmenu.add_command(label="Cut The Fluff", command=highlight)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
