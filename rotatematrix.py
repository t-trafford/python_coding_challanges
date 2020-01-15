A = [
  [1,2,3,4],
  [4,5,6,4],
  [7,8,9,6],
  [10,11,12,8],
[13,14,15,22]
]

B = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

def rotate(A):
    n = len(A)
    m = len(A[0])
    for i in range(n):
            for j in range(m):
                if i < j:
                    A[i][j], A[j][i] = A[j][i], A[i][j]
    print(A)
    for l in A:
        l.reverse()

    print(A)

p = rotate(A)
