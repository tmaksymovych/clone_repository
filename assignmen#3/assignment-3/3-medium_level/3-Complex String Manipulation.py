words = ["car", "kse", "palne", "grape","maths", "dog"]
print("List:", words)
substring = [word.upper() for word in words if len(word) == 3]
print("Substrings of length 3:", substring)