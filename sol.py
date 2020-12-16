# SOLUTION EXAMENS LINGE1225 
# CONSTANTIN DE SCHAETZEN 


import math
#Bug des tests inginious? 
def arret(A):
    H = len(A)
    L = len(A[0])
    G = [-1,0]
    B = [-1,-1]
    for i in range(H):
        for j in range(L):
            if A[i][j] == 'B':
                B[0] = j
                B[1] = H-1-i
            if A[i][j] == 'G':
                G[0] = j
                G[1] = H-i-1
    dH = B[1]-G[1] 
    dL = B[0]-G[0]
    distance = math.sqrt(dH**2 + dL**2)
    if dL !=0:
        angle = math.atan(dH/dL) #angle en radian
    elif B[1]<G[1]:
        angle = -math.pi/2.0
    elif G[1]<B[1]:
        angle = math.pi/2.0
    angle *= 180/math.pi
    direction = 0
    if (B[0]>G[0]):
        direction =1
    elif (B[0]<G[0]):
        direction =-1
    return [direction,angle,distance]

def trajectoire(A):
    s = -1
    for i in range(len(A)):
        if A[i][0] == 1:
            s = i
    countV = 0
    for j in range(1,len(A[0])):
        if s>0 and A[s-1][j] == 1:
            countV+=1
            s -=1
        elif s<len(A)-1 and A[s+1][j] == 1:
            countV +=1
            s+=1
    print(countV)
    return len(A[0])-1 + countV*(math.sqrt(2)-1)

    def integrale(a,b,nbPoints):
    step = float((b-a))/(nbPoints-1)
    sum=0
    for i in range(1,nbPoints):
        f1 = f(a+i*step)
        f0 = f(a+(i-1)*step)
        sum += 1./2*(f1+f0)*step
    return sum

# Les tests semblent buguer sur inginious
# Problème en cas d'égalité, qui faire gagner? + Problème cohérence entre n et l'année de départ
def piloteLePlusRapide(A, n):
    nP = len(A)
    nC = len(A[0])
    nA = len(A[0][0])
    victoire = [0]*nP
    for k in range(nA-1-n,nA):
        for j in range(nC):
            t = A[0][j][k]
            winner = 0
            for i in range(nP):
                if A[i][j][k] != -1 and A[i][j][k] < t:
                    t = A[i][j][k]
                    winner = i
            victoire[winner]+=1
    max = -1
    best = -1
    for i in range(nP):
        if victoire[i]>=max:
            max = victoire[i]
            best = i
    return best


class Date:
    def __init__(self,jour,mois,annee):
        self.__jour = jour
        self.__mois = mois
        self.__annee= annee

    def getJour(self):
        return self.__jour
    def getMois(self):
        return self.__mois
    def getAnnee(self):
        return self.__annee
    def hier(self):
        if self.__jour != 1:
            self.__jour -=1
        else:
            if self.__mois in [1,2,4,6,8,9,11]:
                self.__jour = 31
                if self.__mois == 1:
                    self.__mois = 12
                    self.__annee -=1
                else:
                    self.__mois-=1
            elif self.__mois in [5,7,10,12]:
                self.__jour = 30
                self.__mois -=1
            else: #mois de mars
                if (self.__annee%4==0 and self.__annee%100!=0) or self.__annee%400==0:
                    self.__jour = 29
                    self.__mois-=1
                else:
                    self.__jour = 28
                    self.__mois-=1

def bataille(j1,j2):
    while(len(j1[0])!=0 and len(j2[0])!=0):
        c1 = j1[0][0]
        c2 = j2[0][0]
        if c1>c2 or (c1==1 and c2!=1) or (c1==c2 and j1[1][0]<j2[1][0]):
            j1 = [j1[0][1:len(j1[0])]+[c1]+[c2],j1[1][1:len(j1[1])]+[j1[1][0]]+[j2[1][0]]]
            j2 = [j2[0][1:len(j2[0])],j2[1][1:len(j2[1])]]
        elif c2>c1 or (c2==1 and c1!=1) or (c1==c2 and j2[1][0]<j1[1][0]):
            j2 = [j2[0][1:len(j2[0])] + [c1] + [c2], j2[1][1:len(j2[1])] + [j1[1][0]] + [j2[1][0]]]
            j1 = [j1[0][1:len(j1[0])], j1[1][1:len(j1[1])]]
    if len(j1[0]) == 0:
        return 2,j2
    return 1,j1

def valeurDroite(xA, yA, xB, yB, x):
    return yA + (x-xA)*(yA-yB)/(xA-xB)

def maximaLocaux(tab):
    l = []
    for i in range(1,len(tab)-1):
        if tab[i-1]<tab[i] and tab[i]>tab[i+1]:
            l+=[i]
    return l

def estVallee(tab,a,b):
    xA = a
    yA = tab[a]
    xB = b
    yB = tab[b]
    for i in range(a+1,b):
        if tab[i]>valeurDroite(xA,yA,xB,yB,i):
            return False
    return True

def plusGrandeVallee(tab):
    l = maximaLocaux(tab)
    max = -1
    vallee = [0,0]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[j]-l[i] > max and estVallee(tab,l[i],l[j]):
                vallee = [l[i],l[j]]
                max = l[j]-l[i]
    return vallee

class Casier:
    def __init__(self,bac):
        self.__bac = bac

    def avgAlcool(self):
        m = len(self.__bac)
        n = len(self.__bac[0])
        somme = 0.0
        count = 0
        for i in range(m):
            for j in range(n):
                if self.__bac[i][j].estPleine():
                    somme+=self.__bac[i][j].getAlcool()
                    count +=1 
        return (somme)/count

    def party(self,nom):
        m = len(self.__bac)
        n = len(self.__bac[0])
        for i in range(m):
            for j in range(n):
                if self.__bac[i][j].estPleine() and self.__bac[i][j].getNom() == nom:
                    self.__bac[i][j].boire()

    def isStronger(self,tab):
        for i in range(len(tab)):
            if tab[i].avgAlcool() >= self.avgAlcool():
                return False
        return True
