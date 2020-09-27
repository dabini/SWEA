m = "acbbcdc"
k= "abc"
# res = "cbdc"


answer = ''
idx = 0
end = len(k)
for cha in m:
    if idx == end or cha != k[idx]:
        answer += cha
    else:
        idx += 1
print(answer)