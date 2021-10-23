import sqlite3
from sqlite3 import Error
import json
try:
	from  dbClass import *
except:
	print('Not importing dbClass.py,please put it on the same folder with this file!')
        
#function & generators
def row_generator(dictionary):
    try:
        for nameoffile in dictionary:
            r=[]
            r.append(nameoffile)
            for path in dictionary[nameoffile]:
                r.append(path)
                r.append(dictionary[nameoffile][path])        
            yield r
    except Error as e:
        print(e)
        
#create database(or connect to it!),create table(if not exist!).table name must be ='mytabletest'!
db=Database('tdb.db')
db.create_table('mytabletest')
#read result file and make it dictionary dic!
with open("result.json","r") as f:
    dic=json.load(f)

	
#create gen object
r1=row_generator(dic)
print(r1)

#insert data to table
for nrow in range(len(dic)):
    db.insert(next(r1),'mytable24')
    print(nrow)
