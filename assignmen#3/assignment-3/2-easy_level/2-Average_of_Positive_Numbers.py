numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)

positive_numbers = [nums for nums in numbers_list if nums > 0]
positive_average = sum(positive_numbers) / len(positive_numbers)
print("Average of positive numbers:", positive_average)