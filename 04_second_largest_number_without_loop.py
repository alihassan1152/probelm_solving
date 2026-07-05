# Find second largest number without Loop

elements = [1,2,3,4,5]

unique = list(set(elements))

unique.sort()
print(unique[-2])