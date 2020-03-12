for t in range(1, int(input())+1):
    W, H, N = map(int, input().split())
    x, y = map(int, input().split())

    ans = 0
    for _ in range(N-1):
        tx, ty = map(int, input().split())

        if x == tx: ans += abs(y -ty) #수직이동
        elif y == ty: ans += abs(x - tx) #수평이동
        elif (x < tx and y > ty) or (x > tx and y < ty):
            ans += abs(x - tx) + abs(y - ty)
        else:
            ans += max(abs(x - tx),  abs(y - ty))

        x, y = tx, ty
