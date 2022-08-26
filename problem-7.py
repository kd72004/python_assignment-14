list=[1,2,'c',"java",34,90,9.89]
print(list)
for i in list:
    if type(i)!=int:
        print(i)
        list.remove(i)   
else:
    print(list)
