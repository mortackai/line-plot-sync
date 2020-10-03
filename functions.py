import csv
def csv_find_row(file, columnNumber, searchNumber):

    csv_f = csv.reader(open(file))
    next(csv_f)
    
    for row in csv_f:
        if float(row[columnNumber]) > searchNumber:
            pass
        else:
            return(csv_f.line_num)
            break

def csv_import():
    for i in range:
        csv_f = csv.reader(open(loopfilename))
