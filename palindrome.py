num=int(input("Enter a number :"))
orig=num
sum=0
while(num>0):
    rem=num%10
    sum=sum*10+rem
    num=num//10
if(sum==orig):
    print("Palindrome!!")
else :
    print("Not Palindrome")
