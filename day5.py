'''numbers=[5,10,15]
total=0
for i in numbers:
    total=total+i
print("Total is :",total)'''
numbers = [12, 45, 8, 90, 32]
largest_number=numbers[0]
for i in numbers:
    if largest_number<i:
        largest_number=i
print("Largest number is :",largest_number)