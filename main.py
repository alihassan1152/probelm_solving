def find_second_largest(nums):
    if len (nums) < 2:
        return None
    
    largest = second = float('-inf')
    
    for n in nums:
        if n > largest:
            second, largest = largest, n
        elif largest > n > second:
            second = n
        
    return second if second != float('-inf') else None

numbers = [1,2,3,4,5,6,7,8,9,100]

result = find_second_largest(numbers)

if result is not None:
    print(f"the second largest number in the List is: {result}")
else:
    print(f"there is no second largest number in the list.")