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


# T = int(input())
#
# for t in range(T):
#     str1 = input()
#     str2 = input()
#     res = 0
#
#     for i in range(len(str2)-len(str1)+1):
#         check = ''
#         for j in range(i, i+len(str1)):
#             check += str2[j]
#         if check == str1:
#             res = 1
#
#     print("#{} {}".format(t+1, res))


T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()
    res = 0
    PiTable = [0] * len(str1)
    PiTable[0] = -1
    i = 0
    j = 1
    res = 0

    while j < len(str1)-1:
        if str1[j] == str1[i]:
            PiTable[j+1] = PiTable[j] + 1
            i += 1
            j += 1
        elif str1[0] == str1[j]:
            PiTable[j+1] = 1
            i = 1
            j += 1
        else:
            i = 0
            j += 1

    k = 0
    ans = 0
    while ans + k < len(str2):
        if str2[ans+k] == str1[k]:
            k += 1
        else:
            ans += k - PiTable[k]
            k = 0
        if k == len(str1):
            res = 1
            break
    print("#{} {}".format(t+1, res))