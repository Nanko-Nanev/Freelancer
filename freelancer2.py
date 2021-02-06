import csv

class Example:

#create csv file with data
def write():
    with open('data.csv', 'w', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow(["Hi","there","here","is","an","example"])

#read csv file with data
def read():
    with open('data.csv', 'r',) as file:
       reader = csv.reader(file, delimiter = ',')
       for row in reader:
            print(row)


a = Example.write()
b = Example.read()