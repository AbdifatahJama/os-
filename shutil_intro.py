'''Shutil is high level file operation module for copying removing etc'''
import shutil
import os
from sys import path

src = 'C:\\Users\Abdifatah\OneDrive\Documents\A'
dest = 'C:\\Users\Abdifatah\OneDrive\Documents\B'

os.chdir(src) # Changed current working directory to directory A

files = os.listdir(src) # Lists directories and files in A directory
print(files)
# for file in files:
#   '''Iterates through each text file to read the contents
#      When a folder is reached permision is denied at a folder cannot be opened to be read
#   '''
#   with open(file,'r') as fp:
#     print(file,fp.read())
    
'''Copying files from source to dest folder'''

for file in files:
  '''Iterates through each file in directory and copies into second directory
  Note: If a directory already has file or directory already within it that file or directory is overwritten for the newly copied file/directory. This prevents a build of the same files and directories
  '''
  pass
  # shutil.copy(file,dest) 
  
'''Moving - allows files to be moved from source to destination. This will remove files from the source permeantely

If destination only contains files from source the source files cannot be moved as the destination already contains these files
'''

def move(): 
  '''Moves files from One directory to another. The directory where the files are moved from lose these files'''
  for file in files:
    print(file)
    if os.path.isfile(file):    
     shutil.move(file,dest)
     
    else:
      pass
      
move()








  
  
