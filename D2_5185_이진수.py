hexa = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
         'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def binary(n):
    global tmp
    a = b = 0
    for i in range(4):
        a = n // 2
        b = n % 2
        tmp = str(b) + tmp
        n = a

T = int(input())
for t in range(T):
    N, num = map(str, input().split())
    N = int(N)

    res = ''
    for n in num:
        tmp = ''
        binary(hexa[n])
        res += tmp
    print("#{} {}".format(t+1, res))