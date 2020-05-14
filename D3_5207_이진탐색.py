T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nlst = sorted(list(map(int, input().split())))
    mlst = list(map(int, input().split()))

    cnt = 0
    for num in mlst:
        start = 0
        end = N-1

        flag = 0
        while start <= end:
            mid = (start + end) // 2

            if num >= nlst[mid]:
                if num == nlst[mid]:
                    cnt += 1
                    break

                start = mid + 1
                if flag == 1: break
                flag = 1

            elif num < nlst[mid]:
                end = mid - 1
                if flag == -1: break
                flag = -1


    print("#{} {}".format(t+1, cnt ))