import sys
import os
import magic
import shutil 

mime_type = magic.Magic(mime=True)

try:

    path = sys.argv[1]
    if os.path.isdir(path):
        
        if not os.path.isdir(path+'/aplication'): # Checks if there are folders where the files will be sent
            os.mkdir(path+'/aplication')
        if not os.path.isdir(path+'/audio'):
            os.mkdir(path+'/audio')
        if not os.path.isdir(path+'/text'):
            os.mkdir(path+'/text')
        if not os.path.isdir(path+'/image'):
            os.mkdir(path+'/image') 
        if not os.path.isdir(path+'/font'):
            os.mkdir(path+'/font')       
        
        files = os.listdir(path)                #Lists the files, checks if they are files, takes the mimy type 
        for file in files:                      #and forwards it to the respective folder
            if os.path.isfile(path+f"{file}"):
                type_of_file_compost = mime_type.from_file(path+f"{file}")
                type_of_file = type_of_file_compost.split("/")
                shutil.move(path+f"{file}", path+f"{type_of_file[0]}")
            else:
                print("Invalid file!")
    else:
        print("Typed path is not a directory!")
except:
    print("File verification failed!")