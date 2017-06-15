print("This\'s my first Python tool")
print('Hello World')




age=28
name="XXX"
print("{0} is {1} old".format(name,age))

while age>1:
   print(age)
   age=age-1
print('done')

for i in range(1,5):
   print(i)

print(len(name))


while True:
   s=input("input something")
   if s=="q":
      break
   if len(s)<3:
      print("too short")
      continue
   print("input is not enough")




temp=input("please input a number")
guess=int(temp)
print("you input number",temp)
if guess==8:
   print("correct")
elif guess==9:
   print("9")
else:
   print("wrong")
   
temp=input("please input a number")  


def sayhello():
   print("hello")

