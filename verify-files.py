#Verify that img-files are valid images and not corrupt. If corrupt, put in corrupt folder, if verified put in verified folder
#Instructions:
#Put this file in the folder that should be sorted. Errors often related to too small files, remove or move these.
from os import listdir
from PIL import Image
import os
import glob
import time

directory = './'
filetype = 'jpg'
enterFiletype = input('Enter filetype default jpg: ')

if len(enterFiletype)<2:
    filetype='jpg'
else:
    filetype=enterFiletype

def archiveSmallImg(filetype):
    try:
        os.mkdir(directory+'tinyfiles')
        print('Folder created - tinyfiles')
    except:
        print('Couldnt create folder tinyfiles')
    
    for filename in listdir(directory):
        if filename.endswith('.'+filetype):
            try:
                if os.path.getsize(filename) < 50*1024:
                    os.rename(os.path.join(directory,filename),os.path.join(directory,"tinyfiles/"+filename))
            except:
                pass
def moveImg(filetype,verificationtype):
    try:
        os.mkdir(directory+'verified')
        os.mkdir(directory+'corrupt')
        print('Folders created - verified & corrupt')
        print('Verifying files now.......')
    except:
        print('Couldnt create folder. Permission?')
        
    for filename in listdir(directory):
        if filename.endswith('.'+filetype):
            #print("Working on file: "+filename)
            
            try:
              if verificationtype=="verified":
                img = Image.open(directory+filename) # open the image file
                img.verify() # verify that it is, in fact an image                
              
              os.rename(os.path.join(directory,filename),os.path.join(directory,verificationtype+"/"+filename))
              
              #print("moved Image: "+filename)
              
            except (IOError, SyntaxError) as e:
                pass
              #print("error file:"+filename)
              #print('Bad file:', filename) # print out the names of corrupt files
              #os.rename(filename, directory+"corrupt/"+filename)
            except:
                pass
print(archiveSmallImg(filetype))
moveImg(filetype.upper(),"verified")
moveImg(filetype.lower(),"verified")
moveImg(filetype.upper(),"corrupt")
moveImg(filetype.lower(),"corrupt")
input("Finished")
