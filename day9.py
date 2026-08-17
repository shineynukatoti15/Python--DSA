#count_vowels
'''def count_vowels(text):
    count=0
    for j in text:
        if j in ['a','e','i','o','u']:
            count+=1
    return count
texts="python programming"
print(count_vowels(texts))'''
#reverse the string
'''def reverse_string(text):
    reversed_s=text[::-1]
    return reversed_s
textt="hello"
print(reverse_string(textt))'''
#check palindrone
'''def is_palindrome(text):
    reversed_s=text[::-1]
    if reversed_s==text:
        return True
    else:
        return False
texts="madam"
print(is_palindrome(texts))'''
#count the character
'''def count_char(text,target):
    count=0
    for i in text:
        if i==target:
            count+=1
    return count
texts="banana"
target="a"
print(count_char(texts,target))'''
#remove spaces
'''def remove_spaces(text):
    spaces_removed=""
    for i in text:
        if i !=" ":
            spaces_removed=spaces_removed+i
    return spaces_removed
texts="hello world python"
print(remove_spaces(texts))'''
#day9 challenge
'''def remove_vowels(text):
    removed_char=""
    for i in text:
        if i not in ['a','e','i','o','u']:
            removed_char=removed_char+i
    return removed_char
texts="hello world"
print(remove_vowels(texts))'''
#challenge 7
'''def count_words(text):
    words=text.split()
    return len(words)
texts="Python is very easy"
print(count_words(texts))'''
#challenge 8
'''def longest_word(text):
    words=text.split()
    largest=""
    for i in words:
        if len(i)>len(largest):
            largest=i
    return largest
texts="Python Programming is intersting"
print(longest_word(texts))'''
#challenge 9
'''def frequency_counter(text):
    frequency={}
    for i in text:
        if i in frequency:
            frequency[i]=frequency[i]+1
        else:
            frequency[i]=1
    return frequency
texts="banana"
print(frequency_counter(texts))'''
#challenge 10
def first_unique(text):
    for i in text:
        if text.count(i)==1:
            return i
texts="aabbcdd"
print(first_unique(texts))