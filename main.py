import csv

def addDataToArray(array, data):
    for item in data:
        if item[0] == 'pink morsel':
            price = float(item[1][1:])
            sales = price * float(item[2])
            array.append([sales, item[3], item[4]])

def main():
    data = [['Sales', 'Data', 'Region']]
    with open('data\\daily_sales_data_0.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        addDataToArray(data, csvReader)
    
    with open('data\\daily_sales_data_1.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        addDataToArray(data, csvReader)
    
    with open('data\\daily_sales_data_2.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        addDataToArray(data, csvReader)
    
    with open("data\\proccessed_sales_data.csv", 'w', newline='') as outputFile:
        csvWriter = csv.writer(outputFile)
        csvWriter.writerows(data)

if __name__ == "__main__":
    main()