def bsearch(arr, s, e, b):
    mid = (s+e)//2
    if b == arr[mid]:
        print("element found on",mid)
    elif b < arr[mid]:
        bsearch(arr,0,mid-1,b)
    elif b > arr[mid]:
        bsearch(arr,mid+1,e,b)
    else:
        print("not found")


def insort(arr):
    for i in range(1,len(arr)):
        t = arr[i]
        t1 = i-1
        while t1 >= 0 and t < arr[t1]:
            arr[t1 + 1] = arr[t1]
            t1 = t1-1
        arr[t1+1] = t


a = int(input("Enter no. of elements in array: "))
arr=[]
for i in range (a):
    arr.append(int(input("Enter your elements")))
print (arr)
insort(arr)
print(arr)
b = int(input("enter search element:"))
bsearch(arr,0,len(arr)-1,b)