# deque module use double linked list

from collections import deque

q = deque([1, 2, 3])
print(q)

q.append(4)
print(q)

q.popleft()
q.pop()
print(q)

q.appendleft(5)
print(q)

q.rotate(1)
print(q)

q.rotate(2)
print(q)

q.rotate(3)
print(q)

q.rotate(4)
print(q)

q.rotate(-1)
print(q)