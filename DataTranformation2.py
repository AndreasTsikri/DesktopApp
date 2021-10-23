import os#executing os commands
import time
from contextlib import contextmanager#using context manager decorator
import re#using regural expressions!
import json

#functions & generators

@contextmanager
def go(folderToGo):#this func for going from onfile making something and then getting back to original!
    try:
        cwd=os.getcwd()
        os.chdir(folderToGo)
        yield
    finally:
        os.chdir(cwd)
        
def open_clean_return_lines(filename):
    with open(filename,'r') as f:
        lines=f.readlines()   
    lines=lines[:30]    
    
    cleanLines=[line for line in lines if line!='\n']
    cleanLines=cleanLines[:3]
    return cleanLines
    
def badOrGood(fileLines):    
    keyword='Aριθμός'
    keyword2='ΑΡΙΘΜΟΣ'
    keyword3='Αριθμός'
    found=False
    for line in fileLines:
        if (re.search(r"{}".format(keyword),line)) or (re.search(r"{}".format(keyword2),line)) or (re.search(r"{}".format(keyword3),line)):
            
                found=True            
    return found
    
def myDecoder(fileLines):
    fixedEncodedlines=[]####list where each element is a line!
    for line in fileLines:
            l=line.encode("ISO-8859-1",errors='ignore').decode("windows -1253").encode("utf-8")
            #print(l.decode("utf-8"))
            fixedEncodedlines.append(l.decode("utf-8"))
            #an to print einai ok-->fixedEncodedFile.append(l)
    return fixedEncodedlines
   
def clean_word(word):
    cleanword=''
    for i in word:
        if i.isalpha():cleanword+=i
    return cleanword
    
#main
with go('words'):
    filesToTransform=os.listdir()  
    dirpath=os.path.abspath(os.getcwd())
    #print(dirpath)
    """  
print('files for transformatio:\n')
print(filesToTransform)
"""
time.sleep(5)
#clean files that ends-with 'A.doc' or doesnt end with .doc or doesnt start with 't'!
for i,files in enumerate(filesToTransform):
    if files.endswith('A.doc') or not files.endswith('.doc') or not files.startswith('t'):
        filesToTransform.remove(files)
        #print(files,filesToTransform[i:i+5])

"""
paths=[]
with go('words'):
    for file in filesToTransform:
        path=os.path.abspath(os.getcwd()+'/{}'.format(file))
        paths.append(path)
print(paths)
"""

print(len(filesToTransform))


#print(dic)

#input("Check dic if is ok ,then,Press Any key to continue...")

#del(paths)#delete paths memory

#Tranformation
print('Start transformation with antiword')
for file in filesToTransform:
    #print('file transforming--\n{}'.format(file))    
    #print(file)
    try:
    	os.system('antiword ./words/{} > ./txts/{}.txt'.format(file,file))   	
    except:
    	print('probl')
"""with go('txts'):
	for file in filesToTransform:
		cleanlines=open_clean_return_lines('./{}.txt'.format(file))
		if len(cleanlines)<2:
			filesToTransform.remove(file)"""

#find 'praksi' in files if they are good,else
#i 'fixing' them and search for 'praksi' again!
print('all ended good!!!!!')
print(len(filesToTransform))

with go('txts'):    
    praksh_forEachFile=[]    
    #for file in os.listdir():
    for file in filesToTransform:
        #print(file)
        
        cleanlines=open_clean_return_lines('./{}.txt'.format(file))#return 0 if lines are lower than 3
        found=badOrGood(cleanlines)
        #print(found)
        if len(cleanlines)<3:
            filesToTransform.remove(f"{file}")
            #praksh_forEachFile.append('ok')       
        else:
            if found :
                praksh_forEachFile.append(cleanlines[1].replace('\n',''))            
            if not found :#file is bad            
                #print('----fixed text-----\n')
                newCleanedLines=myDecoder(cleanlines)
                #print(newCleanedLines)
                praksh_forEachFile.append(newCleanedLines[1].replace('\n',''))           
print('finito')
#print(len(filesToTransform))
#print(len(praksh_forEachFile))
#path
paths=[f"{dirpath}{file}" for file in filesToTransform]
#print('len of path:')
#print(len(paths))
#print(len(praksh_forEachFile))
#dictionary in form {name:path}
#dic={filesToTransform[i]:paths[i] for i in range(len(paths))}
#print('dictionary is :\n')

print('praksi is :\n')
#print(praksh_forEachFile)
print(len(praksh_forEachFile))
print(len(filesToTransform))
print(len(paths))

##debug
"""
with go('txts'):
    for file in filesToTransform:
        cleanlines=open_clean_return_lines('./{}.txt'.format(file))#return 0 if lines are lower than 3
        if len(cleanlines)<3:   
           
            print(os.path.getsize('./{}.txt'.format(file)))
            print(cleanlines)
            print(file)
"""
input("Check  if praksi is ok ,then,Press Any key to continue...")

#fix praksh to be one word 
for i,praksh in enumerate(praksh_forEachFile):
    praksh_forEachFile[i]=clean_word(praksh)

#final dictonairy in format {name : {path:praksi}}
fdic={filesToTransform[i]:{paths[i]:praksh_forEachFile[i]} for i in range(len(paths))}

print('final dictionary is :\n')
print(fdic)

input("Check final dic if is ok ,then,Press Any key to continue...")

#exctract dict to json file

with open('result.json', 'w') as fp:
    json.dump(fdic, fp)

print('finished!!')
