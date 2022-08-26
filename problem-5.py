list=[]
num=int(input("enter how many number you want to enter -> "))
while num:
    list.append(int(input("enter number -> ")))
    num-=1
else:
    print(list)
    print("smallest number is ",min(list))
