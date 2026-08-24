#challenge 1
'''def set_numbers(numbers):
    unique = set(numbers)
    return unique
numbers = [5, 2, 5, 8, 2, 9, 8, 1]
print(set_numbers(numbers))'''
#challenge 2
'''def membership(numbers):
    for i in numbers:
        if 15 in numbers:
            return "Found"
        else:
            return "Not Found"
number = {10, 20, 30, 40, 50}
print(membership(number))'''
#common elements(challenge 3)
'''def common_elements(a,b):
    intersection_n=a.intersection(b)
    return intersection_n
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Intersection of a and b is",common_elements(a,b))'''
#challenge 4
'''def union_elements(a,b):
    union_n=a.union(b)
    return union_n
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union of a and b ",union_elements(a,b))'''
#challenge 5
'''def difference_elements(a, b):
    difference_e=a.difference(b)
    return difference_e
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
print("The difference of a and b is :",difference_elements(a,b))'''
# dictionary challenge 1
'''student = {
    "name": "Shiney",
    "age": 20,
    "course": "CSE"
}
print(student["course"])'''
#challenge 2
''''student = {
    "name": "Shiney",
    "age": 20,
    "course": "CSE",
    "college": "NRI"
}
print(student["college"])
#challenge 3
student = {
    "name": "Shiney",
    "age": 20,
    "course": "CSE",
    "age": "21"
}
print(student["age"])'''
#challenge 4
#deleting the key
'''student = {
    "name": "Shiney",
    "age": 21,
    "course": "CSE"
}
del student ["age"]
print(student)'''
#challenge 5
'''def check_key(student,key):
    for key in student:
        if key in student:
            return "Found"
        else:
            return "Not Found"
student = {
    "name": "Shiney",
    "age": 21,
    "course": "CSE"
}
print(check_key(student,"age"))'''
# final challenge 
def count_frequencies(numbers):
    frequency={}
    for i in numbers:
        if i in frequency:
            frequency[i]=frequency[i]+1
        else:
            frequency[i]=1
    return frequency
numbers = [2, 3, 2, 5, 3, 2, 7, 5]
print(count_frequencies(numbers))