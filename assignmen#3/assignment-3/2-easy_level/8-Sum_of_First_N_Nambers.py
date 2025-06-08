numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)

##Sum of First N Numbers:
n_amount = int(input("Enter n first numbers:"))
sum_n_first = sum(numbers_list[:n_amount])
print("Sum of first", n_amount, "numbers is:", sum_n_first)