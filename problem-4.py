list=[]
num=int(input("enter how many number you want to enter -> "))
while num:
    list.append(input("enter number -> "))
    num-=1
else:
    print(list)
    print("maximum numb is ",max(list))
