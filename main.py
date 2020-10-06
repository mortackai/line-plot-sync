import csv
from functions import csvFindRow
from functions import getListFromFile

curveList = getListFromFile('filelist.txt')

matrixA = []

for file in curveList:
    #print(file)
    #print(csvFindRow('test-curves/' + file, 1, 290))
    curvepointlist = []
    matrixA.append([file,csvFindRow('test-curves/' + file, 1, 290)])

print(matrixA)
