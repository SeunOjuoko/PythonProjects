import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

dataDictionary = data.to_dict()
print(dataDictionary)

tempList = data["temp"].to_list()
average = sum(tempList)/len(tempList)
print(average)
print(data["temp"].mean())
print(data["temp"].max())

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

#Tempreature to Fahrenheit
monday = data[data.day == "Monday"]
mondayTemp = monday.temp[0]
mondayTemp_F = float(mondayTemp * 9/5 + 32)
print(mondayTemp_F)

#Create a data frame from scratch
dataDictionary = {
    "students": ["Shay","Tyler","Liam"],
    "score": [76, 56, 65]
}
print(pandas.DataFrame(dataDictionary))

data = pandas.DataFrame(dataDictionary)
data.to_csv("data.csv")