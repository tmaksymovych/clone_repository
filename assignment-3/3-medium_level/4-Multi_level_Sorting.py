numbers_list = [1, 56, 7, 27, 1, 23, 0, 202, -34, -13, 7, 0, 1]
print("Numbers:", numbers_list)
sorted_numbers = sorted(numbers_list, key=lambda x: (-x, numbers_list.count(x)))
print("Sorting by descending, then by frequency:", sorted_numbers)