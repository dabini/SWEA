T = int(input())
total = 0
for t in range(T):
    input_lst = list(map(int, input().split()))
    input_lst = sorted(input_lst)

    total = 0

    for inp in input_lst[1:-1]:
        total += inp
    avg = round(total / (len(input_lst) - 2))
    print("#{0} {1}".format(t+1, avg))
