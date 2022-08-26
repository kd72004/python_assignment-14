list=[1,2,2,3,2,45]
print(list)
fre=0
num=int(input("enter a number which is vailiable in list -> "))
for i in list:
    if(num==i):
        print("index no",fre)
    fre+=1
          
else:
    print(list)
