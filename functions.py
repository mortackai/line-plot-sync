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
	files
