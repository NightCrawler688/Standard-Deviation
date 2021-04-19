import math
import csv

with open("class1.csv",newline = '') as f:
        reader = csv.reader(f)
        file_data = list(reader)
file_data.pop(0)
data = file_data[1]
def mean(data):
        n = len(data)
        total = 0
        for x in data:
                total+=int(x)
        mean = total/n
        return mean

squared_list = []
for number in data:
        a = int(number) - mean(data)
        a = a**2
        squared_list.append(a)
sum = 0
for i in squared_list:
        sum+=i
result = sum/(len(data) - 1)
standard_deviation = math.sqrt(result)
print('The standard deviation is: ' + str(standard_deviation))
