import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self,name):
        self.name=name
        self.connection=self.create_connection()
        self.table_names=[]
    #connection   
    def create_connection(self):
            connection = None
            try:
                connection = sqlite3.connect(self.name)
                print("Connection to SQLite DB successful")
            except Error as e:
                print(f"The error '{e}' occurred")
            return connection
    def create_table(self,table):#def create_table(self,table):
        try:            
            #query=f"INSERT INTO mytable(name, age, gender, nationality)  VALUES ('{data[0]}','{data[1]}','{data[2]}','{data[3]}');"
            query=f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,path TEXT,praksi TEXT);"
            self.connection.execute(query)
            
            print('succesfully create the table!')
            self.table_names.append(table)
            #return 0           
        except Error as e:
                print(e)
    def insert(self,data,table):#data is a list data =[name,praksi,path]        
        try:            
            query=f"INSERT INTO mytabletest(name, path, praksi)  VALUES ('{data[0]}','{data[1]}','{data[2]}');"
            self.connection.execute(query)
            self.connection.commit()
            print('succesfully INSERT INTO table!')
            #return 0
        except Error as e:
                print(e)
    def searchby_name(self,pattern):
        try:
            query=f'SELECT * FROM mytabletest WHERE name="{pattern}";'
            #query=f"SELECT * FROM mytabletest WHERE name='t1.doc';"
            r=self.connection.execute(query)
            result=r.fetchall()
            return result
            #return 0
        except Error as e:
                print(e)
    def searchby_path(self,pattern):
        try:
            query=f'SELECT * FROM mytabletest WHERE path="{pattern}";'
            r=self.connection.execute(query)
            result=r.fetchall()
            return result
            #return 0
        except Error as e:
                print(e)
    
    def searchby_praksi(self,pattern):
        try:
            query=f'SELECT * FROM mytabletest WHERE praksi="{pattern}";'
            r=self.connection.execute(query)
            result=r.fetchall()
            return result
        except Error as e:
            print(e)
    def make_query(self,query):
        try:            
            r=self.connection.execute(query)
            result=r.fetchall()
            return result
        except Error as e:
            print(e)
            
    def __del__(self):
        self.connection.close()
