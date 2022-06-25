## 행렬 회전 ##

## 시간복잡도 O(N)
## N X N 사이즈인 것을 명시
def Solution():
  # 4 X 4
  matrix = [[1, 2, 3, 4],
            [5, 6, 7, 8,],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

  print("origin: {}".format(matrix))
  rotateMatrix(matrix)
  print("rotated: {}".format(matrix))
  
def rotateMatrix(matrix):
  N = len(matrix)
  M = len(matrix[0])
  
  for layer in range(int(N/2)):
    first: int = layer
    last: int = M - 1 - layer
    for i in range(first, last):
      offset: int = i - first # last에서 한칸씩 줄어들어야함. 
      lt = matrix[first][i]
      #lb -> lt
      matrix[layer][i] = matrix[last-offset][first]
      #rb -> lb
      matrix[last-offset][first] = matrix[last][last-offset]
      #rt -> rb       
      matrix[last][last-offset] = matrix[i][last]
      #lt -> rt
      matrix[i][last] = lt


if __name__ == "__main__":
  Solution()


