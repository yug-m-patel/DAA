#a = [1, 2, 3, 5, 2]
def dup(a):
    b = []
    for i in range(len(a)+1):
        b.insert(i, 0)
    for i in a:
        b[i] = b[i]+1
        if b[i] > 1:
            print("Duplicate no is:", i)
            continue
c = int(input("enter no of elements:"))
d=[]
for i in range(c):
    d.append(int(input()))
dup(d)
