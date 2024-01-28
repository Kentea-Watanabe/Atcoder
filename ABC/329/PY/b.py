N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
B = [A[i] - A[i - 1] for i in range(1, len(A))]

for i, v in enumerate(B):
     if v != 0:
          print(A[i+1])
          break