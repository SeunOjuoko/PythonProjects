#Read File: Option 1
file = open("File.txt")
contents = file.read()
print(contents)
file.close()

#Read File: Option 2 (Opens and closes the file)
with open("File.txt", mode = "r") as file:
    contents = file.read()
    print(contents)

#Write File (Overwrites Everything in the file)
with open("File.txt", mode = "w") as file:
    file.write("Bye Zeon Ojuoko")

#Write File (Appends adds to the file)
with open("File.txt", mode = "a") as file:
    file.write("\n It was nice meeting you, Zeon")

#Creates a new file
with open("NewFile.txt", mode = "w") as file:
    file.write("Welcome Back, Zeon Ojuoko")

