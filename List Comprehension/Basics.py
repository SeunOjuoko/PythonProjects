#Task 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

#Task 2
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string) for string in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)

#Task 3
with open("file1.txt") as file1:
  list1 = file1.readlines() 
with open("file2.txt") as file2:
  list2 = file2.readlines() 
result = [int(num) for num in list1 if num in list2]
print(result)

#List Comprehension

#Task1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word: len(word) for word in sentence.split()}
print(result)

#Task 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: temp * 9/5 + 32 for (day,temp) in weather_c.items()}
print(weather_f)

