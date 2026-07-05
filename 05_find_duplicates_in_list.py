# Find the duplicates numbers in List

micheal_scotfield = [1,2,3,3,4,5,6,7,8,8]

duplicates = []
seen = set()

for n in micheal_scotfield:
    if n in seen and n not in duplicates:
        duplicates.append(n)
    seen.add(n)
    
print(f"The duplicates numbers in List is: {duplicates}")