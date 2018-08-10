import os
#At imagesFolder,get filename and output to filenames.txt
if __name__=="__main__":
    path="./images"
    files=os.listdir(path)
    f=open("filenames.txt",'w')
    for string in files:
        f.write(string+'\n')
    f.close()