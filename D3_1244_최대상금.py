T = int(input())
for t in range(T):
    rawnum, ch_num = map(int, input().split())
    rawnum = list(str(rawnum))
    for ch in range(ch_num):
        for r in range(ch+1, len(rawnum)):
            rawnum[ch], rawnum[ch+1] = rawnum[ch+1], rawnum[ch]
            if int(rawnum[ch]) <= int(rawnum[r]):
                rawnum[ch], rawnum[r] = rawnum[r], rawnum[ch]
    res = "".join(rawnum)
    print("#{} {}".format(t+1, res))