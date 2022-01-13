import csv

csvFile = open('newPeople.csv', mode='w')

# Read the object
data = {["nameFirst", "nameLast", "age"], ["Bill", "Jones", "55"], ["Jill", "Joens", "54"]}

file_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for row in data:
    file_writer.writerow(row)

csvFile.close()