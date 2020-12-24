def campagnePrevention(mat):
    n = len(mat[0])
    res = [0]*6
    over60 = 0 #inutilise

    for i in range(n):
        if mat[1][i] >=1.26 or mat[2][i] >= 2.0:
            res[0]+=1
        if mat[1][i] >=1.26 and mat[0][i] > 60:
            res[1]+=1
        if mat[2][i] >= 2.0 and mat[0][i] > 60:
            res[2]+=1
        if mat[1][i] >=0.45 and mat[1][i]<1.26:
            res[3]+=1
        if mat[0][i]>60:
            over60+=1
        if (mat[1][i] >=1.26 or mat[2][i] >= 2.0) and mat[0][i]>60:
            res[4]+=1
        if mat[1][i] >=1.6 and mat[1][i] > res[5]:
            res[5] = mat[1][i]
    res[4] = 100*float(res[4])/n #enonce surprenant
    return res
#print(campagnePrevention([[65.0,20.0,35.0,58.0,62.0,80.0,79.0,75.0],
#                          [2.0,1.10,0.42,1.61,0.8,1.29,1.27,1.2],
#                          [1.1,0.9,0.6,2.2,2.1,1.7,0.6,2.12]])) #should return [6.0,3.0,2.0,1.0,62.5,2.0]
