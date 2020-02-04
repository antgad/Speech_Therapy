#from os import listdir
#from os.path import isfile, join
#mypath='C://Users//Anant//Downloads//F//F01//Session1'
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(onlyfiles)

import os

path = 'D://mpstme//SEM 7//PROJECT//Datasets//Control//Male//MC01'

files1 = []
files2 = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        #if '.wav' in file:
        files1.append(os.path.join(r, file))
print(files1)
path = 'D://mpstme//SEM 7//PROJECT//Datasets//Control//Male//MC02'
for r, d, f in os.walk(path):
    for file in f:
        #if '.wav' in file:
        files2.append(os.path.join(r, file))
print(files2)