#10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

# num = int(input())
#
# for i in range(1, num+1):
#     ten_num = input().split(" ")
#     sum = 0
#     for ten in ten_num:
#         if int(ten) % 2:
#             sum += int(ten)
#     print(f"#{i} {sum}")

#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

# num = int(input())
#
# for i in range(1, num+1):
#     input_num = input().split(" ")
#     sum_num = 0
#     for inp in input_num:
#         sum_num += int(inp)
#     avg = sum_num / len(input_num)
#     print(f'#{i} {round(avg)}')

#2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

# num = int(input())
# for i in range(1, num+1):
#     num_lst = input().split(" ")
#     left_n = int(num_lst[0])
#     right_n = int(num_lst[1])
#     if left_n > right_n:
#         print(f'#{i} >')
#     elif left_n < right_n:
#         print(f'#{i} <')
#     else:
#         print(f'#{i} =')

#10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
# num = int(input())
# for i in range(1, num+1):
#     n_lst = input().split(" ")
#     new = []
#     for n in n_lst:
#         n = int(n)
#         new.append(n)
#     print(f'#{i} {max(new)}')

#중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
#입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

# n = int(input())
# num = input().split(" ")
# lst = []
# for k in num:
#     k = int(k)
#     lst.append(k)
#     lst.sort()
#     out = int((n-1)/2)
# print(lst[out])

#하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
# raw = str(input())
# total = 0
#
# for i in range(len(raw)):
#     total += int(raw[i])
# print(total)

#년/월/일 출력
# n = int(input())
# for i in range(1,n+1):
#     cal = str(input())
#     year =  cal[0:4]
#     month = cal[4:6]
#     day = cal[6:]
#     if month in ['01', '03', '05', '07', '08', '10', '12']:
#         if int(day) < 1 or int(day) > 31:
#             print(f'#{i} -1')
#         else:
#             print(f'#{i} {year}/{month}/{day}')
#     elif month in ['04', '06', '09', '11']:
#         if int(day) <1 or int(day) > 30:
#             print(f'#{i} -1')
#         else:
#             print(f'#{i} {year}/{month}/{day}')
#     elif month == '02':
#         if int(day) < 1 or int(day) > 28:
#             print(f'#{i} -1')
#         else:
#             print(f'#{i} {year}/{month}/{day}')
#     else:
#         print(f"#{i} -1")
