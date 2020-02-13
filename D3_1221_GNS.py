T = int(input())
for _ in range(T):
    t, num = map(str, input().split())
    num = int(num)
    Info = [[[0]*128 for _ in range(128)]for _ in range(128)]
    lst= list(map(str, input().split()))
    cnt = [0] * 10

    Info[ord('Z')][ord('R')][ord('0')] = 0
    Info[ord('O')][ord('N')][ord('E')] = 1
    Info[ord('T')][ord('W')][ord('0')] = 2
    Info[ord('T')][ord('H')][ord('R')] = 3
    Info[ord('F')][ord('O')][ord('R')] = 4
    Info[ord('F')][ord('I')][ord('V')] = 5
    Info[ord('S')][ord('I')][ord('X')] = 6
    Info[ord('S')][ord('V')][ord('N')] = 7
    Info[ord('E')][ord('G')][ord('T')] = 8
    Info[ord('N')][ord('I')][ord('N')] = 9

    for i in range(num):
        cnt[Info[ord(lst[i][0])][ord(lst[i][1])][ord(lst[i][2])]] += 1

    check = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    res = []
    for i in range(10):
        res += [check[i]] * cnt[i]
    res = " ".join(res)

    print("{} {}".format(t, res))


# T = int(input())
# for _ in range(T):
#     t, num = map(str, input().split())
#     num = int(num)
#
#     cnt_dict = {"ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0, "FIV":0, "SIX" : 0, "SVN" : 0, "EGT":0, "NIN":0}
#     checks = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     lst = list(map(str, input().split()))
#
#     for l in lst:
#         if l == "ZRO":
#             cnt_dict['ZRO'] += 1
#         elif l == "ONE":
#             cnt_dict['ONE'] += 1
#         elif l == "TWO":
#             cnt_dict['TWO'] += 1
#         elif l == "THR":
#             cnt_dict['THR'] += 1
#         elif l == "FOR":
#             cnt_dict['FOR'] += 1
#         elif l == "FIV":
#             cnt_dict['FIV'] += 1
#         elif l == "SIX":
#             cnt_dict['SIX'] += 1
#         elif l == "SVN":
#             cnt_dict['SVN'] += 1
#         elif l == "EGT":
#             cnt_dict['EGT'] += 1
#         elif l == "NIN":
#             cnt_dict['NIN'] += 1
#
#     res = []
#     for check in checks:
#         res += [check]  * cnt_dict[check]
#     res = " ".join(res)
#
#     print("{} {}".format(t, res))