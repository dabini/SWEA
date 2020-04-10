# T= int(input())
# for t in range(T):
#     N, M, L = map(int, input().split())
#     lst = list(map(int, input().split()))
#     for m in range(M):
#         idx, num = map(int, input().split())
#         lst.insert(idx, num)
#
#     print("#{} {}".format(t+1, lst[L]))

#LinkedList 활용
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.size += 1
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
                self.size += 1

    def find(self, data):
        cur = self.head
        idx = 0
        while cur != None:
            if cur.data == data:
                return idx

            cur = cur.next
            idx += 1
        return None

    def insert(self, idx, data):
        node = Node(data)
        cur = self.head
        cur_idx = 0
        pre_node = None

        if idx == 0:
            if self.head != None:
                next_node = cur
                self.head = node
                node.next = next_node
            else:
                self.head = None
        else:
            while cur_idx < idx:
                if cur != None:
                    pre_node = cur
                    cur = cur.next
                    cur_idx += 1
                else:
                    break
            if cur_idx == idx:
                node.next = cur
                pre_node.next = node
            else:
                return None

    def pop(self, idx):
        cur_idx = 0
        cur = self.head
        pre_node = None

        if idx == 0:
            self.head = cur.next
        else:
            while cur_idx <idx:
                if cur.next:
                    pre_node = cur
                    cur = cur.next
                    cur_idx += 1
                else:
                    break
            if cur_idx == idx:
                pre_node.next = cur.next
                return cur.data
            else:
                return None

    def clear(self):
        self.head = None

T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))
    linked = LinkedList()
    for num in lst:
        linked.append(num)

    for m in range(M):
        idx, data = map(int, input().split())
        linked.insert(idx, data)

    print("#{} {}".format(t+1, linked.pop(L)))