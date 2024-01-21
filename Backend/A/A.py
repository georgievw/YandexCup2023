from collections import deque

def get_sum(lst, n, m):
  result = 0
  dq = deque([0]*(n+1))
  for i in reversed(range(m)):
    if lst[i] != 0:
      result += lst[i]**2 + (dq[0] - dq[lst[i]])
      dq.appendleft(dq[0]+lst[i])
      dq.pop()
  return result

n, m = map(int, input().split())
lst = list(map(int, input().split()))
print(get_sum(lst, n, m))