import os
import sys
arg=sys.argv[1]
#At imagesFolder,get filename and output to arg1
if __name__=="__main__":
    path="./images"
    files=os.listdir(path)
    f=open(arg,'w')
    for string in files:
        f.write(string+'\n')
    f.close()