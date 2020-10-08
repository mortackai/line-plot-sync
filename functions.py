import csv
def csvFindRow(file, columnNumber, searchNumber):

    csv_f = csv.reader(open(file))
    next(csv_f)
    
    for row in csv_f:
        if float(row[columnNumber]) > searchNumber:
            pass
        else:
            return(csv_f.line_num)
            break

def csvImport():
    for i in range:
        csv_f = csv.reader(open(loopfilename))

def getListFromFile(filename):
	files = []
	with open("filelist.txt") as index:
		for line in index:
			files.append(line.strip('\n'))
	return files

# 2nd Stage Min Temp
def minTemp(fileList, column):
    for i, file in enumerate(fileList, start = 0):
        print(fileList[i][0])
        currentFile = csv.reader(open('test-curves/curve1.csv'))# + fileList[i][0]))
        currentRow = fileList[i][1]
        print(currentRow[0][0])
        for row in currentFile:
            if row[1] < x:
                x = row[1]
            else:
                pass
        print(x)
            

# 2nd Stage Average Temp
#def avgTemp():

# Return Max Temp
#def maxTemp():
