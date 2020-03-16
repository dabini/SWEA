# T = int(input())
# for t in range(T):
#     A, B = map(list, input().split())
#     cnt = 0
#     n = len(B)
#     for a in range(0, len(A)-n+1):
#         if A[a:a+n] == B:
#             cnt += 1
#     print("#{} {}".format(t+1, len(A)-((n-1)*cnt)))

# T = int(input())
# for t in range(T):
#     A, B = map(str, input().split())
#
#     A = A.replace(B, '0')
#     ans = len(A)
#     print('#{} {}'.format(t+1, ans))

T = int(input())
for t in range(T):
    A, B = input().split()
    cnt = 0
    start = 0

    while start <= len(A) - len(B):
        pos = A.find(B, start)
        if pos < 0:
            break
        cnt += 1
        start = pos + len(B)

    print('#{} {}'.format(t+1, cnt + len(A) - cnt * len(B)))

