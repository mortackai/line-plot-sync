import csv
import pandas as P
from functions import csv_find_row
from functions import get_list_from_file
from functions import get_max_shift_index
from functions import combine_columns_of_files

columnHeaders = ['CH1_LSD', 'CH1_AVG', 'CH1_USD', 'CH1_MAX', 'CH1_MIN', 'CH2_LSD', 'CH2_AVG', 'CH2_USD', 'CH2_MAX', 'CH2_MIN']


curveList = get_list_from_file('filelist.txt')

maxIndexShift = get_max_shift_index(curveList)

print(combine_columns_of_files(maxIndexShift, curveList, "2ndStgSens"))

















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
