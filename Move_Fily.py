import os 
import shutil

from_dir = 'C:/Users/SRI/Downloads'
to_dir = 'D:/Images & gif'

list_of_files = os.listdir(from_dir)
print(list_of_files)


for fn in list_of_files:
    name, ext = os.path.splitext(fn)
    print(name)
    print(ext)

    if ext == '':
        continue    
    if ext in ['.jpg','.gif','.png','.svg']:

        path1 = from_dir + '/' + fn
        path2 = to_dir + '/' + "Images & gif"  
        path3 = to_dir + '/' + "Image & gif" + fn
        print("path1", path1)
        print("path3",path3)

if os.path.exists(path2):
    print("Moving"+ fn + ".....")
    shutil.move(path1,path3)

else : 
    os.makedirs(path2)
    print("Moving"+ fn + ".....")
    shutil.move(path1,path3)
    