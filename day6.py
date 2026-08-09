#linear search
'''numbers = [15, 22, 8, 40, 17]
search=int(input("Enter the element you want to search: "))
found=False
for i in range(len(numbers)):
    if search==numbers[i]:
        print("element found at index ",i)
        found=True
        break
if found==False:
    print("Element not found")'''
'''num=int(input("Enter the number you want to reverse: "))
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print("The reversed number is : ",reversed_num)'''
#largest number
numbers = [15, 22, 8, 40, 17]
num=0
largest_num=int(input("Enter the index to find the largest number: "))
for i in numbers:
    if largest_num<num:
        largest_num=num
print("The largest number is :",largest_num)
