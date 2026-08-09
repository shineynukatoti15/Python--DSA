'''number=int(input("Enter the no.of digits you wanna count : "))
count=0
while number>0:
    number=number//10
    count+=1
print("The no.of digits you've enterd is :",count)'''
number=int(input("Enter the number you want to check the palindrome: "))
original_number=number
reversed_number=0
while number>0:
    digit=number%10
    reversed_number=reversed_number*10+digit
    number=number//10
if reversed_number==original_number:
    print("The number is a palindrome. ")
else:
    print("The number is not a palindrome .")