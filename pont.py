def pont(A,ref):
    n = len(A[0]) #nombre de ponts
    for i in range(n):
        A[2][i] = A[4][i]*A[5][i]
    minD = math.sqrt(sum( (A[i][0]-ref[i])**2 for i in range(4)))
    minidx=0
    for j in range(n):
        dist = math.sqrt(sum((A[i][j]-ref[i])**2 for i in range(4)))
        if dist < minD:
            minD = dist
            minidx = j
    #print(math.sqrt(sum((A[i][3]-ref[i])**2 for i in range(4))))
    return minidx

# print(pont([[65,12,25,35,50],
#             [20,30,40,10,30],
#             [0,0,0,0,0,0],
#             [14.9,8.4,6.4,7.12,13.3],
#             [80,75,60,100,65],
#             [4,2,3,2,6]],
#            [35,23,402,9.6]))
