food_times = [3, 1, 2]
k = 5

if sum(food_times) <= k:
    answer = -1

food = []
for idx, value in enumerate(food_times):
    food.append((value, idx+1))

food.sort()
print(food, k)
