import csv
path = '/RISHI/H2K/FileIO/TEMP/CSVFilesteachers.csv'

file = open(path)
data = csv.reader(file)
for eachRow in data:
    print(eachRow)
file.close()
