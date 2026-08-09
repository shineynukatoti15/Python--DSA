n=int(input("Enter the number to print the pattern: "))
'''for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()'''
'''for i in range(n,0,-1):`
    for j in range(i):
        print("*",end="")
    print()'''
'''for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    print()'''
'''for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end="")
    print()'''
'''for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(k+1,end="")
    print()'''
'''for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()'''
'''for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(n-i+1):
        print("*",end="")
    print()'''
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()