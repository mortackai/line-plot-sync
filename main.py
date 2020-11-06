import csv
import pandas as P
from functions import csv_find_row
from functions import get_list_from_file

columnHeaders = ['CH1_LSD', 'CH1_AVG', 'CH1_USD', 'CH1_MAX', 'CH1_MIN', 'CH2_LSD', 'CH2_AVG', 'CH2_USD', 'CH2_MAX', 'CH2_MIN']
csvHeaders = ["DateTime", "2ndStgSens", "1stStgSens", "Tube", "Null", "2ndStgHeat", "1stStgHeat", "AIO 1", "AIO 2", "AIO 3", "AIO 4", "DIO", "Relays", "V1", "V2", "V3"]

curveList = get_list_from_file('filelist.txt')
indexShift = []
df2 = P.DataFrame()

for file in curveList:
    df = P.read_csv(file)
    indexShift.append(csv_find_row(df,1,290))
    
maxIndexShift = max(indexShift)

for file in curveList:
    df = P.read_csv(file)                                               ### Read file name from list and import to dataframe
    df.columns = csvHeaders                                             ### Rename column headers
    df = df.shift(periods=maxIndexShift - (csv_find_row(df,1,290)))     ### shift index of dataframe to match one that started the latest
    df2[file] = df["2ndStgSens"]                          ### append data from a row to the summary dataframe

df2.to_csv('test.csv', index=False)

















#### LOWER STANDARD DEVIATION
##DataFrame.mean() - DataFrame.std()
##
#### AVERAGE
##DataFrame.mean()
##
#### UPPER STANDARD DEVIATION
##DataFrame.mean() + DataFrame.std()
##
#### MAX
##DataFrame.max()
##
#### MIN
##DataFrame.min()
