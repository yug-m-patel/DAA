def merg(arr1, arr2):
    d = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] >= arr2[0]:
            d.append(arr2[0])
            arr2.remove(arr2[0])
        else:
            d.append(arr1[0])
            arr1.remove(arr1[0])

        # while len(arr1) != 0:
        #     d.append(arr1[0])
        #     arr1.remove(arr1[0])
        # while len(arr2) != 0:
        #     d.append(arr2[0])
        #     arr2.remove(arr2[0])
    while len(arr1) != 0:
        d.append(arr1[0])
        arr1.remove(arr1[0])
    while len(arr2) != 0:
        d.append(arr2[0])
        arr2.remove(arr2[0])
    return d





def mergsort(a):
    if len(a) == 1:
        return a
    else:
        arr1 = []
        arr2 = []
        n = len(a) // 2
        for i in range(n):
            arr1.append(a[i])
        for i in range(n, len(a)):
            arr2.append(a[i])
        arr1 = mergsort(arr1)
        arr2 = mergsort(arr2)
        return merg(arr1, arr2)


b = list(map(int, input().split(',')))
c = mergsort(b)
print(c)
