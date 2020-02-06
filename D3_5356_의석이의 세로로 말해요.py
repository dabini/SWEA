T = int(input())

for t in range(T):
    text = [['*'] * 15 for _ in range(15)]
    word = ""

    for k in range(5):
        w = input()
        for i in range(len(w)):
            text[k][i] = w[i]

    for y in range(15):
        for x in range(15):
            if text[x][y] != '*':
                word += text[x][y]

    print("#{} {}".format(t+1, word))