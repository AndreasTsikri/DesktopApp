import tkinter as tk
from tkinter import messagebox
from dbClass import *
import os

#-----------
#functions
#-----------

def search():
    entity=entry.get()
    print(entity)
    insert(entity)
    return

def insert(entity):
    textlist.set(entity)
    return

def showSelected():
    sel_label.config(text=listbox.get(tk.ANCHOR))
    return

def showpraksi():
    query='select distinct praksi from mytabletest;'
    r=db.make_query(query)
    praksi_textlist.set(r)
    return

def SearchSelected():
    selected_praksi=praksi_listbox.get(tk.ANCHOR)
    query=f'SELECT * FROM mytabletest WHERE praksi="{selected_praksi[0]}";'
    r=db.make_query(query)
    print(r)
    textlist.set(r)
    return

def ShowChoices():
    val=v.get()
    if val==1:
        choice='id'
    if val==2:
        choice='name'
    if val==3:
        choice='path'
    if val==4:
        choice='praksi'
    return messagebox.showinfo('PythonGuides', f'You Selected {choice}.')

def fetch():
    val=v.get()
    if val==1:
        choice='id'
        messagebox.showinfo('WAIT:', f'You Selected {choice}.NO SEARCH BY ID!')
    if val==2:
        choice='name'
        pat=entry.get()
        result=db.searchby_name(pat)
        #print(result)
        textlist.set(result)
    if val==3:
        choice='path'
        pat=entry.get()
        result=db.searchby_path(pat)
        #print(result)
        textlist.set(result)
    if val==4:
        choice='praksi'        
        pat=entry.get()
        result=db.searchby_praksi(pat)
        #print(result)
        textlist.set(result)
    return

#windows opener!
#works only on windows!
def open_word_windows():
    word_dir=r'C:\Users\mrsAgapi\Desktop\app'#path of working directory
    fileName=listbox.get(tk.ANCHOR)[1]#nameoffile
    filepath=f"{word_dir}\\{fileName}"
    print(filepath)
    try:
        os.startfile(filepath)
    except:
        print('problem:no open file')
    return

#linux opener!
#works only on linux!

def open_word_linux():    
    #filepath=f"/home/lubuntu/Desktop/app/txts/{filename}"
    #print('filepath')
    #print(filename)
    #filepath='/home/lubuntu/Desktop/app/txts/t6.doc'
    filepath=listbox.get(tk.ANCHOR)[2]
    #change featherpad with your text editor to open file!!
    cmd= f'featherpad {filepath}.txt'
    try:
        os.system(cmd)
    except:
        print('problem:no open file')
    return

#MAIN
#db
db=Database('tdb.db')

#root
app=tk.Tk()
app.geometry('800x800')
app.minsize(width=750,height=750)
#frame
fr=tk.Frame(app)
fr.pack()

#radio-Button 1
v = tk.IntVar()
rd1=tk.Radiobutton(fr,text="id",variable=v,value=1,command=ShowChoices).pack(anchor="w")
rd2=tk.Radiobutton(fr,text="name.doc",variable=v,value=2,command=ShowChoices).pack(anchor="w")
rd3=tk.Radiobutton(fr,text="path",variable=v,value=3,command=ShowChoices).pack(anchor="w")
rd4=tk.Radiobutton(fr,text="praksi",variable=v,value=4,command=ShowChoices).pack(anchor="w")

#search entry
entry=tk.Entry(app,width=15,text='Click to Search')
entry.pack()

#buttor search
btn=tk.Button(text='Search',width=15,bg='black',fg=('yellow'),command=search)
btn.pack()

#label-of listbox columns
lb=tk.Label(app,width=40,text='id |name |path |praksi ')
lb.pack()

#1st listbox
insert_item=[]
textlist=tk.StringVar(insert_item)
listbox=tk.Listbox(app,width=45,bg='red',fg='black',listvariable=textlist)
listbox.pack()

#select-button
sel_btn=tk.Button(text='show',width=15,bg='black',fg=('yellow'),command=showSelected)
sel_btn.pack()

#selected label from listbox1
sel_label=tk.Label(app)
sel_label.pack()

#show-praksi Label
show_praksi_label=tk.Label(app,text='Press "show praksi" to see results below',width=40)
show_praksi_label.pack()

#button-to-show psaki
show_praksi_button=tk.Button(text='show praksi',width=15,bg='black',fg=('red'),command=showpraksi)
show_praksi_button.pack()

#2nd listbox (shows data if praksi-button is pressed) 
praksi_textlist=tk.StringVar()
praksi_listbox=tk.Listbox(app,width=45,bg='green',fg='black',listvariable=praksi_textlist)
praksi_listbox.pack()

#select- praksi Label
select_praksi_label=tk.Label(app,text='select,then ,Press "select praksi" to see results in red!!',width=40)
select_praksi_label.pack()

#button-to-select praksi
select_praksi_button=tk.Button(text='select praksi',width=15,bg='black',fg=('red'),command=SearchSelected)
select_praksi_button.pack()

#button-OPEN WORD!
open_button=tk.Button(text='open file',width=25,bg='red',fg=('black'),command=open_word_linux)#change command:open_word_windows for windows machine!
open_button.pack()

#start of app
if __name__=="__main__":
    app.mainloop()
