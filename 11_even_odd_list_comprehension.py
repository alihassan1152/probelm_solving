numbers = [1,2,3,4,5,6,7,8,9,10]

even = [n for n in numbers if n %2 == 0]
odd = [n for n in numbers if n %2 != 0]

print(even)
print(odd)



even, odd = [], []

for n in numbers:
    if n %2 == 0:
        even.append(n)
    else:
        odd.append(n)
        
print(even)
print(odd)



elements = [7, 0, 13, 22, -4]

even = [n for n in elements if n %2 == 0]
odd = [n for n in elements if n %2 != 0]

print(even)
print(odd)


List = [1,33,4,5,6,7,8,9]

result = []

largest = [n for n in List if n > 5]
result.extend(largest)
print(result)