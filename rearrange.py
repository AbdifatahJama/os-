'''This script wants to rearrange different files types into specfic folders

For example: -> word docs are moved to a word document folder
             -> pdf are moved to a pdf document folder
             -> etc 
'''
import os
from posixpath import join
import shutil

print(os.getcwd())

'''Change current working directory'''

wordFolder = 'C:\\Users\Abdifatah\Documents\Word folder'
pdfFolder = 'C:\\Users\Abdifatah\Documents\PDF folder'
textFile = 'C:\\Users\Abdifatah\Documents\Text Files'
imageFolder = 'C:\\Users\Abdifatah\Documents\Images folder'
powerpointFolder = 'C:\\Users\Abdifatah\Documents\Powerpoint Folder'
mapleFolder = 'C:\\Users\Abdifatah\OneDrive\Documents\Collection\Maple Folder'

def action():
  '''Change current working directory'''
  os.chdir('C:\\Users\Abdifatah\OneDrive\Documents\Collection')
  PATH = 'C:\\Users\Abdifatah\OneDrive\Documents\Collection'
  list = os.listdir(PATH) # Find list of dirs within the directory
  if len(list) > 0: # Check list size to see if any files or folders are within it
    for item in list: # Iterates through each item within the list
      if os.path.isfile(os.path.join(PATH,item)): # Checks if the path is a file or directory
        '''Once it is established the path is a file, the extenstion should be looked'''
        split = os.path.splitext(item)[1] # Splits file name and gets extension using indexing of the tuple
        print(split)
        '''Using if statements on each iteration of the loop to check the extension and then move to the relavant folder destination that is pre set at the top of the script'''
        if split == '.docx': 
          print('Word document')
          shutil.move(item,wordFolder)
        
        elif split == '.pdf':
          print('PDF document')
          shutil.move(item,pdfFolder)
        
        elif split == '.txt' or '.csv':
          shutil.move(item,textFile)
        
        elif split == '.pptx':
          print('Powerpoint')
          shutil.move(item,powerpointFolder)
        
        elif split == '.jpg' or '.png':
          print('Image File')
          shutil.move(item,imageFolder)
        
        elif split == '.mw':
          print('Maple file')
          shutil.move(item,mapleFolder)
          
        else:
            print('Other file')
            
      
      else: # Should refactor and send anyone files into a folder called 'Unknown folder'
        '''If extension is not reconised by script we assume it is a folder and do not move'''
        print('Cannot move folders')
  
  else:
    print('Folder is empty')
    
action()
