# field = [[0]*300 for _ in range(300)]
field = [[0]*5 for _ in range(5)]

k = 1
x = 1
for y in range(1, 5):
    while y >=1 and x <= y:
        field[y][x] = k
        k += 1
        if x == y and y == 1:
            break
        y -=1
        x += 1

print(field)


# k = 0
# n = 0
# for y in range(1, 5):
#     m = 1
#     l = 1
#     for x in range(1, 5):
#         m = k + m
#         field[y][x] = m
#         l += 1
#         m = m +l
#     n += 1
#     k = k + n
# print(field)
