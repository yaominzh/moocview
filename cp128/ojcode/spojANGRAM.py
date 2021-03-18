n = int(input())
from collections import Counter
for i in range(n):
    a,b = map(str,list(input().split()))
    if len(a) != len(b):
        print('false')
        continue
    ca = Counter(a)
    cb = Counter(b)
    flag = True
    for v in ca:
        if ca[v] !=cb[v]:
            flag = False
            break
    for v in cb:
        if cb[v] != ca[v]:
            flag = False
            break
    if flag:
        print('true')
    else:
        print('false')
