#신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.

# headlines = input()
# headline = ""
# for line in headlines:
#     line = line.upper()
#     headline += line
# print(headline)

#주어진 숫자만큼 # 을 출력해보세요.
#
# num = int(input())
#
# print("#"*num)

# 서랍의 비밀번호가 생각이 나지 않는다.
#비밀번호 P는 000부터 999까지 번호 중의 하나이다.
#주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.
#예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
#P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자

# password = input().split(" ")
#
# p = int(password[0])
# k = int(password[1])
# cnt = 1
# while p > k:
#     if p == k:
#         break
#     else:
#         k += 1
#         cnt += 1
# print(cnt)

#2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
# num = int(input())
#
# for n in range(1, num+1):
#     two = input().split(" ")
#     a = int(two[0])
#     b = int(two[1])
#     print(f'#{n} {a//b} {a%b}')

#대각선 출력하기
#
# for i in range(5):
#     output = list('+++++')
#     output[i] = '#'
#     print(''.join(output))

#1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
# n = int(input())
# total = 0
# for i in range(1, n+1):
#     total += i
# print(total)

#두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.

# cal = input().split(" ")
# a = int(cal[0])
# b = int(cal[1])
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)

# 입력으로 1개의 정수 N 이 주어진다.#
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
#
# N = int(input())
# lst = []
#
# for i in range(1, N+1):
#     if N % i == 0:
#         lst.append(str(i))
# print(" ".join(lst))

#A와 B가 가위바위보를 하였다.
#가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
#A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

# game = input().split(" ")
#
# a = int(game[0])
# b = int(game[1])
#
# if a == 1:
#     if b == 2:
#         print("B")
#     else:
#         print("A")
# elif a == 2:
#     if b == 1:
#         print("A")
#     else:
#         print("B")
# else:
#     if b == 1:
#         print("B")
#     else:
#         print("A")

#1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
#주어질 숫자는 30을 넘지 않는다.

# num = int(input())
# lst = []
# num <= 30
# for n in range(0, num+1):
#     n = 2 ** n
#     lst.append(str(n))
# print(' '.join(lst))

#주어진 숫자부터 0까지 순서대로 찍어보세요

# num = int(input())
# lst = []
# for i in range(num+1):
#     lst.append(str(i))
# new = lst[::-1]
# print(' '.join(new))
