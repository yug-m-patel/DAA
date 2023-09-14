


def quicksort( a, l, r):

    if(l<r):
        q=partion(a,l,r)
        quicksort(a,l,q-1)
        quicksort(a,q+1,r)

def partion( a, l, r):
    i=l
    for j in range(r-1):
        if(a[j]<=a[r-1]):
            temp = a[j]
            a[j]=a[i-1]
            i+=1

    temp = a[i-1]
    a[i]=a[r-1]
    a[r-1]=temp
    return i



a=[]
b=int(input("Enter no of elements:"))

for i in range(b):
    a.append(int(input("Enter Element:")))

print(a)
quicksort(a,0,b)
print(a)