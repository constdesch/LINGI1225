def perimetreSapin(M):
	count = 0 
	for i in range(len(M)):
		flag_g = False
		flag_d = False
		for j in range(len(M[0])):
			#gauche a droite
			if M[i][j] == '+' and flag_g == False:
				count+=1 
				flag_g = True
			#droite a gauche
			if M[i][len(M[0])-1-j] == '+' and flag_d == False:
				count += 1
				flag_d = True

	for j in range(len(M[0])):
		flag_h = False
		flag_b = False
		for i in range(len(M)):
			if M[i][j] == '+' and flag_h == False:
				count += 1
				flag_h = True
			if M[len(M)-1-i][j] and flag_b == False:
				count +=1 
				flag_b = True
	return count 

M =[[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,'+','+',0,0],
	[0,'+','+','+','+',0],
	['+','+','+','+','+','+'],
	[0,0,'+','+',0,0],
	[0,0,'+','+',0,0],
	[0,0,'+','+',0,0]]
print(perimetreSapin(M)) #should print 24	