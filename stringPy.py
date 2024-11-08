

name = "M Hashim Khan"

# print(name)
# print(name[0])

# for i in name:
#     print(i)

# ///////// find the length of the String /////////
# print(len(name))

# ///////// To check word or specific part in string use in keyWord /////////
# print("him" in name)

# ///////// To check if a certain phrase or character is NOT present in a string, we can use the keyword not in. /////////
# print("Khan" not in name)

# ///////// Slicing String /////////
# print(name[0:4])
# print(name[:8])
# print(name[2:])
# print(name[-4:])
# print(name[-8:-4])


# ///////// Upper Case /////////
# print(name.upper())

# ///////// Lower Case /////////
# print(name.lower())

# ///////// Remove Whitespace /////////
# a = " Hello, World! "
# print(a.strip())

# ///////// Replace String /////////
# print(a.replace("World" , "Earth"))

# ///////// Split String /////////
# print(a.split(" "))
# print(a.split(","))


# F String
# print(f"My Name is {name}")

# findt = "ABCDCDC"
# substring = "CDC"

# for i in range(len(findt)):
#     if findt[i: i + len(substring)] == substring:
#         print(findt[i: i + len(substring)])

s = "qA2"

# check = [False]*5
# for i in range(len(s)):
#     if s[i].isalnum():
#         check[0] = True
#     if s[i].isalpha():
#         check[1] = True
#         print(s[i])
#     if s[i].isdigit():
#         check[2] = True
#     if s[i].islower():
#         check[3] = True
#         print(s[i])
#     if s[i].isupper():
#         check[4] = True    

# [print(x) for x in check]

# # Check if any alphanumeric characters exist in the string
# print(any(c.isalnum() for c in s))

# # Check if any alphabetical characters exist in the string
# print(any(c.isalpha() for c in s))

# # Check if any digits exist in the string
# print(any(c.isdigit() for c in s))

# # Check if any lowercase characters exist in the string
# print(any(c.islower() for c in s))

# # Check if any uppercase characters exist in the string
# print(any(c.isupper() for c in s))

