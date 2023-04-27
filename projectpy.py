# # import string
# # alpha=string.ascii_lowercase
# # print(alpha)

# import string
# size=5
# def print_rangoli(size):
#     if i<=size:
#         for i in string.ascii_lowercase:
#             print(i.center(5))
# print_rangoli(size)
# def person(name,**data):
    
#     print(name)
#     for i,j in data.items():
#         print(i,j) 
    
# person("shashi",age=28,city="banglore",ph=9036477324)
# def count(lst):
#     even=0
#     odd=0
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd
# lst=[20,15,26,78,36,55,19,84,79]
# even,odd=count(lst)
# print("even:{} and odd:{}".format(even,odd))
#lst=list(input())
# names=input("enter names with space")
# lst=names.split()
# def count(lst):
#     name=0
#     for i in lst:
#         if len(i)>5:
#             name+=1
#     return name 
# name=count(lst)
# print(name)

# def fib(n):
#     a=0
#     b=1
#     if n<0:
#         print("invalid number") 
#     elif n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c 
#             print(c)
# fib(-5)        

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# x=5
# result=fact(x)
# print(result)  
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i=0
# def greet():
#     global i
#     i+=1
#     print('hello',i)
#     greet()   
# greet()
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# result=fact(5)
# print(result)

# def fact(n):
#     return 1 if n<=1 else n*fact(n-1)
# print(fact(5))
# f=lambda a,b:a+b
# result=f(5,6)
# print(result)

# from functools import reduce
# nums=[3,2,4,5,8,9,7,6]
# evens=list(filter(lambda n:n%2==0,nums))
# doubles=list(map(lambda n:n*2,evens))
# print(doubles)
# sum=reduce(lambda a,b:a+b,doubles)
# print(sum)

# def runningSum(nums):
#     a=[]
#     sum=0
#     for i in nums:
#         sum+=i
#         a.append(sum)
#     return a
# nums=[1,2,3,4]
# runningSum(nums)
#def countfactors(self,A):
# A=17
# c=0
# i=1
# while (i*i<=A):
#     if (A%i==0):
#         if (i==(A//i)):
#             c+=1
#         else:
#             c+=2 
#     i+=1
# if c==2:
#     print(1)
# else:
#     print(0) 
# A=25  
# if A==1:
#     print(1)
# i=2
# while (i*i<=A):
#     if i*i==A:
#         print(i)
#     i+=1
#     print(-1)
import math as m
class geometry:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=m.pi*(radius**2)
        print("area of the circle is:", a)
radius=int(input("radius of thr circle"))
circle=geometry(radius)
circle.area()
        