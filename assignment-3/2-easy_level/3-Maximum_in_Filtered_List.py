numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)

filtered_point = int(input("Enter maximum number:"))
filtered_numbers = [nums for nums in numbers_list if nums < filtered_point]
maximum = max(filtered_numbers)
print("Maximum number, less than",filtered_point,"is", maximum)