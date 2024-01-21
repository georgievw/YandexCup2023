from random import randint

class YCMultiSet:
  def __init__(self, xs, n, ys, m):
    self.xs = xs
    self.ys = ys
    self.values = [(i, j) for i in range(n) for j in range(m)]

  def get_gcd(self, a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    if min_num == 0:
      return max_num
    return self.get_gcd(max(a, b) % min(a, b), min(a, b))

  def partition(self, left, right, pivot):
      pivot_left = left - 1
      pivot_right = left
      for n in range(left, right+1):

        if self.xs[self.values[n][0]]*self.ys[pivot[1]] > self.xs[pivot[0]]*self.ys[self.values[n][1]]:
          continue

        if self.xs[self.values[n][0]]*self.ys[pivot[1]] == self.xs[pivot[0]]*self.ys[self.values[n][1]]:
          self.values[n], self.values[pivot_right] = self.values[pivot_right], self.values[n]
          pivot_right += 1
          continue

        self.values[n], self.values[pivot_right], self.values[pivot_left+1] = self.values[pivot_right], self.values[pivot_left+1], self.values[n]

        pivot_right += 1
        pivot_left += 1

      return pivot_left, pivot_right

  def k_stat(self, begin, end, index):
      pivot = self.values[randint(begin, end)]
      l, r = self.partition(begin, end, pivot)
      if index < r and index > l:
        return pivot
      if index <= l:
        return self.k_stat(begin, l, index)
      if index >= r:
        return self.k_stat(r, end, index)

  def get_k(self, k):
    
    indexes = self.k_stat(0, len(self.values)-1, k-1)
    dividend = self.xs[indexes[0]]
    divisor = self.ys[indexes[1]]
    gcd = self.get_gcd(dividend, divisor)
    return (int(dividend / gcd), int(divisor / gcd))

  def set_x(self, i, xi):
    self.xs[i-1] = xi
    return

  def set_y(self, i, yi):
    self.ys[i-1] = yi
    return

f = open("input.txt")
n, m, q = map(int, f.readline().split())
xs = list(map(int, f.readline().split()))
ys = list(map(int, f.readline().split()))

mset = YCMultiSet(xs, n, ys, m)

for _ in range(q):
  command = list(map(int, f.readline().split()))
  if command[0] == 1:
    print(*mset.get_k(command[1]))
    continue
  if command[0] == 2:
    mset.set_x(command[1], command[2])
    continue
  if command[0] == 3:
    mset.set_y(command[1], command[2])
    continue