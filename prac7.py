a = [1, 2, 3, 5, 2]
b = []
for i in range(len(a) + 1):
    b.insert(i, 0)
for i in a:
    b[i] = b[i] + 1
    if b[i] > 1:
        print("duplicate no is :", i)
        continue

for i in range(1, len(a) + 1):
    if b[i] == 0:
        print("missing no is :", i)
