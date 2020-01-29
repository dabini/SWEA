#1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

T = int(input())

for t in range(T):
    total = 0
    N = int(input())
    lst = []

    for n in range(1, N+1):
        lst.append(n)

    for l in lst:
        if l % 2:
            total += l
        else:
            total -= l
    print("#{0} {1}".format(t+1, total))