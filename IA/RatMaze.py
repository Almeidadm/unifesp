import numpy as np

#Se a posição é segura para ser visitada
def isSafe(mat, visited, x, y):
  if mat[x][y] == 0 or visited[x][y] == 1:
    return False
  return True

#Se a posição está dentro da matriz
def isValid(x, y, M, N):
  if x < M and y < N and x >= 0 and y >= 0:
    return True
  return False

def findLongestPath(mat, visited, i, j, x, y, maxDist, dist, M, N):
  if mat[i][j] == 0:
    return 0

  if i == x and j == y:
    return max(dist, maxDist)

  visited[i][j] = 1

#Descendo
  if isValid(i+1, j, M, N) and isSafe(mat, visited, i+1, j):
    maxDist = findLongestPath(mat, visited, i+1, j, x, y, maxDist, dist+1, M, N)
#A direita
  if isValid(i, j+1, M, N) and isSafe(mat, visited, i, j+1):
    maxDist = findLongestPath(mat, visited, i, j+1, x, y, maxDist, dist+1, M, N)
#A esquerda
  if isValid(i-1, j, M, N) and isSafe(mat, visited, i-1, j):
    maxDist = findLongestPath(mat, visited, i-1, j, x, y, maxDist, dist+1, M, N)
#Subindo
  if isValid(i, j-1, M, N) and isSafe(mat, visited, i, j-1):
    maxDist = findLongestPath(mat, visited, i, j-1, x, y, maxDist, dist+1, M, N)

  visited[i][j] = 0

  return maxDist

def main():

  all_results = []
  while True:
    line = input()
    x, y = int(line[0]), int(line[2])
    if x == 0 or y == 0:
      break
    mat = [[1 for i in range(x)] for j in range(y)]
    visited = [[0 for i in range(x)] for j in range(y)]
    for i in range(x):
      line = input()
      for l in range(len(line)):
        if line[l] == '#':
          mat[i][l] = 0

    paths_sizes = []
    for i in range(x):
      for j in range(y):
        if mat[i][j] == 1:
          for k in range(x):
            for l in range(y):
              if mat[k][l] == 1:
                paths_sizes.append(findLongestPath(mat, visited, i, j, k, l, 0, 0, x, y))
    all_results.append(np.amax(paths_sizes))

  for result in all_results:
    print(result)

if __name__ == '__main__':
  main()
