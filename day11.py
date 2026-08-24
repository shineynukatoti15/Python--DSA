#challenge 1
def second_largest(numbers):
    largest_number=0
    second_largest=0
    for i in numbers:
        if i >largest_number:
            second_largest=largest_number
            largest_number=i
        elif i>second_largest:
            second_largest=i
    return second_largest
numbers = [10, 5, 20, 8, 15]
print("The largest number is : ",second_largest(numbers))
#challenge 2
def remove_duplicates(numbers):
    unique=set(numbers)
    return unique 
numbers = [4, 2, 7, 4, 2, 9, 7, 1]
print( "The duplicates removed number is :",remove_duplicates(numbers))
#challenge 3
def count_even_odd(numbers):
    count_even=0
    count_odd=0
    for i in numbers:
        if i%2==0:
            count_even=count_even+1
        elif i%2!=0:
            count_odd=count_odd+1
    return count_even,count_odd
numbers = [10, 7, 4, 9, 12, 3, 8]
print( count_even_odd(numbers))
#challenge 4
def most_frequent(numbers):
    frequency={}
    max_count=0
    most_frequent_number=0
    for i in numbers:
        if i in frequency:
            frequency[i]=frequency[i]+1
        else:
            frequency[i]=1
    for i in frequency:
        if frequency[i]> max_count:
            max_count=frequency[i]
            most_frequent_number=i
    return most_frequent_number
numbers = [2, 3, 2, 5, 3, 2, 7, 5, 2]
print(most_frequent(numbers))
# challenge 5
def move_zeroes_to_endd(numbers):
    result=[]
    zero_counter=0
    for i in numbers:
        if i!=0:
            result.append(i)
        else:
            zero_counter+=1
    for i in range(zero_counter):
        result.append(0)
    return result
numbers = [0, 1, 0, 3, 12]
print(move_zeroes_to_endd(numbers))
# challenge 6
def find_missing(numbers):
    for i in range(1,7):
        if i not in numbers:
            return i
numbers=[1,2,3,5,6]
print(find_missing(numbers))
#challenge 7
def intersection_of_N(a,b):
    result=[]
    for i in a:
        if i in b:
            result.append(i)
    return result
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(intersection_of_N(a,b))
# challenge 8
def count_pairs(numbers,target):
    count=0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                count +=1
    return count
numbers = [1, 5, 7, -1, 5]
target = 6
print(count_pairs(numbers,target))
#challenge 9
def first_duplicate(numbers):
    seen=set()
    for i in numbers:
        if i in seen:
            return i
        else:
            seen.add(i)
numbers = [4, 2, 7, 2, 9, 4]
print(first_duplicate(numbers))
#challenge 10 (two sum)
def two_sum(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                return [i,j]
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers,target))