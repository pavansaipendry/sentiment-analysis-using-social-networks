import csv

with open('tweets.csv', encoding="utf-8") as file:
    reader = csv.reader(file)
    column_index = 3
    data_array = []
    for row in reader:
        data = row[column_index]
        data_array.append(data)

print(data_array)
