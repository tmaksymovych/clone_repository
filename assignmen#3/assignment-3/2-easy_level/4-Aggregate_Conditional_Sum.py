numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)

divisor = int(input("Enter a divisor:"))
divisible_numbers = (nums for nums in numbers_list if nums % divisor == 0)
divisible_summary = sum(divisible_numbers)
print("Sum of numbers divisible by", divisor, "is", divisible_summary)