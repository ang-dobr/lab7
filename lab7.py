def merge(*lists):
    a, b = [], []
    for i in range(0, len(*lists) - 2):
        a += [*lists[i]]
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            b.append(a[i][j])
    return sorted(b)


k = int(input())
l = []
for i in range(k):
    l.append(list(map(int, input().split())))
print(merge(l))