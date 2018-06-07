import tkinter as tk


def color_text(edit, tag, word, fg_color='black', bg_color='white'):
    word = word + ' '
    edit.insert('end', word)
    end_index = edit.index('end')
    begin_index = '%s - %sc' % (end_index, len(word) + 1)
    edit.tag_add(tag, begin_index, end_index)
    edit.tag_config(tag, foreground=fg_color, background=bg_color)


def main():
    root = tk.Tk()
    root.geometry('600x200')

    edit = tk.Text(root)
    edit.pack()

    text = "give me the money"

    word_list = text.split()

    #print(word_list)

    myword = 'give'
    myword2 = 'the'

    tags = ["tg" + str(k) for k in range(len(word_list))]
    for ix, word in enumerate(word_list):
        if word[:len(myword)] == myword:
            color_text(edit, tags[ix], word, 'black', 'yellow')
        elif word[:len(myword2)] == myword2:
            color_text(edit, tags[ix], word, 'black', 'yellow')
        else:
            color_text(edit, tags[ix], word)

    root.mainloop()

main()