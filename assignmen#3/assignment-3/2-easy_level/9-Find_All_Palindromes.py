string_list = ["civic", "apple", 7, "africa", 10, "YevheniY", "level", "ananas", 202]
print("list:", string_list)

##Find All Palindromes:
polindrome_list = (words for words in string_list if str(words)[::1] == str(words)[::-1])
print("Polindromes from the list:", list(polindrome_list))