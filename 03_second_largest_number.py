# Find the  second largest number in the List

numbers = [1,2,3,4,5,6,7,8,9,100,99]

largest = second = float('-inf')

for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif largest > n > second:
        second = n
print(f"The second largest number is: {second}")