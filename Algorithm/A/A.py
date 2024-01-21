n = int(input())
a_lst = map(int, input().split())

stack = list()
for a in a_lst:
  while stack and stack[-1] >= a:
    stack.pop()
  stack.append(a)

n_divided = 0
for min_a in stack:
  if min_a == n_divided + 1:
    n_divided += 1
    continue
  break

print(n_divided)