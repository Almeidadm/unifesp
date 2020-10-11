
#Criando uma sequência que indique quais alterações precisam ser feitas
def Ki(seq, target):
	res = ''
	for i in range(len(seq)):
		if seq[i] != target[i]:	res += '1' # caso precise mutar
		else: res += '0' #caso precise manter
	return res

#Definindo a probabilidade de mutação da sequência Ki pela
#pela propriedade da sequência de Bernouli com k=0
def ProbMutation(seq, prob):
	res = 1
	for i in seq:
		if i == '0':
			res *= (1-prob)
		else:
			res *= prob

	return res

#Cruzando duas sequências num dado ponto
def Cross(seq1, seq2, point):
	child1 = seq1[:point] + seq2[point:]
	child2 = seq2[:point] + seq1[point:]
	return child1, child2 #retorna os dois possívei filhos


def SolveP(seq1, seq2, target, point, prob):
	#Tomamos os filhos do cruzamento entre as duas sequências dadas	
	child1, child2 = Cross(seq1, seq2, point)

	#Calculamos a probabilidade de mutação da sequência de manipulação
	#Para a sequência alvo, sequência que desejamos atingir
	#Fazemos com ambos os filhos
	probMutChild1 = ProbMutation(Ki(child1, target), prob)
	probMutChild2 = ProbMutation(Ki(child2, target), prob)

	#Pela união das probabilidades acontecerem simultaneamente
	res = probMutChild1 + probMutChild2 - probMutChild1*probMutChild2

	return res


if __name__ == '__main__':
	n = int(input())
	for i in range(0, n):
		lenght = input()
		inp = input()
		inp = inp.split(' ')
		point = int(inp[0])
		prob = float(inp[1])
		seq1 = input()
		seq2 = input()
		target = input()
		print('%.7f'%SolveP(seq1, seq2, target, point, prob))