score = [150, 45, 5, 67, 122, 560, 35, 234, 78, 90, 225]

#Print Max
total = sum(score)
sum = 0
for exam in score:
    sum += exam
print(sum)

#Print Max
max = 0
for exam in score:
    if exam > max:
        max = exam
print(max)