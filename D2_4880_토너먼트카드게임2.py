def f(i, j):
    if i ==j:
        return i
    else:
        r1 = f(i, (i+j)//2)
        r2 = f((i+j)//2+1,j)
        r = [r1, r2]
        return win(r1, r2)

def win(p1, p2):
    if card[p1] == card[p2]:
        return p1
    elif card[p1] == 2 and card[p2] == 1:
        return p1
    elif card[p1] == 3 and card[p2] == 2:
        return p1
    elif card[p1] == 1 and card[p2] == 3:
        return p1
    else:
        return p2

T = int(input())
for t in range(T):
    N = int(input())
    card = [0] + list(map(int, input().split()))
    print("#{} {}".format(t+1, f(1,N)))