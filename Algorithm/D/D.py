def ford(edges, nodes, s, visited):
  dist = dict.fromkeys(nodes, float('inf'))
  dist[s] = 0
  visited[s] = 1
  for j in range(len(nodes)):
    is_updated = False
    for edge in edges:
      if dist[edge[0]] + edge[2] < dist[edge[1]]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        visited[edge[1]] = 1
        is_updated = True
  if is_updated:
    return True
  else:
    return False

def has_bad_cycle(edges, nodes):
  visited = dict.fromkeys(nodes, 0)
  for node in nodes:
    if visited[node] == 0:
      result = ford(edges, nodes, node, visited)
      if result:
        return True
  return False

f = open('input.txt')
n, m = map(int, f.readline().split())
edges = list()
nodes = set()
for _ in range(m):
  line = f.readline().split()
  nodes.add(int(line[0])-1)
  nodes.add(int(line[1]))
  if line[2] == ">=":
    edges.append((int(line[0])-1, int(line[1]), (-1)*int(line[3])))
    continue
  if line[2] == "<=":
    edges.append((int(line[1]), int(line[0])-1, int(line[3])))
    continue

if has_bad_cycle(edges, nodes):
  print("NO")
else:
  print("YES")