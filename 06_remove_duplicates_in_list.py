# Remove duplicates in List

fibbonacchi = [1,2,3,4,4,5,6,7,8,9,9]

unique = []

for n in fibbonacchi:
    if n not in unique:
        unique.append(n)
print(unique)


# 2nd way

elements = [1,2,3,4,4,5,6,6]

print(list(dict.fromkeys(elements)))



# 3rd way

numbers = [3, 1, 2, 1, 3, 4]

print(list(set(numbers)))           
print(list(dict.fromkeys(numbers)))  

unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
    print(f"n={n}, unique={unique}")  
    

# forth way in strings

alphabets = ["b", "a", "b", "c", "a"]

unique = []

for n in alphabets:
    if n not in unique:
        unique.append(n)
print(unique)
