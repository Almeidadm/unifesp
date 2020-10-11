import numpy as np

def Mdistance(c1, c2):
	return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])

def fitness(ind, pontos):
	#print(ind)
	f = 0
	for i in range(len(ind)-1):
		#print(pontos[ind[i]], pontos[ind[i+1]])
		f += Mdistance(pontos[ind[i]], pontos[ind[i+1]])
	#	print(Mdistance(pontos[ind[i]], pontos[ind[i+1]]))
	f += Mdistance(pontos[ind[0]], pontos[ind[-1]])
#	print()
	return f

def crossover(ind1, ind2):
	aux1 = ind1[:6] + ind2[6:]
	aux2 = ind2[:6] + ind1[6:]
	return aux1, aux2

def mutation(ind):
	ind[3], ind[7] = ind[7], ind[3]
	
def AG(pop, pontos, i):
	if i == 0:
		for ind in pop:
			print('individuo: ',ind, 'fitness:', fitness(ind, pontos))
		return

	popAux = pop
	n1, n2 = crossover(pop[0], pop[1])
	n3, n4 = crossover(pop[2], pop[3])
	mutation(n1)
	mutation(n2)
	mutation(n3)
	mutation(n4)
	popAux.append(n1)
	popAux.append(n2)
	popAux.append(n3)
	popAux.append(n4)  
	f = []
	for ind in popAux:
		f.append(fitness(ind, pontos))
	arr = np.array(f)
	arr = list(arr.argsort()[:4])
	pop = []
	for j in arr:
		pop.append(popAux[j])

	AG(pop, pontos, i-1)
	return
	
if __name__ == '__main__':
	pontos = { 0: (1,5), 1: (4,6), 2: (7,5), 3: (5,4), 4:(9, 4), 5: (2, 3),
						6: (4, 2), 7: (6,2), 8: (1, 1), 9: (5, 1), 10: (3, 0), 11: (9, 0)}

	
	pop = [list(np.random.permutation(12)) for i in range(4)]	
	
	print(np.matrix(pop))
	
	print('População para 15 iterações:')
	AG(pop, pontos, 15)
	print()
	print('População para 30 iterações:')
	AG(pop, pontos, 30)