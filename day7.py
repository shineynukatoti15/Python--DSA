numbers = [5, 10, 18, 25, 40, 55, 70]
found=False
search=int(input("Enter the search element: "))
left=0
right=len(numbers)-1
while left<=right:
    mid=(left+right)//2
    if search==numbers[mid]:
            found=True
            print("Element found at index ", mid)
            break
    elif search>numbers[mid]:
        left=mid+1
    else:
        right=mid-1
if not found:
    print("Element not found or enter invalid search element.")
    
