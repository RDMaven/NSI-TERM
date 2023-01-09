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
            for l in range(j, j+side):    
                if k >= rows or l >= cols or table[k][l] != 0:
                    flag = False
                    break
          if flag:
            side += 1
        max_side = max(max_side, side-1)
  return max_side

if __name__ == "__main__":

    nbLignes, nbColonnes = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(nbLignes)]
    print(max_square(table))