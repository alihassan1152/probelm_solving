# Nested List [[1,2],[3,4],[5,6]] ke elements ko single List [1,2,3,4,5,6] main convert karta hai

nested = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)
print(f"The final List is here after solve nested list problem: {flat}")


nested_list = [["A", "B"],["C","D"],["E","F"]]

flat = []

for sublist in nested_list:
    for item in sublist:
        flat.append(item)

print(flat)