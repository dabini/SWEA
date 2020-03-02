# def Swim(i, Pay_total, q):
#     global sol, Pay_month, Plan, Pay_three, Pay, Pay_total2, k
#
#     if i >= 12:
#         if sum(Pay_total) < Pay[3]:
#             sol_TMP = sum(Pay_total)
#         else:
#             sol_TMP = Pay[3]
#
#         if sol_TMP < sol[-1]:
#             sol.append(sol_TMP)
#         return
#
#     else:
#         for j in range(i, 12):
#             Pay_total[:j] = Pay_month[:k] + Pay_total[k:i] + Pay_month[i:j]
#             if sum(Pay_month[j:j + 3]) <= Pay[2]:
#                 Pay_total[j] = Pay_month[j]
#                 Swim(j + 1, Pay_total[:j] + [Pay_month[j]] + Pay_total[j + 1:], j)
#             else:
#                 Pay_total[j:j + 3] = [Pay[2], 0, 0]
#                 Swim(j + 3, Pay_total[:j] + [Pay[2], 0, 0] + Pay_total[j + 3:], j)
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     Pay = list(map(int, input().split()))
#     Plan = list(map(int, input().split()))
#
#     Pay_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     Pay_three = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     Pay_total2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
#     for i in range(12):
#         if Pay[1] < Pay[0] * Plan[i]:
#             Pay_month[i] = Pay[1]
#         else:
#             Pay_month[i] = Pay[0] * Plan[i]
#
#     sol = [100000]
#
#     for i in range(12):
#         k = i
#         Swim(i, Pay_month[:i] + Pay_total2[i:], i)
#
#     print("#{} {}".format(test_case, sol[-1]))

# T = int(input())
# for t in range(T):
#     D, M, Tm, Y = map(int, input().split())
#     month = list(map(int, input().split()))
#     pay = [0 for _ in range(12)]
#     for i in range(12):
#         pay[i] = min(D * month[i], M)
#     n = 0
#     payment = sum(pay)
#     for i in range(1 << 12):
#         bp = 0
#         dumpay = 0
#         cnt = 0
#         for j in range(12):
#             if i & (1 << j):
#                 if cnt != 0:
#                     bp = 1
#                     break
#                 cnt = 2
#                 A = 0
#                 for k in range(3):
#                     if j + k < 12:
#                         A += pay[j + k]
#                 if A <= Tm:
#                     bp = 1
#                     break
#                 dumpay += Tm
#             else:
#                 if cnt:
#                     cnt -= 1
#                 else:
#                     dumpay += pay[j]
#         if bp == 0:
#             payment = min(dumpay, payment)
#     payment = min(payment, Y)
#     print('#{} {}'.format(t + 1, payment))



def pool(month, price):
    global min_pri, day, mon, three_mon
    if month >= 12:
        if price < min_pri:
            min_pri = price
    else:
        pool(month+1, price + cnt_lst[month+1] *day)
        pool(month+1, price + mon)
        pool(month+3, price + three_mon)

T = int(input())
for t in range(T):
    day, mon, three_mon, year = map(int, input().split())
    cnt_lst = [0] + list(map(int, input().split()))
    min_pri = year
    pool(0, 0)
    print("#{} {}".format(t+1, min_pri))
