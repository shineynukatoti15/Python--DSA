y=int(input("Enter the year:"))
if(y%100==0) and (y%400==0) and (y%4==0):
    print("the year you entered is a leap year." )
else:
    print("the year you entered is not a leap year.")