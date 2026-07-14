# WAY 1
numbers = [1,1,1,3,4,4,5,6,6]
freq = {}

for n in numbers:
    freq[n] = freq.get(n, 0) + 1

print(freq)



# WAY 2
List = ["A", "A", "C", "D", "D"]
freq = {}

for n in List:
    freq[n] = freq.get(n, 0) + 1

print(freq)