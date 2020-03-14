T = int(input())
for t in range(T):
    raw = list(input())
    H = int(input())
    locations = list(map(int, input().split()))
    locations.sort()
    check = 0
    for location in locations:
        raw.insert(location+check, '-')
        check += 1
    print("#{} {}".format(t+1, ''.join(raw)))