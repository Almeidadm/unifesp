import random

#A função de avaliação que queremos otimizar
def Fitness(x):
	return 1 + 2*x - x**2

#cria um vetor de elementos com posições aleatórias
def CreatePosition(n):
	X = [random.random() for i in range(n)]
	#gerando valores > 1 e negativos	
	for x_i in X:	x_i = (x_i - 0.5)*10
	return X

#cria um vetor de elementos com velocidades aleatórias
def CreateVelocity(n):
	V = [random.random() for i in range(n)]
	return V

#Atualiza a volocidade das partículas
def UpdateVel(V, w, c1, c2, r1, r2, LBP, GBP, X):
	nV = []	
	for i in range(len(V)):
		nV.append(w*X[i]+c1*r1*(LBP[i]-X[i])+c2*r2*(GBP-X[i]))
	return nV

#Atualiza a posição das partículas
def UpdatePos(X, V):
	nX = []
	for i in range(len(X)):
		nX.append(X[i]+V[i])
	return nX

#Função para encontrar a posição que otimiza a fitness
def BestFitness(X):
	best = 0
	x = 0
	for x_i in X:
		if Fitness(x_i) > best:
			best = Fitness(x_i)
			x = x_i
	#retorna o valor da fitness e sua posição correspondente
	return best, x

#Avalia qual é a melhor posição em que cada uma das particulas já esteve
def LocalBestPosition(LBP, X):
	for i in range(len(X)):
		if Fitness(LBP[i])<Fitness(X[i]):
			LBP[i] = X[i]
		

#Resolve de fato o problema
def PSO(n, w, c1, c2, iterations):
	X = CreatePosition(n)
	V = CreateVelocity(n)
	#vetor com o valor da fitness de todas as posições
	F = [Fitness(x_i) for x_i in X] 
	#Como é a inicialização a melhor posição é a que se está	
	LBP = X
	GBF, GBP = BestFitness(X)
	LBF = GBF#local é igual por ser a inicialização
	i = 0
	while i < iterations:
		r1 = random.random()
		r2 = random.random()
		V = UpdateVel(V, w, c1, c2, r1, r2, LBP, GBP, X)
		X = UpdatePos(X, V)
		LBF, pLBF = BestFitness(X)
		if LBF > GBF:
			GBF = LBF
			GBP = pLBF
		LocalBestPosition(LBP, X)
		i+=1
	return GBF, GBP

if __name__ == '__main__':
	print('insira em ordem o número de particulas, w, c1, c2 e as iterações:', end=' ')
	aux = input()
	n, w, c1, c2, ite = aux.split(' ')
	print(PSO(int(n), float(w), float(c1), float(c2), int(ite)))

		
	
	