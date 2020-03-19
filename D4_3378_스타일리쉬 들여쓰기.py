def A_F(code, l):
    global af
    ab = 0
    cd = 0
    ef = 0
    for i in range(0, l):
        for j in range(len(code[i])):
            if code[i][j] == "(":
                ab += 1
            elif code[i][j] == ")":
                ab -= 1
            elif code[i][j] == "{":
                cd += 1
            elif code[i][j] == "}":
                cd -= 1
            elif code[i][j] == "[":
                ef += 1
            elif code[i][j] == "]":
                ef -= 1
    af.append((ab, cd, ef))


def RCS(af, indenp, p):
    org = []
    ab, cd, ef = af[0]
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                if p == 1:
                    org.append((R, C, S)) #모든 값이 후보기 때문에
                elif R*ab + C*cd + S*ef == indenp[1]:
                    org.append((R, C, S))
                for i in range(2, p):
                    ab, cd, ef = af[i -1]
                    dest = []
                    for R, C, S in org:
                        if R*ab + C*cd +S*ef == indenp[i]:
                            dest.append((R, C, S))
                    org = dest
                return org
T = int(input())
for t in range(T):
    p, q = map(int, input().split())
    indenp = [0] *p #들여쓰기 온점 개수 기록

    codep = []
    codeq = []

    for i in range(p):
        codep.append(input())
    for j in range(q):
        codeq.append(input())

    af = []
    A_F(codep, p) #괄호 개수

    for i in range(p):
        cnt = 0
        while codep[i][cnt] == ".":
            cnt += 1
        indenp[i] = cnt

    # R, C, S 후보 정하기
    rcs = RCS(af, indenp, p)

    af = [] #라인별 괄호 개수
    A_F(codeq, q)
    indenq = [0] * q
    for i in range(1, q):
        ab, cd, ef = af[i-1] #이전 줄 까지의 괄호수


    if rcs:
        R, C, S = rcs[0]
        ans = R*ab + C*cd + S*ef
        for x in rcs[1:]:
            R, C, S = x
            if R*ab + C*cd + S*ef != ans:
                indenq[i] = -1
                break

        if indenq[i] != -1:
            indenq[i] = ans