 def diagonal(self, A):
        n = len(A)
        b = [[] for i in range((2*n)-1)]
        for i in range(n):
            for j in range(n):
                sum = i+j
                b[sum].append(A[i][j])
        return b
