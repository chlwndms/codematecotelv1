arr=[1,3,5,6,7,9,10]
val = int(input()) 

#finding the input value from given array with binary search (recursive function)

def recursion(front, end):
    if front>end:
        return -1

    mid = (front+end)//2

    if arr[mid] < val:
        return recursion(mid+1, end)
    elif arr[mid] > val:
        return recursion(front, mid-1)
    else :
        return mid

result = recursion(0, len(arr)-1)

if result == -1:
    print("Input value doesn't exist")
else:
    print(result)
