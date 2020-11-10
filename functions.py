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

def get_max_shift_index(curveList):

    indexShift = []
        
    for file in curveList:
        df = P.read_csv(file)
        indexShift.append(csv_find_row(df,1,290))
        return(max(indexShift))

def combine_columns(maxIndexShift, curveList, columnName):
    
    csvHeaders = ["DateTime", "2ndStgSens", "1stStgSens", "Tube", "Null", "2ndStgHeat", "1stStgHeat", "AIO 1", "AIO 2", "AIO 3", "AIO 4", "DIO", "Relays", "V1", "V2", "V3"]
    df2 = P.DataFrame()
    
    for file in curveList:
        df = P.read_csv(file)                                               ### Read file name from list and import to dataframe
        df.columns = csvHeaders                                             ### Rename column headers
        df = df.shift(periods=maxIndexShift - (csv_find_row(df,columnName,290)))     ### shift index of dataframe to match one that started the latest
        df2[file] = df[columnName]                                          ### append data from a row to the summary dataframe
    return(df2)                                                             ### Return dataframe of the combined data


def lower_std_dev(df):
    df = df.mean(axis=1).subtract(df.std(axis=1))
    return(df)

def average(df):
    df = df.mean(axis=1)
    return(df)

def upper_std_dev(df):
    df = df.mean(axis=1).add(df.std(axis=1))
    return(df)

def maxdf(df):
    df = df.max(axis=1)
    return(df)

def mindf(df):
    df = df.min(axis=1)
    return(df)
