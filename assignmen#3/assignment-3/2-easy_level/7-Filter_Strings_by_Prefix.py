string_list = ["apple", "table", "yevheniy", "python", "africa", "yogurt", "ananans"]
print("list:", string_list)

##Filter Strings by Prefix:
users_prefix = input("enter prefix:")
prefix_check = [pref for pref in string_list if str(pref).startswith(users_prefix)]
print("String/s starts with", {users_prefix}, ":", prefix_check)