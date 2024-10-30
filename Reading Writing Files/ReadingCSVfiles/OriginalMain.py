import csv

with open("weather_data.csv") as csvfile:
    #Creates a list of data from the CSV file
    data = csv.reader(csvfile)
    #Loops through the data within the CSV file
    day = []
    temperature = []
    condition = []
    for row in data:
        if row[0] != "day":
            day.append(row[0])
        if row[1] != "temp":
            temperature.append(int(row[1]))
        if row[2] != "condition":
            condition.append(row[2])
    print(day)
    print(temperature)
    print(condition)

