string_1 = ("This mail point dot dog Yecheniy is good")
string_2 = ("apple banana orange table chair window cloud river")
string_3 = ("function variable list tuple dictionary loop class import module lambda exception")
string_4 = ("puppy chicken cat fish bird turtle hamster rabbit")

print("String 1:", string_1)
print("String 2:", string_2)
print("String 3:", string_3)
print("String 4:", string_4)

x = int(input("enter an amount of letter  :"))

len_str1 = len(string_1)
len_str2 = len(string_2)
len_str3 = len(string_3)
len_str4 = len(string_4)


string_count = [len_str1, len_str2, len_str3, len_str4] 
count_greater_than_x = [a for a in string_count if a > x]

print(f"An amount of string with lenghts greater than {x} is {len(count_greater_than_x)}")











