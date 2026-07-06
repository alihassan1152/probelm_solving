# Find Largest number in the List

micheal_scotfield = [10, 22, 9, 100]

largest = micheal_scotfield[0]

for n in micheal_scotfield:
    if n > largest:
        largest = n
print(largest)

# Find Smallest number in the List

numbers = [1,2,3,4,5]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n
print(smallest)


# Find Largest and Smallest number in the List

jan_abruzi = [12,100,14,55,18]
largest = smallest = jan_abruzi[0]

for n in jan_abruzi:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print(f"The largest number in the List is:{largest}")
print(f"The smallest number in the List is:{smallest}")