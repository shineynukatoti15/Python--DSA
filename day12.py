# Bubble sort
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in  range(len(numbers)-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers
numbers = [5, 2, 8, 1, 3]
print(bubble_sort(numbers))
#selection_sort
def selection_sort(numbers):
    for i in range(len(numbers)):
            min_index=i
            for j in range(i+1,len(numbers)):
                  if numbers[j]<numbers[min_index]:
                        min_index=j
            numbers[i],numbers[min_index]=numbers[min_index],numbers[i]
    return numbers
numbers = [5, 2, 8, 1, 3]
print(selection_sort(numbers))
# largest  difference
def Largest_difference(numbers):
    largest_num=numbers[0]
    smallest_num=numbers[0]
    for i in numbers:
        if i>largest_num:
            largest_num=i
    for i in numbers:
        if i<smallest_num:
            smallest_num=i
    return largest_num-smallest_num
numbers = [10, 5, 15, 7, 20, 8]
print(Largest_difference(numbers))
# Rotate a List
def rotate_a_list(numbers):
    last_element=numbers[-1]
    remaining_list=numbers[:-1]
    rotated_list=[last_element]+remaining_list
    return rotated_list
numbers = [1, 2, 3, 4, 5]
print(rotate_a_list(numbers))
# find common elements
def common_elements(a,b):
    result=[]
    for i in a:
        if i in b:
            result.append(i)
    return result
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(common_elements(a,b))
#move negative numbers to first
def move_negatives(numbers):
    positive=[]
    negative=[]
    for i in numbers:
        if i<0:
            negative.append(i)
        else:
            positive.append(i)
    return negative+positive
numbers = [3, -1, 4, -2, 7, -5, 6]
print(move_negatives(numbers))
#find the missing numbers
def find_missing(numbers):
    for i in range(1,8):
        if i not in numbers:
            return i
numbers = [1, 2, 3, 5, 6, 7]
print(find_missing(numbers))
#reversing words
def reverse_words(text):
    split_version=text.split()
    reversed_version=split_version[::-1]
    return reversed_version
text = "Python is very easy"
print(reverse_words(text))
# count vowel in each word
def vowel_count(text):
    words = text.split()
    vowel_check = {'a', 'e', 'i', 'o', 'u'}
    result_dict = {}
    for i in words:
        count = 0
        for j in i:
            if j in vowel_check:
                count +=1
                result_dict[i]=count
    return result_dict
text = "python is very easy"
print(vowel_count(text))
#character for i 
def char_frequency(text):
    frequency={}
    for i in text:
        if i in frequency:
            frequency[i]=frequency[i]+1
        else:
            frequency[i]=1
    return frequency
text = "programming"
print(char_frequency(text))
#non repeating first character
def first_nonrepeting(text):
    for i in text:
        if text.count(i)==1:
            return i
text="aabbcddee"
print(first_nonrepeting(text))
#two sum
def two_sum(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[i+1]==target:
                return[numbers[i],numbers[i+1]]
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers,target))