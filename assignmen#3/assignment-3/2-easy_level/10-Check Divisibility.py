numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)

##Check Divisibility:
divisor = int(input("Enter divisor:"))
divisible_numbers = [nums % divisor == 0 for nums in numbers_list]
print("Divisible numbers by", divisor, "are :" , divisible_numbers)