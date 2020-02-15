T = int(input())

for t in range(T):
    word = input()
    res = []

    for w in word:
        if w not in res or w != res[-1]:
            res += [w]
        elif w in res and w == res[-1]:
            res.pop()
    print("#{} {}".format(t+1, len(res)))