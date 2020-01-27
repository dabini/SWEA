#d2 1926. 369게임

num = int(input())
num_lst = list(range(1, num+1))
lst = []
for n in num_lst:
    cnt = 0
    for k in str(n):
        if k in ['3', '6', '9']:
            cnt += 1
            if cnt >= 1:
                n = "-" * cnt
    lst.append(str(n))
print(' '.join(lst))