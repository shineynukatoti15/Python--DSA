#print numbers upto 10
#level one
'''for i in range(1,11):
    print(i)
for reverse in range(10,0,-1):
    print(reverse)
for even in range(1,21):
    if even%2==0:
        print(even)
for odd in range(1,20):
    if odd%2!=0:
        print(odd)
number=int(input("Enter the number you want :"))
for i in range(1,11):
    print(f"{number}  x {i} ={number*i}")'''
#level two
#find the sum of fromm one to n.
'''num=int(input("Enter the number to sum up:"))
sum=0
for i in range(num+1):
    sum=sum+i
print("The total sum is :",sum)'''
#factotrial of a number
'''number=int(input("Enter the number to get the factorial :"))
fact=1
for i in range(1,number+1):
    fact=fact*i
print(f"The factorial of the number {number} is ",fact)'''
#assignment
'''num=int(input("Enter a number: "))
reversed_number=0
while num>0:
    digit=num%10
    reversed_number=reversed_number*10+digit
    num=num//10
print(reversed_number)'''
#count digits
'''number=int(input("Enter the number:"))
count=0
while number>0:
    number=number//10
    count+=1
print("The count of the digit is:",count)'''
#palindrone
'''num=int(input("Enter the number to check palindronre: "))
palindrone_num=0
original_NUM=num
while num>0:
    digit=num%10
    palindrone_num=palindrone_num*10+digit
    num=num//10
if palindrone_num==original_NUM:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")'''
#sum of n numbers
'''number=int(input("Enter the number: "))
total=0
for i in range(number+1):
    total=total+i
print("The total sum of the number is: ",total)'''
number=int(input("Enter the number: "))
total=1
for i in range(1,number+1):
    total=total*i
print("The factorial of the number is: ",total)