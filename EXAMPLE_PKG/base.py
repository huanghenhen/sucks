import os
import glob
import re

class salad ():
    
    def __init__(self):
        self.path = ''
        self.item=[]
        self.numbers=[]
        
    def write (self, path,salad, n_items):
        self.path=path
        print (self.path)
        
        assert len(salad) == len(n_items), "Stupid"
        for k in range(len(salad)):
            print(salad[k],n_items[k])
            for j in range(n_items[k]):
                file_name=salad[k]+str("{:0>2}".format(j))+'.salad'
                f=open(os.path.join(self.path, file_name),"w+")
                f.close()
        
    def read(self, path):
        flist=glob.glob(os.path.join(path, '*.salad'))
        a=[]
        for file in flist:
            pattern=r'(\w+)(\d\d).salad'
            a.append(re.findall(pattern, file))
        return a
