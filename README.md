# DesktopApp
Desktop app using Tkinter for GUI and sqlite for database management system.
Developed completely on linux systems.
It will be used on windows.

```diff
-Description of the app:
```
This app provides an interactive environment (or a way!) of searching a big amount of files(word files) that are stored in a specific folder in the HD.Files contain informations that are needed and all have some specific detail that we want to search so we can identify the file(greek word 'praksi').Its not necessary to search only by this detail but this was the original purpose of development!
we create a database with the details of the files,providing a way to the user to search whatever detail they want(here we have implemented the 'praksi' search as far as today)  along with the path of the file.
When user decide the file he wants , hw is in position to open the file!


AppPreview contains snapshots of the app.

Db-mother-PLAN.ctd is a file describing the workflow of the app,created using cherry-tree application.

Instructions for running the application:
	
	-we need to have two more folders(they are not uploaded in this repository)-->"txts" , "words"
		-"words" contains initial word documents
		-"txts" contains the after-processing files
		-for this transformation we use the 'antiword' package in linux((sudo) apt get-install antiword)

	- we run 'Datatransformation2.py' for proccesing the word docs
	-The result of 'Datatransformation2.py' is a "result.json" filei(it is not uploaded in this repository).This file will be processed by 'db_creation.py' for database generation
	-'db_creation.py' creating the ''tdb.db''(database-file that can be moved from system to system) inside sqlite3 system.(Sqlite3 installed in linux using (apt-get install sqlite3)
	-'dbClass.py' contains database class.
	-*** ''tdb.db'' (database file) ,'app.py' ,'dbClass.py' are the only files that are necessary for RUNNING the app!(so the only thing to run the app is a database,a table with data,'app.py','dbClass.py' and modify them accordingly to fetch specific cols or rows!)***
	-'dbClass.py' , 'db_creation.py' must be in the same folder when  'db_creation.py' is executed.
	-we run 'app.py' that contains the GUI.(for installing tkinter --> (sudo) apt-get install python3-tk)
	-'dbClass.py' ,'app.py' mut be on the same folder when 'app.py' is executed

