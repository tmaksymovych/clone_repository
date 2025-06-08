numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)

divisor_x = int(input("Enter first divisor:"))
divisor_y = int(input("Enter second divisor:"))
divisble_numbers = [nums for nums in numbers_list if nums % divisor_x == 0 & nums % divisor_y != 0]
print("Numbers divisible by", divisor_x, "and not divisible by", divisor_y, "are:", list(divisble_numbers))