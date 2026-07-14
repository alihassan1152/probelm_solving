# 1
text = "madam"
if text == text[::-1]:
    print("PALINDROM")
else:
    print("NOT PALINDROM")
    


# 2
word = "madam"
is_pal = True

for i in range(len(word) // 2):
    if word[i] != word[len(word)-1 -i]:
        is_pal = False
print(is_pal)


# 3
name = ["Ali", "Haroon", "Khuzaima"]

if text == text[::-1]:
    print(name, "PALINDROM")
else:
    print(name, "NOT PALINDROM")


# 4
words = ["racecar", "hello", "level"]

for text in words:
    if text == text[::-1]:
        print(text, "PALINDROM")
    else:
        print(text, "NOT PALINDROM")