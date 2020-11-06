import csv
import pandas as P

# move import of file to a dataframe to another function
def csv_find_row(df, columnNumber, searchValue):
    resultIndex = df.iloc[:, 1].sub(searchValue).abs().idxmin()
    return(resultIndex)

# temp file list import, will replace with gui version of file selection
def get_list_from_file(filename):
	files = []
	with open("filelist.txt") as index:
		for line in index:
			files.append(line.strip('\n'))
	return files
