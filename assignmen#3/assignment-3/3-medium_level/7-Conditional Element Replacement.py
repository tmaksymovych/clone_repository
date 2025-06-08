numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers list:", numbers_list)


"""i've got two variants of the task:"""


# numbers = {"a1":1, "b1":56, "c1":7, "d1":27, "e1":23, "f1":0, "g1":202, "h1":-34, "j1":-13}

# def replace_under_zero(dictionary):
#     """Replace negative values in a dictionary with zero.
#     """
#     for key in dictionary:
#         if dictionary[key] < 0:
#             dictionary[key] = 0
#     return dictionary
    
# replace_under_zero(numbers)
# print("Replaced all negative numbers with 0:", list(numbers.values()))

for nums in numbers_list:
    if nums < 0:
        numbers_list[numbers_list.index(nums)] = 0
print("Replaced all negative numbers with 0:", numbers_list)