numbers = [2,3,4,5,6]

total = 0
count = 0
maximum = numbers[0]

for n in numbers:
    total = total + n
    count = count + 1
    if n > maximum:
        maximum = n

print("Sum", total)
print("Average", count/total)
print("Max", maximum)