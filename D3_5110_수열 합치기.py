class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new

    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]:
                break
            cur = cur.next
        if cur is None:
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur == lst.head:
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)

def printL(lst):
    if lst.head is None:
        return
    cur = lst.tail
    cnt = 0
    while cur is not None:
        if cnt >= 10:
            break
        print(cur.data, end=" ")
        cur = cur.prev
        cnt += 1
    print()

T= int(input())
for t in range(T):
    N, M = map(int, input().split())
    linked = LinkedList()
    for m in range(M):
        add = list(map(int, input().split()))
        addList(linked, add)
    print("#{}".format(t+1), end=" ")
    printL(linked)

