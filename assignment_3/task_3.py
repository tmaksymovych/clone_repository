numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]
print("Numbers:", numbers_list)


## 1.Sum of numbers:
summary = sum(numbers_list)
print("Sum of numbers:", summary)


##2.Find Minimum:
minimum = min(numbers_list)
print("Minimum number:", minimum)


##3.List Reversal:
numbers_list.reverse()
print("Reversed list:", numbers_list)


##4.Print Odd Numbers:
Odd_numbers = [nums for nums in numbers_list if nums % 2 != 0]
print("Odd numbers from the list:", Odd_numbers)


##5.Multiply List:
multyplier = 2
multyplied_numbers = [a * multyplier for a in numbers_list]
print("Multiplied list:", multyplied_numbers)


##Filter by Condition:
x = int(input("Enter minimum point:"))
filtered_numbers = [nums for nums in numbers_list if nums > x]
print("mumbers bigger than",x,":", filtered_numbers)      


##Average of Positive Numbers:
positive_numbers = [nums for nums in numbers_list if nums > 0]
positive_average = sum(positive_numbers) / len(positive_numbers)
print("Average of positive numbers:", positive_average)


##Maximum in Filtered List:
filtered_point = int(input("Enter maximum number:"))
filtered_numbers = [nums for nums in numbers_list if nums < filtered_point]
maximum = max(filtered_numbers)
print("Maximum number, less than",filtered_point,"is", maximum)


##Aggregate Conditional Sum:
divisor = int(input("Enter a divisor:"))
divisible_numbers = (nums for nums in numbers_list if nums % divisor == 0)
divisible_summary = sum(divisible_numbers)
print("Sum of numbers divisible by", divisor, "is", divisible_summary)


#List of Squares:
print("squared numbers:", [nums ** 2 for nums in numbers_list])


#Extract Positive Numbers:
positive_numbers = [nums for nums in numbers_list if nums > 0]
print("Positive numbers:", positive_numbers)


##Filter Strings by Prefix:
users_prefix = input("enter numeric prefix:")
prefix_check =   [nums for nums in numbers_list if str(nums).startswith(users_prefix)]
print("Numbers starts with", {users_prefix}, ":", prefix_check)

##Sum of First N Numbers:
n_amount = int(input("Enter n first numbers:"))
sum_n_first = sum(numbers_list[:n_amount])
print("Sum of first", n_amount, "numbers is:", sum_n_first)

##Find All Palindromes:
polindrome_list = (nums for nums in numbers_list if str(nums)[::1] == str(nums)[::-1])
print("Polindromes from the list:", list(polindrome_list))


##Check Divisibility:
divisor = int(input("Enter divisor:"))
divisible_numbers = [nums % divisor == 0 for nums in numbers_list]
print("Divisible numbers by", divisor, "are" , list(divisible_numbers))


##Filter by Multiple Conditions:
divisor_x = int(input("Enter first divisor:"))
divisor_y = int(input("Enter second divisor:"))
divisble_numbers = [nums for nums in numbers_list if nums % divisor_x == 0 and nums % divisor_y != 0]
print("Numbers divisible by", divisor_x, "and not divisible by", divisor_y, "are:", list(divisble_numbers))


##Nested List Flattening:
list_of_lists = [[1,6],[2,13],[0,16]]
print("List of lists:", list_of_lists)
single_list = list_of_lists[0] + list_of_lists[1] + list_of_lists[2]
print(single_list)


#Complex String Manipulation:

###########################


# Given a list of strings, extract substrings starting with 'a' and capitalize them
words = ["car", "kse", "palne", "grape","maths", "dog"]
print("List:", words)
substring = [word.upper() for word in words if len(word) == 3]
print("Substrings of length 3:", substring)


#Multi-level Sorting:
numbers_list = [1, 56, 7, 27, 23, 0, 202, -34, -13]