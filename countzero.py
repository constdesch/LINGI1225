def countZero(A):
    nRow, nCol = len(A),len(A[0])
    if nRow != nCol:
        return #la matrice n'est pas carree
    res = [0]*4
    for i in range(nRow):
        for j in range(nCol):

            if A[i][j] == 0 and i>j: #strictement sous la diagonale principale
                if j<nCol-i-1: #strictement au dessus de la diagonale secondaire
                    res[0]+=1
                elif j>nCol-i-1: #strictement en dessous de la diagonale secondaire
                    res[3]+=1
            elif A[i][j]==0 and i<j: #strictement au dessus de la diagonale principale
                if j<nCol-i-1: #strictement au dessus de la diagonale secondaire
                    res[1]+=1
                elif j>nCol-i-1: #strictement en dessous de la diagonale secondaire
                    res[2]+=1
    return res
# print(countZero([[5,0,2,0,0],
#                  [0,0,0,0,0],
#                  [0,0,6,1,0],
#                  [2,1,1,1,0],
#                  [1,2,3,4,5]
#                  ])) #should return [3,3,3,0]
