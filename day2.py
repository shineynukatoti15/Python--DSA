'''
//checking whether the number is positive ,negativeor zero
number=int(input("Enter a number: "))
if number==0:
    print("The number id zero. ")
elif number>0:
    print("The number is positive. ")
else:
    print("The number is negative. ")
    //whether the person is eligible to vote or not
age=int(input("Enter your age: "))
if age>=18:
    print("The candidate can vote. ")
else:
    print("The candidate cannot vote. ")
    //comparing two numbers
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
if number1>number2:
    print("The number1",number1,"is greater than number2",number2)
else:
    print("The number2",number2,"is greater than number1",number2)
    //checking the largest among three numbers
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number:"))
if n1>n2 and n1>n3:
    print("The first number is greater than second and third number.")
elif n2>n1 and n2>n3:
    print("The second number is greater than first and third number. ")
else:
    print("The third number is greater than the first and second number. ")
    //checking a leap year 
year=int(input("enter a year: "))
if year%400==0 and year%100==0 and year%4==0:
    print("The year you entered is a leap year. ")
else:
    print("The year you entered is not a leap year. ")
    //grade calculator
marks=int(input("Enter the marks you scored: "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=75 and marks<=89:
    print("Grade B")
elif marks>=60 and marks<=74:
    print("Grade C")
elif marks<=60:
    print("Fail")
else:
    print("Invalid marks")
    //atm eligibility
age=int(input("Enter your age:"))
has_atm_card=input("Enter yes if you have atm card or else no :(yes/no)")
if age>=18 and has_atm_card="yes":
   print("Access Granted.")
else:
   print("Access Denied.")
   //login system
username=input("Enter the username: ")
password=input("Enter the password: ".lower())
if username=="shiney"and password=="1106.Shineyy":
    print("Login Succesful.")
else:
    print("Login unsuccessful.")
height=int(input("Enter the height: "))
weight=int(input("Enter the weight: "))
bmi=weight/(height*height)
if bmi<=18.5:
    print("you are underweight. ")
elif bmi>=18.5 and bmi<=24.9:
    print("you have a normal weight. ")
elif bmi<=25.0 and bmi>=29.9:
    print("you are overweight.")
else:
    print("you are obese. ")
units=int(input("Enter the units :"))
if units<=100:
    first_100_unit=units*2
    print(f"The bill you need to pay is: {first_100_unit}")
elif units>=101 and units<=200:
    first_slab=100*2
    remaining_units=units-100
    remaining_units*=3
    second_slide=first_slab+remaining_units
    print(f"The bill you need to pay is :{second_slide}")
elif units>200:
    first_slab=100*2
    remaining_units=units-200
    second_slab_bill=100*3
    third_bill=remaining_units*5
    total_bill=first_slab+second_slab_bill+third_bill
    print("The total bill you need to pay is :",total_bill)
else:
    print("You've enter invalid details. ")
number=int(input("Enter a number you want to reverse: "))
reversed_number=0
count=0
while number>0:
    digit=number%10
    reversed_number=reversed_number*10+digit
    number=number//10
    count+=1
print("The reversed number\ is : ",reversed_number)
print("The numner of digits you've entered is: ",count)'''
