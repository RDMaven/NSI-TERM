def max_square(table):
  rows = len(table)
  cols = len(table[0])
  max_side = 0
  for i in range(rows):
    for j in range(cols):
      if table[i][j] == 0:
        side = 1
        flag = True
        while flag:
          for k in range(i, i+side):
            if k >= rows or table[k][j] != 0:
              flag = False
              break
          for l in range(j, j+side):
            if l >= cols or table[i][l] != 0:
              flag = False
              break
          if flag:
            side += 1
        max_side = max(max_side, side)
  return max_side
"""
# test the function
table1 = [  [1, 0, 1], 
            [0, 0, 0], 
            [1, 0, 1]]
print(max_square(table1))  # should print 3
table2 = [  [1, 0, 1], 
            [1, 0, 0], 
            [1, 0, 1]]
print(max_square(table2))  # should print 2
"""
if __name__ == "__main__":

    nbLignes, nbColonnes = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(nbLignes)]
    print(max_square(table))