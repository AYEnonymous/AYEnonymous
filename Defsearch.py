
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
import io

root = Tk()
root.title("Keyword Search App")
root.geometry("300x50")
img = PhotoImage(file='F:\\Python\\keyword.png')
root.iconphoto(False,img)

entry_var = tk.StringVar()

class KeywordApp:

    def __init__(self, master):

        myFrame = Frame(master)
        myFrame.grid

        self.entry_label = Label(master, text= "Keyword: ").grid(row=1,column=0)
        self.text = Entry(master, textvariable= entry_var).grid(row=1, column=1)
        self.open = Button(master, text = "Open File", command=self.open_file).grid(row=2, column=0)
        self.search = Button(master, text = "Search", command=self.input).grid(row=2, column=1)

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir=".")
        self.infile = open(filename, "r")
        print(self.infile.name)
        self.infile.close()

    def input(self):
        entry = entry_var.get()
        entry_var.set("")

        try:
            file = open(self.infile.name)
            keyword = entry
            lines = file.readlines()
            list = []
            idx = 0
            for line in lines:
                if keyword in line:
                    list.insert(idx, line)
                    idx += 1
            file.close

            if len(list)==0:
                print(keyword+ "not found in " +file)
            else:
                lineLen = len(list)
                print("\n**** Lines containing \"" +keyword+ "\" ****\n")
                for i in range(lineLen):
                    print(end=list[i])
                print()
        except:
            print("Does not exist please try another keyword")



e = KeywordApp(root)
root.mainloop()
