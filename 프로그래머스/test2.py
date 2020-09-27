blocks = [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
l = len(blocks)
lst = [[0 for j in range(i+1)] for i in range(l)]

for num in range(l):
    block = blocks[num]
    lst[num][block[0]] = block[1]
# print(lst)

for j in range(1, l):
    for i in range(j+1):
        if lst[j][i]:
            sm = lg =i
            while sm:
                lst[j][sm-1] = lst[j-1][sm-1] - lst[j][sm]
                sm -= 1
            while lg <j:
                lst[j][lg+1] = lst[j-1][lg] - lst[j][lg]
                lg += 1
answer = sum(lst, [])
print(answer)