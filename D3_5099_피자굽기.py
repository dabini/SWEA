# def isEmpty():
#     return front == rear
# def isFull():
#     return (rear +1) % len(queue) == front
#
# def deQueue():
#     global front
#     if not isEmpty():
#         front = (front+1) % len(queue)
#         return queue[front]
#
# def enQueue(item, idx):
#     global rear
#     if isFull():
#         for q in range(len(queue)):
#             queue[q] //= 2
#             if queue[q] == 0:
#                 deQueue()
#                 res.pop()
#     else:
#         rear = (rear +1) % len(queue)
#         queue[rear] = item
#         res.append(idx)

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    front = rear = 0
    queue = []
    for n in range(N):
        queue.append([pizza[n], n])

    k = 0
    while len(queue) != 1:
        queue[0][0] //= 2

        if queue[0][0] == 0:
            if N + k < M:
                queue.pop(0)
                queue.append([pizza[N+k], N+k])
                k += 1
            elif N + k >= M:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

    print("#{} {}".format(t+1, queue[0][1] +1))