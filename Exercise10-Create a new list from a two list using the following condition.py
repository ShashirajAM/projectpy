#Exercise 10: Create a new list from a two list using the following condition
list1=[10,20,25,30,65]
list2=[62,44,37,13,16]
result=[]
for i in list1:
    if i%2!=0:
        result.append(i)
for i in list2:
    if i%2==0:
        result.append(i)
print(result)
