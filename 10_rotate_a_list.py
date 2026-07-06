# Rotate list main pehle 2 index last main chale jate hain matlab aik daira hai 6 logon ka jo bss ghoom jata hai or kuch nahi.

numbers = [0,9,8,7,6,5,4,3,2,1]

n = 2 

rotated = numbers[n:] + numbers[:n] 
print(rotated)


# ye last wale 2 index ko first main laikar ane ke liye.

elements = ["a","b","c","h","g","z"]

x = 2

rotated = elements[-x:] + elements[:-x]
print(rotated)