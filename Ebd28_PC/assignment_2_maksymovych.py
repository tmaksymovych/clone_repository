print("\n\tgreeting:")
## 1.Hello Variable World:
greeting = "Hello, Python World!"
print(greeting)

print("\n\tBasic Math Operations:" )
## 2.Basic Math Operations:
first_integer = int(input("enter first integer:"))
second_integer = int(input("enter second integer:"))

addition = first_integer + second_integer
substraction = first_integer - second_integer
multiplication = first_integer * second_integer
division = first_integer / second_integer

print()

print("Addition:", addition)
print("Substraction:", substraction)
print("Multiplication:", multiplication)
print(f"Division:", division)

print("\n\tString Manipulation:")

## 3.String Manipulation:
string_1 = input("Enter first string: ")
string_2 = input("Enter second string: ")

print("\n",string_1 + " " + string_2)

print("length of",{string_1}, "=", len(string_1))
print("length of", {string_2}, "=", len(string_2))

print("\n\tConditional Logic:")

#4.Conditional Logic:
num = int(input("enter your integer:"))
if num % 2 == 0:
    print(num,"is even")
else:
    print(num,"is odd")

print("\n count to 10:")

##5.Simple Loop:
a = 1
while a <= 10:
    print(a)
    a += 1 

print("\n\tNumber type:")

##6.If-Else Conditions:
number = float(input("Enter a number: "))
if number > 0:
    print("Your number is Positive.")
elif number == 0:
    print("You number is zero.")
else:
    print("Your number is negative.")    

print("\n\tEven Numbers(1;10):")

##7.Even Numbers with Range:
for a in range(1, 11):
    if a % 2 == 0:
        print(a)
        
print("\n\tSum:")

##8.Summing Numbers:
user_number = int(input("Enter a number: "))
final_count = 0

for a in range(1, user_number + 1):
    final_count += a

print("The sum of numbers from 1 to",user_number, "is:",final_count)

print("\n\tCountdown to 1:")

##9.Countdown Loop:
for a in range(10, 0, -1):
    print(a)

print("\n\tselective count:")

##10.Selective Looping:
for a in range(1, 11):
    if a == 5:
        continue
    if a == 7:
        break
    print(a)

