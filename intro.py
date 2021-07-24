'''Operating system of a computer controls how a computer runs and saves programs

This can be manipulated and controlled using the os module 
'''
from genericpath import isfile
import os
'''Gets current working directory'''
cwd = os.getcwd() 
print(cwd)

'''Can get the list of directories within a dictory(file). Empty argument assumes current working directory or a PATH can be added'''

'''Currently current working directory has one directory within it'''
list = os.listdir("C:\\")
print(list)

'''Can create a single directory'''

def make_dir():
  os.mkdir('folder1') # makes directory called folder1 in current working as PATH not specified
  

'''Can aslo make directories within directories(folders that open folders)

folder2 
       |innerfolder2
                    |innerinnderfolder2
'''

def make_layers_dir():
  os.makedirs("Folder2/innerFolder2/innerFolder2")


'''directories can be made but also deleted. if path not given current working directory is assumed. can only delete empty directories without anuything inside'''

def delete_dir():
  pass

'''also can rename a directories name by speciying original name and new name'''

def rename():
  os.rename('folder1','Folder1')

'''can also look into the folders and files a directory has using walk()

walk gives you three values at a time current path,directory name,file name
'''

def walk():
  '''able to iterate/walk through each path file '''
  for cur_dir,dir_name,file_name in os.walk('C://Users\Abdifatah\OneDrive\Documents\VS SETUP'):
    print('Current directory:',cur_dir)
    print('directory name:',dir_name)
    print('File name:',file_name)
    print('-----------')
    
walk()

# def list(PATH = ''):
#   return os.listdir(PATH)

# print(list('C://Users\Abdifatah\OneDrive\Documents\VS SETUP'))

'''can also breakdown a directory or files name from its path

from its basename
from its dirname
'''

basename = os.path.basename('C://Users\Abdifatah\OneDrive\Documents\VS SETUP\matplotlib')
print(basename)

dirname = os.path.dirname('C://Users\Abdifatah\OneDrive\Documents\VS SETUP\matplotlib')
print(dirname)

'''Can also split a pathname basename and dirname'''

split = os.path.split('C://Users\Abdifatah\OneDrive\Documents\VS SETUP\matplotlib')
print(split) # returns array with dirname and basename

'''The path can be checked for it exists which returns a boolean'''

exist = os.path.exists('C://Users\Abdifatah\OneDrive\Documents\VS SETUP\matplotlib')
print(exist)

'''Can check if path goes to a directory to file'''

is_dir = os.path.isdir('C://Users\Abdifatah\OneDrive\Documents\VS SETUP')
print(is_dir)

is_file = os.path.isfile('C://Users\Abdifatah\OneDrive\Documents\VS SETUP\random_plot_data.csv.txt')
print(is_file)

'''script has been working with the current directory so far but this can be changed'''

if os.path.isdir('C://Users/Abdifatah/OneDrive/Documents/New folder (3)'):
  os.chdir('C://Users/Abdifatah/OneDrive/Documents/New folder (3)')
  print('Current working directory changed to:',os.path.basename('C://Users/Abdifatah/OneDrive/Documents/New folder (3)'))

'''can now produce new directory in current working directory'''

'''home environ

enviroment variables are pre initialised contasts that have a key and value. Contains m
information about the type of computer to the username home path etc.
'''

print(os.environ.get('HomePath'))

'can create new file in home directory'

PATH = '__text__.txt' # add this txt file to the home directory path

'''can join two paths togethor without concatanating. This adds the path slashes automatically'''
print(os.path.join(os.environ.get('HomePath'),PATH))
 


