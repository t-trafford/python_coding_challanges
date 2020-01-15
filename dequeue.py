from collections import deque


dq = deque([(1,2,3)])
print(dq)

n1,n2,n3 = dq.popleft()
print(n1)
print(n2)
print(n3)