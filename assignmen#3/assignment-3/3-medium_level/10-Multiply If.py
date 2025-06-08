import random 

numbers_list = [random.randint(-8096, 15730) for _ in range(124)]
print("numbers:", numbers_list)

Y = int(input("Enter multyplier:"))
X = int(input("Enter limiter:"))

multyplied_list = [nums for nums in numbers_list * Y if nums > X]
print("Multiplied list:", multyplied_list)