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

def moveImg(filetype,verificationtype):
    try:
        os.mkdir(directory+'verified')
        os.mkdir(directory+'corrupt')
        print('Folders created - verified & corrupt')
    except:
        pass
        
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
moveImg(filetype.upper(),"verified")
moveImg(filetype.lower(),"verified")
moveImg(filetype.upper(),"corrupt")
moveImg(filetype.lower(),"corrupt")
input("Finished")