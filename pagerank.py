#Note : cet exercice semble plus complique que le niveau du cours

def dout(A):
	d = [0]*len(A)
	for i in range(len(A)):
		for j in range(len(A[0])):
			d[i]+=A[i][j]
	return d 
def din(A):
	d = [0]*len(A[0])
	for i in range(len(A)):
		for j in range(len(A[0])):
			d[j]+=A[i][j]
	return d 
def transpose(A): 
	At = [[0]*len(A) for i in range(len(A[0]))]
	for i in range(len(A)):
		for j in range(len(A[0])):
			At[j][i] = A[i][j]
	return At
def mult(A,v):
	res = [0]*len(A)
	for i in range(len(A)):
		for j in range(len(A[0])):
			res[i] += A[i][j]*v[j]
	return res
def probabilityMatrix(A):
	d = dout(A)
	for i in range(len(A)):
		for j in range(len(A[0])):
			A[i][j] /= d[i]
	return A 

def score(A):
	d = din(A)
	somme =0 
	for i in range(len(d)):
		somme += d[i]
	for i in range(len(d)):
		d[i] /= somme 

	P = probabilityMatrix(A)
	Pt = transpose(P)
	score = mult(Pt,d) 
	n = 10 #nombre d'iteration predefini (on regarde pas la convergence)
	for i in range(n):
		score = mult(Pt,score)
	return score


A =[[0,2,1],
	[3,0,1],
	[1,2,0]]
print(probabilityMatrix(A))
print(score(A))
