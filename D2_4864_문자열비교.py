# T = int(input())
#
# for t in range(T):
#     str1 = input()
#     str2 = input()
#
#     if str1 in str2:
#         res = 1
#     else:
#         res = 0
#
#     print("#{} {}".format(t+1, res))


T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()
    res = 0

    for i in range(len(str2)-len(str1)+1):
        check = ''
        for j in range(i, i+len(str1)):
            check += str2[j]
        if check == str1:
            res = 1

    print("#{} {}".format(t+1, res))