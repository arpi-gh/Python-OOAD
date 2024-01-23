import tkinter.filedialog
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.filepath = None

        self.text.bind("<Control-z>", self.undo)
        self.text.bind("<Control-y>", self.redo)
        self.text.bind("<Control-s>", self.save_file)

    def client_exit(self):
        exit()

    def open_file(self):
        self.filepath = (tkinter.filedialog.askopenfilename
                         (initialdir=r"C:\Users\User\PycharmProjects\pythonProject",
                          title='Open Text File',
                          filetypes=(("Text Files", "*.txt"),)))

        if self.filepath:
            with open(self.filepath, 'r') as txt_file:
                stuff = txt_file.read()
                self.text.insert(END, stuff)

    def new_file(self):
        pass

    def save_file(self, event=None):
        if self.filepath:
            with open(self.filepath, 'w') as txt_file:
                txt_file.write(self.text.get(1.0, END))
        else:
            self.save_as()
        print('Your file has been saved.')

    def save_as(self, event=None):
        new_file_path = tkinter.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if new_file_path:
            with open(new_file_path, 'w') as file:
                file.write(self.text.get(1.0, END))

    def undo(self, event=None):
        if event:
            self.text.edit_undo()
        else:
            self.text.edit_undo()
        print('Undo works.')

    def redo(self, event=None):
        if event:
            self.text.edit_redo()
        else:
            self.text.edit_redo()
        print('Redo works.')

    def init_window(self):
        self.master.title('Text Editor')
        self.pack(fill=BOTH, expand=1)

        self.text = Text(root, width=40, height=10, font='Helvetica', undo=True)
        self.text.pack(pady=10, padx=10)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='New', command=self.new_file)
        file.add_command(label='Open', command=self.open_file)
        file.add_command(label='Save', command=self.save_file)
        file.add_command(label='Save as', command=self.save_as)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Undo', command=self.undo)
        edit.add_command(label='Redo', command=self.redo)
        menu.add_cascade(label='Edit', menu=edit)

        my_format = Menu(menu)
        my_format.add_command(label='Fonts')
        menu.add_cascade(label='Format', menu=my_format)


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
