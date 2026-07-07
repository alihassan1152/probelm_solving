# Find the  second largest number in the List

numbers = [1,2,3,4,5,6,7,8,9,100,99]

    largest = second = float('-inf')
    
    for n in nums:
        if n > largest:
            second, largest = largest, n  # Pythonic tuple assignment
        elif largest > n > second:
            second = n
            
    # If second remains -inf (e.g., all elements are identical), return None
    return second if second != float('-inf') else None

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 99]
result = find_second_largest(numbers)

if result is not None:
    print(f"The second largest number is: {result}")
else:
    print("There is no second largest number in the list.")
    