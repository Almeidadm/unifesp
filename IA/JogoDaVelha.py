

#Gera todos os possiveis movimentos
def Movimentos(seq):
	movimentos = []
	#Toda posição vazia é factivel de movimento
	for i in range(len(seq)):
		aux = ''		
		if seq[i] == '.':
			aux = seq[:i] + 'X' + seq[i+1:]					
			movimentos.append(aux)
	return movimentos

#confere se é possivel ser vitorioso
#com o dado tabuleiro
def Vence(seq):
	if '.XX' in seq:
		return True
	if 'X.X' in seq:
		return True
	if 'XX.' in seq:
		return True
	return False


#Os jogadores são dados como tipos booleanos
#dessa forma nosso jogador objetivo é True
def Solve(seq, jogador):
	#caso seja possivel vencer com este tabuleiro
	#retorna o jogador vencedor	
	if Vence(seq):
		return jogador
	
	for mov in Movimentos(seq):

		#Se este movimento garante a vitoria para o jogador
		#retornamos ele próprio, True
		if jogador and Solve(mov, not jogador):
			return jogador
		#Se este movimento garante uma vitoria para o oponente
		#retornamos False, o oponente
		elif not jogador and not Solve(mov, not jogador):
			return jogador
		
	#Caso nenhum movimento garantiu a vitoria do jogador
	if jogador:
		return False
	#Caso nenhum movimento garantiu vitoria do oponente
	return True

if __name__ == '__main__':
	
	while True:
		n = int(input())
		if n == 0:	break
		seq = input()
		if Solve(seq, True):
			print('S')
		else:
			print('N')