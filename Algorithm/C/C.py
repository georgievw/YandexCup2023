def get_n_i_ones(n, i):
  return 2**(i-1) * ((n+1)//2**i) + max(0, ((n+1)%2**i)-2**(i-1))

def get_sum(m):
  result = 0
  i = 1
  one_sum = get_n_i_ones(m, i)
  while one_sum != 0:
    result = (result + (one_sum*one_sum)*(2**(i-1))) % 1000000007
    i += 1
    one_sum = get_n_i_ones(m, i)
  return result

f = open("input.txt")
t = int(f.readline())
for _ in range(t):
  print(get_sum(int(f.readline())))