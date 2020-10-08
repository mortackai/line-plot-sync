import csv
from functions import csvFindRow
from functions import getListFromFile
from functions import minTemp

curveList = getListFromFile('filelist.txt')

matrixA = []

for file in curveList:
    #print(file)
    #print(csvFindRow('test-curves/' + file, 1, 290))
    curvepointlist = []
    matrixA.append([file,csvFindRow('test-curves/' + file, 1, 290)])


with open('newcsv.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['CH1_LOW', 'CH1_AVG', 'CH1_HIGH', 'CH1_MAX', 'CH2_LOW', 'CH2_AVG', 'CH2_HIGH', 'CH2_MAX'])
    thewriter.writerow([])

minTemp(matrixA,2)


    
#print(matrixA[0][0])
#print(matrixA[0][1])

