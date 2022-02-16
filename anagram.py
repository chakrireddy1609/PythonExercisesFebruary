str1 = "Heart1"
str2 = "Earth"
str1_list = list(str1.lower())
str2_list = list(str2.lower())
str1_list.sort()
str2_list.sort()
if str1_list == str2_list:
    print("given strings are anagram")
else:
    print("given strings are not anagram")


