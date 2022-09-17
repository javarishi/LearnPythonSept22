import os

path = '/RISHI/H2K/FileIO/demofile_x1.txt'
if os.path.exists(path):
    print("This is already exists")
else:
    filex = open(path, 'x')
    filex.close()
    print("File is created")
# delete the file
os.remove(path)
path_dir = '/RISHI/H2K/FileIO/TEMP'
# os.mkdir(path_dir)
if os.path.exists(path_dir):
    print("Directory is created ", path_dir)

#os.rmdir(path_dir)

if not os.path.exists(path_dir):
    print("Directory is removed ", path_dir)

target_dir = "/RISHI/H2K/FileIO"
files = os.listdir(target_dir)
for eachFile in files:
    if 'csv' in eachFile:
        print(eachFile)
        if os.path.exists(path_dir):
            print("Transfer files here")
        else:
            os.mkdir(path_dir)
        src_path = target_dir + "/" + eachFile
        dest_path = path_dir + "/" + eachFile
        os.rename(src_path, dest_path)