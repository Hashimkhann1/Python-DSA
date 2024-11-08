


myInfo = {
    "name" : "M Hashim",
    "age" : 22,
    "male" : True,
    "class" : "3 semester"
}
print(myInfo)
print(myInfo.get('name'))
print(myInfo.keys())
print(myInfo.values())

myInfo["phoneNumber"] = "03130000000"
print(myInfo);


for x in myInfo:
  print(x)
  print(myInfo[x])



for x in myInfo.values():
  print(x)


print(">>>>>>>>>>>>>>>>>>")

for x in myInfo.items():
  print(x)


print(">>>>>>>>>>>.")

if 0.1 + 0.2 == 0.3:
  print("True")
else:
  print("False")


  exp = {
    "name" : "hhasbjahs",
    "detal" : "kajnsjhbd",
    "mail" : True,
  }

  for key , value in exp.items():
    print(f"{key} : {value}")