from intro import PATH
import os


'''This small script wants to automate deleting all directories within the Documents PATH that have no inner directories and no files'''

'''freestyle'''

# def make_dir():
#   os.mkdir('C:\\Users\Abdifatah\OneDrive\Documents\practicefolder')

# '''Change to the practice folder directory'''
# os.chdir('C:\\Users\Abdifatah\OneDrive\Documents\practicefolder')

# def add_dir(number = 0):
#   '''Adds directories in the current working directory using a for loop'''
#   for i in range(number):
#     os.rmdir()


'''First need to change directories to Documents Path'''

PATH = 'C:\\Users\Abdifatah\OneDrive\Documents'
os.chdir(PATH)

def walk_cwd():
  return os.walk(PATH) # returns genarator object that can be iterated

list = []

def iter():
  gen = walk_cwd()
  i = 0
  for cur_dir,dir_name,file_name in gen:
    if len(dir_name) == 0 and len(file_name) == 0:
      os.rmdir(cur_dir)
      list.append(cur_dir)
      
    else:
      print('FINE')
      
  print(str(len(list)) + ' ' + 'files deleted')
    
  length = len(list)
  print(length)
  
  


iter()










