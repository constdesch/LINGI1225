def fournitureStat(A):
    n = len(A[0])
    idx = int(input("Entrez le numero de la fourniture:"))
    idx -=1
    if idx<0 or idx >len(A[0])-1:
        print("erreur : Aucune fourniture n'est associee a ce numero")
    mean = 0
    max = A[0][idx]
    min = A[0][idx]
    for i in range(4):
        mean += 0.25*A[i][idx]
        if A[i][idx] > max:
            max = A[i][idx]
        if A[i][idx] < min:
            min = A[i][idx]
    print("moyenne : {} ; max : {} ; min : {}".format(mean,max,min))
    if A[0][idx] > mean:
        print("La quantite moyenne en 2012 est superieure a la moyenne")
    else:
        print("La quantite moyenne en 2012 est inferieure a la moyenne")
# fournitureStat([[15,30,35,25,50,10,49],
#                 [20,30,40,10,30,9,40],
#                 [10,20,32,18,35,9,50],
#                 [15,17,42,10,40,19,27]])
