# Find missing number in formula n(n+1)/2 

numbers = [1,2,3,5,6]
n = 6

expected_sum = n * (n + 1) // 2
print(f"The missing number in the List is: {expected_sum - sum (numbers)}")

print(expected_sum)




# Pehle bara total nikalo phir 101 se pehle wala hissa minus kardo

micheal_scotfield = [101, 103, 104, 105, 106, 107, 108]

start = 101
end = 108

expected_sum = end * (end + 1) // 2 - (start - 1) * start // 2

print(f"The missing number in the List is: {expected_sum - sum (micheal_scotfield)}")

print(expected_sum)