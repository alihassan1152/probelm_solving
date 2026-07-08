# Find common numbers in differnet Lists

numers_1 = [1,2,3,4,5,6,7,8]
numbers_2 = [4,5,6,2,3,4]

common = list(set(numers_1) & set(numbers_2))

print(common)




# Find common numbers in the different List with Loop

List1 = [1,2,3,4,5,6]
List2 = [4,5,7,8,9]

common = []

for n in List1:
    if n in List2 and n not in common:
        common.append(n)
print(common)