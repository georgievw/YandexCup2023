#с переборчиком
def get_similarity(string, begin, word):
  similarity_count = 0
  for i in range(len(word)):
    if string[begin+i] == word[i]:
      similarity_count += 1
  return similarity_count

def make_haiku(string, word1, word2):
  word1_lst = list()
  word2_lst = list()

  for i in range(len(string)-len(word1)+1):
    sim = get_similarity(string, i, word1)
    if not word1_lst or word1_lst[-1][0] < sim:
      word1_lst.append((sim, i))

  for i in reversed(range(len(string)-len(word2)+1)):
    sim = get_similarity(string, i, word2)
    if not word2_lst or word2_lst[-1][0] < sim:
      word2_lst.append((sim, i))

  word1_i = word2_i = 0
  max_similarity = -1
  for i in range(len(word1_lst)):
    for j in range(len(word2_lst)):
      if word2_lst[j][1] - len(word1) >= word1_lst[i][1] and word2_lst[j][0] + word1_lst[i][0] > max_similarity:
        word1_i = word1_lst[i][1]
        word2_i = word2_lst[j][1]
        max_similarity = word2_lst[j][0] + word1_lst[i][0]
  return string[:word1_i] + word1 + string[word1_i+len(word1):word2_i] + word2 + string[word2_i+len(word2):]

string = input()
print(make_haiku(string, "Yandex", "Cup"))