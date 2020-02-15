T = int(input())

for t in range(T):
    N = int(input())
    out = []

    lst = list(map(int, input().split()))

    for n in range(5): #열개까지 출력
        min_num = min(lst)
        max_num = max(lst)
        out.append(str(max_num))
        out.append(str(min_num))
        lst.remove(max_num)
        lst.remove(min_num)
    k = " ".join(out)
    print("#{} {}".format(t+1, k))