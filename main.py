import csv
import pandas as P
from functions import csv_find_row
from functions import get_list_from_file
from functions import get_max_shift_index
from functions import combine_columns
from functions import lower_std_dev
from functions import average
from functions import upper_std_dev
from functions import maxdf
from functions import mindf

columnHeaders = ['CH1_LSD', 'CH1_AVG', 'CH1_USD', 'CH1_MAX', 'CH1_MIN',
                 'CH2_LSD', 'CH2_AVG', 'CH2_USD', 'CH2_MAX', 'CH2_MIN']

curveList = get_list_from_file('filelist.txt')

maxIndexShift = get_max_shift_index(curveList)

secondStgSensdf = combine_columns(maxIndexShift, curveList, "2ndStgSens")
firstStgSensdf = P.DataFrame(combine_columns(maxIndexShift, curveList, "1stStgSens"))
Tubedf = P.DataFrame(combine_columns(maxIndexShift, curveList, "Tube"))
secondStgHeatdf = P.DataFrame(combine_columns(maxIndexShift, curveList, "2ndStgHeat"))
firstStgHeatdf = P.DataFrame(combine_columns(maxIndexShift, curveList, "1stStgHeat"))

outputdf = P.DataFrame()

outputdf["CH1_LSD"] = lower_std_dev(secondStgSensdf)
outputdf["CH1_AVG"] = average(secondStgSensdf)
outputdf["CH1_USD"] = upper_std_dev(secondStgSensdf)
outputdf["CH1_MAX"] = maxdf(secondStgSensdf)
outputdf["CH1_MIN"] = mindf(secondStgSensdf)
outputdf["CH2_LSD"] = lower_std_dev(firstStgSensdf)
outputdf["CH2_AVG"] = average(firstStgSensdf)
outputdf["CH2_USD"] = upper_std_dev(firstStgSensdf)
outputdf["CH2_MAX"] = maxdf(firstStgSensdf)
outputdf["CH2_MIN"] = mindf(firstStgSensdf)

outputdf.to_csv('test.csv', index=False)
