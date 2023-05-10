#1 Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def multiplicationorsum(num1,num2):
    product=num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2
result=multiplicationorsum(60,30)
print("the result is:",result)

#2 Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

previousnum=0
for i in range(1,11):
    sum=previousnum+i
    print("current number",i,"previous number",previousnum, "sum",sum)
    previousnum=i

#3 Write a program to accept a string from the user and display characters that are present at an even index number
import time as t
start=t.time()
wordname=input('enter the word: ')
#N=len(wordname)
a=list(wordname)
for i in a[0::2]:
    print(i)
end=t.time()
x=end-start
print(x)

#4 Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove(word,n):
    x=word[n:]
    print(x)
    
remove('pynative',4)

#5 Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def checknum(numlist):
    if numlist[0]==numlist[-1]:
        return True
    else:
        return False

x=checknum([10,54,32,68,10])
print(x)

    
