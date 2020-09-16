food_times = [3, 1, 2]
k = 5
answer = 0
num = 0
N = len(food_times)
while num <= k:
    for i in range(N):
        if num > k:
            break
        if food_times[i]:
            num += 1
            food_times[i] -= 1
            answer = i + 1

print(answer)
