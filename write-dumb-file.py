import csv as shitpisser

with open('test.csv', 'w', newline='') as thefile:
	thewriter = shitpisser.writer(thefile, delimiter=' ',
																quotechar='|')
	for x in range(20):
		thewriter.writerow([x, x+2, 'Butt'])
