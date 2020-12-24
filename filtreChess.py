def filtreChess(A):
    nRow,nCol = len(A),len(A[0])
    out = [[0]*nCol for i in range(nRow)]
    for i in range(nRow):
        for j in range(nCol):
            inc =5*A[i][j]
            if j>0:
                inc -= A[i][j-1]
            if j<nCol-1:
                inc -= A[i][j+1]
            if i>0:
                inc -= A[i-1][j]
            if i<nRow-1:
                inc -= A[i+1][j]
            out[i][j] = inc
    return out
#print(filtreChess([[1]*5 for i in range(5)]))
