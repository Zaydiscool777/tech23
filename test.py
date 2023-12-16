import csv
f = open("data.csv", 'r+')
read = [i[1] for i in csv.reader(f)]
print(read)