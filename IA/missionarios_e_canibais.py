
#caso onde todos estão do lado objetivo do rio
SOLUTION = (0, 0, 0)

#O movimento é seguro?
#Autoriza apenas movimentos que não matem missionários
def isSafe(M, C):
	#neste caso teríamos um missionário isolado no outro lado
	if M == 2 and C == 1:
		return False       
	if M >= C:
		return True
	return False

#este método retorna todos os possíveis estados, incluindo o passo de desfazer
#alguma ação realizada préviamente
def NextState(M, C, B):
	state = []
	Mc = 3 - M
	Cc = 3 - C

	if B == 0:
	#Quando B == 0, temos a barco na borda objetivo,
	#assim precisamos que alguns elementos votem com o barco para prosseguir	

		for i in range(1, 3):
			#mandando 1 ou 2 missionários para a borda original
			if Mc - i >= 0 and isSafe(M+i, C):
				state.append((M+i, C, 1))
			#mandando 1 ou 2 canibais para a borda original
			if Cc - i >= 0 and isSafe(M, C+i):
				state.append((M, C+i, 1))
		#mandando 1 missionário e 1 canibal para a borda original
		if Mc-1 >= 0 and Cc - 1 >=0 and isSafe(M+1, C+1):
			state.append((M+1, C+1, 1))
		
		return state
	else:

		#Aqui, diferente do anterior, temos B==1, onde temos o barco
		#na borda original
		for i in range(1, 3):
			#mandando 1 ou 2 missionários para a borda objetivo
			if M - i >= 0 and isSafe(M-i, C):
				state.append((M-i, C, 0))
			#mandando 1 ou 2 canibais para a borda objetivo
			if C - i >= 0 and isSafe(M, C-i):
				state.append((M, C-i, 0))
		#mandando 1 missionário e 1 canibal para a borda objetivo
		if M-1 >= 0 and C - 1 >=0 and isSafe(M-1, C-1):
			state.append((M-1, C-1, 0))
		return state

#definimos uma função recursiva que avança na árvore de busca
#assim ela faz busca de todas as soluções a partir do nó vigente
def MeC(M, C, B, caminho, Visitados):
	#solução encontrada	
	if (M, B, C) == SOLUTION:
		return caminho
	Fcaminhos = []#futuros caminhos que tomaremos na árvore
	estados = NextState(M, C, B)#todos os possíveis estados
	if estados == None: return None 

	for s in estados:
		#Para que não fiquemos percorrendo o mesmo nó diversas vezes
		#É utilizado um vetor de tuplas visitadas que minimiza a execução
		if s  not in Visitados:
			cam = MeC(s[0], s[1], s[2], caminho + [s], Visitados+[s])
			if cam != None:
				#alocamos o caminho na lista de todos os 
				#possíveis caminhos até a solução
				Fcaminhos.append(cam)

	if Fcaminhos == []: return None
	#retornamos o menor caminho, ignorando possíveis caminhos de mesmo tamanho,
	#Pois	isso exigiria uma alteração na lógica implementada	
	return min(Fcaminhos)
	
if __name__ == "__main__":
	Caminho = MeC(3, 3, 1, [(3, 3, 1)], [])
	print('A menor solução tem tamanho', len(Caminho)-1, ' em relação às arestas. Veja:')
	for tupla in Caminho:
		print(tupla, end = ' ')
	print()
