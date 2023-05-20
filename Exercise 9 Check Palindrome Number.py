#Exercise 9: Check Palindrome Number
n=12321
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if temp==rev:
    print("given number is a palindrome")
else:
    print("given number is not a palindrome")    
        