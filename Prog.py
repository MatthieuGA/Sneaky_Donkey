import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import tkinter as tkin
from tkinter import ttk
from tkinter import filedialog as fd
from functools import partial
import sys
from PIL import ImageTk
import time

"""def select_file2():
    filetypes = (
        ('text files', '*.html'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    f = open(filename, "r")
    
    opened_timestamp= f.readline()
    opened_timestamp = opened_timestamp[4:]
    opened_timestamp = opened_timestamp[:-4]

    lien = f.readline()
    lien = lien[4:]
    lien = lien[:-4]
    comments = f.readline()
    comments = comments[4:]
    comments = comments[:-4]
    f.readline()
    title=f.readline()
    
    print(info)
    print(opened_timestamp,filename,title,lien)
    return opened_timestamp,filename,title,lien,comments

    print(children)"""


def edit():
   # Get selected item to Edit
   selected_item = tree.selection()[0]
   tree.item(selected_item, text="blub", values=(go.get(),ho.get(),io.get(),jo.get(),ko.get()))
def delete():
   # Get selected item to Delete
   selected_item = tree.selection()[0]
   tree.delete(selected_item)


def create():
    tree.insert('', 'end', text="?", values=(go.get(),ho.get(),io.get(),jo.get(),ko.get()))
def sorting():
    
    #rows = [(tree.item(item, 'values'), item) for item in tree.get_children('')]
    # if you want to sort according to a single column:
    rows = [(tree.set(item, 0), item) for item in tree.get_children('')]
    rows.sort()

    # rearrange items in sorted positions
    for index, (values, item) in enumerate(rows):
        tree.move(item, '', index)
def add():
    value = add_entry.get()
    values.append(value)
    tree.insert("", tk.END, values=(f'#{len(values)}', value, 'more', 'moar'))


def search():
    global search_entry, search
    search = Toplevel(root)
    search.title("Rechercher")
    search.geometry("400x200")
    search_frame = LabelFrame(search, text="Rechercher par nom")
    search_frame.pack(padx =10, pady=10)
    search_entry = Entry(search_frame, font=("Bahnschrift",18))
    search_entry.pack(padx=20,pady=20)
    search_button = Button(search,text ="Chercher", command=search_records)
    search_button.pack(padx=20,pady=20)
    
def search_records():
    bar = search_entry.get()
    search.destroy()
    for records in tree.get_children():
        tree.delete(records)
    
root = tk.Tk()
root.title("In-ventory")

value = StringVar() 
value.set("Objet")
go = Entry(root, textvariable=value)
go.grid(row = 2, column = 1)
value1 = StringVar() 
value1.set("Location")
ho = Entry(root, textvariable=value1)
ho.grid(row = 2, column = 0)
value = StringVar() 
value.set("Qté")
io = Entry(root, textvariable=value)
io.grid(row = 3, column = 1)
value1 = StringVar() 
value1.set("Temps")
jo = Entry(root, textvariable=value1)
jo.grid(row = 3, column = 0)

value1 = StringVar() 
value1.set("Utilisations")
ko = Entry(root, textvariable=value1)
ko.grid(row = 4, column = 0)

edit_btn = tk.Button(root, text="Editer", command=edit)
edit_btn.grid(row = 5, column = 1)
del_btn = tk.Button(root, text="Supprimer", command=delete)
del_btn.grid(row = 5, column = 0)
#ret_btn = ttk.Button(root, text="Retour", command=back)
#ret_btn.grid(row = 3, column = 1)
cre_btn = tk.Button(root, text="Créer ligne", command=create)
cre_btn.grid(row = 6, column = 0)
srt_btn = tk.Button(root, text="Trier", command=sorting)
srt_btn.grid(row = 6, column = 1)

#sve_btn = ttk.Button(root, text="Sauvegarder", command=save1)
#sve_btn.grid(row = 4, column = 2)

values = []



lb1 = tk.Label(root, text="Search:")
lb1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
search_entry = tk.Entry(root, width=15)
search_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E, rowspan=1)
btn = tk.Button(root, text="search", width=10, command=search)
btn.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

add_lb = tk.Label(root, text="add:")
add_lb.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
add_entry = tk.Entry(root, width=15)
add_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E, rowspan=1)
btn1 = tk.Button(root, text="add", width=10, command=add)
btn1.grid(row=1, column=0, padx=10, pady=10, rowspan=2)

# treeview
tree = ttk.Treeview(root, height=25)
tree["columns"] = ("one", "two", "three", "four","five")
tree.column("one", width=120)
tree.column("two", width=160)
tree.column("three", width=130)
tree.column("four", width=160)
tree.column("five", width=160)
tree.heading("one", text="Objet")
tree.heading("two", text="Location")
tree.heading("three", text="Quantité")
tree.heading("four", text="temps")
tree.heading("five", text="Utilisation")
tree["show"]="headings"
tree.grid(row=0, column=2, rowspan=7, pady=20)

root.geometry("960x570")
#Tk.attributes("-fullscreen", True)

if __name__ == '__main__':

    root.mainloop()