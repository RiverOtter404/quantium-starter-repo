import csv
import os

def addDataToArray(array, data):
    for item in data:
        if item[0] == 'pink morsel':
            price = float(item[1][1:])
            sales = price * float(item[2])
            array.append([sales, item[3], item[4]])


paths = os.listdir(os.curdir + '\\data')
data = [['Sales', 'Data', 'Region']]

for path in paths:
    if path[-4:] == '.csv':
        with open(f'data\\{path}', 'r') as csvFile:
            csvReader = csv.reader(csvFile)
            addDataToArray(data, csvReader)

with open("proccessed_sales_data.csv", 'w', newline='') as outputFile:
    csvWriter = csv.writer(outputFile)
    csvWriter.writerows(data)
