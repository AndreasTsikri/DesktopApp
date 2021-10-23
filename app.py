import tkinter as tk
from tkinter import messagebox
from dbClass import *
import os

#functions
def search():
    entity=entry.get()
    print(entity)
    insert(entity)
    return
def insert(entity):
    textlist.set(entity)
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
	
def showSelected():
    sel_label.config(text=listbox.get(tk.ANCHOR))
    #print(listbox.get(tk.ANCHOR))
#database functions
def fetch():	
	val=v.get()
	if val==1:
		choice='id'
		messagebox.showinfo('WAIT:', f'You Selected {choice}.NO SEARCH BY ID!')
	if val==2:
		choice='name'
		pat=entry.get()
		result=db.searchby_name(pat)
		print(result)
		textlist.set(result)
	if val==3:
		choice='path'
		pat=entry.get()
		result=db.searchby_path(pat)
		print(result)
		textlist.set(result)
	if val==4:
		choice='praksi'
		print(choice)
		pat=entry.get()
		result=db.searchby_praksi(pat)
		print(result)
		textlist.set(result)
def showpraksi():	
	query='select distinct praksi from mytabletest;'
	r=db.make_query(query)
	praksi_textlist.set(r)
	
def SearchSelected():
    selected_praksi=praksi_listbox.get(tk.ANCHOR)
    #print(selected_praksi[0])
    query=f'SELECT * FROM mytabletest WHERE praksi="{selected_praksi[0]}";'
    r=db.make_query(query)
    print(r)
    textlist.set(r)
    
#windows opene!
def open_word_windows():#works only on windows!
	
	
	word_dir=r'C:\Users\mrsAgapi\Desktop\app'#path of working directory
	fileName=listbox.get(tk.ANCHOR)[1]#nameoffile
	filepath=f"{word_dir}\\{fileName}"
	print(filepath)
	try:
		os.startfile(filepath)
	except:
		print('problem:no open file')
	
	
def open_word_linux():
	#filepath=listbox.get(tk.ANCHOR)[3]
	#print(filepath)
	filepath='/home/lubuntu/Desktop/app/txts/t6.doc'
	cmd= f'featherpad {filepath}.txt'
	try:
		os.system(cmd)
	except:
		print('problem:no open file')

	
"""
#create radio-Button according to how many unique entries as a praksi!


run=db.make_query('select distinct praksi from mytabletest;')
insert(run)

"""

#db
db=Database('tdb.db')

#root
app=tk.Tk()
app.geometry('700x700')

praksi_button_isPressed=True
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

#set-button -list of praksis to search
"""set_btn=tk.Button(text='Set',width=15,bg='black',fg=('yellow'),command=fetch)
set_btn.pack()"""
#label-of listbox columns
lb=tk.Label(app,width=40,text='id |name |path |praksi ')
lb.pack()

#listbox
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
show_praksi_button=tk.Button(text='show praksis!',width=15,bg='black',fg=('red'),command=showpraksi)
show_praksi_button.pack()

#2nd listbox (shows if praksi-button is pressed) 
praksi_textlist=tk.StringVar()
praksi_listbox=tk.Listbox(app,width=45,bg='green',fg='black',listvariable=praksi_textlist)
praksi_listbox.pack()

#select- praksi Label
select_praksi_label=tk.Label(app,text='select,then ,Press "select praksi" to see results in red!!',width=40)
select_praksi_label.pack()
##button-to-show praksi

select_praksi_button=tk.Button(text='select praksi',width=15,bg='black',fg=('red'),command=SearchSelected)
select_praksi_button.pack()


##button-OPEN WORD!
open_button=tk.Button(text='open file',width=25,bg='red',fg=('green'),command=open_word_windows)
open_button.pack()

"""
insert_item=['apple','orange','anana']
text.set(insert_item)
"""

#start of app
if __name__=="__main__":
    app.mainloop()



