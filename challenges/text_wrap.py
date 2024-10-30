import textwrap


text = "ABCDEFGHIJKLIMNOQRSTUVWXYZ";
num = 4


print('\n'.join(textwrap.wrap(text , num)))



# textLen = num
# # print(textLen)

# charList = list(text)
# # charList.insert(40 , "*")
# print(charList)

# while textLen <= len(text):
#     print(textLen)
#     charList.insert((textLen) , "*")
#     textLen += num
    
# print(charList)

# for i in range(len(text)):
#     if(count == 4):
#     #   print(text[pre:])
#       wantedText = text[:pre] + "\n"
#       print(wantedText)
#       pre += count
#       count = 0
#       print(pre)
#     else:
#         count += 1
        