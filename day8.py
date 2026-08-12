#square 
'''def square(a):
    result=a*a
    return result
s=square(6)
print(s)'''
#mini challange
'''def is_even(num):
    if num%2==0:
        return True
    else:
        return False
result=is_even(45)
print(result)'''
#dsa challenge
'''def count_even(numbers):
    count=0
    for i in numbers:
        if i%2==0:
            count=count+1
    return count
numbers = [10, 7, 4, 13, 8, 5]
print(count_even(numbers))'''
#largest number
'''def find_largest(numbers):
    largest_num=number[0]
    for i in numbers:
        if largest_num>i:
            largest_num=i
    return largest_num
number = [-10, -3, -25, -1]
print(find_largest(number))'''
#count greater
def count_greater(number,target):
    count=0
    for i in number:
        if i >target:
            count=count+1
    return count
numbers = [10, 25, 7, 40, 15]
target = 15
print(count_greater(numbers,target))