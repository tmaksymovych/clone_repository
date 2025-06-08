numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)

##Filter by Condition:
x = int(input("Enter minimum point:"))
filtered_numbers = [nums for nums in numbers_list if nums > x]
print("mumbers bigger than",x,":", filtered_numbers)