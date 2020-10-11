
import numpy as np

def CriaTabuleiro(n, m):
	Tab = [[0 for i in range(m)] for j in range(n)]
	return Tab


def DispoePeças(Tab, pos):
	i = -1
	#percorrendo a matriz de baixo para cima
	while i >= -len(Tab):
		for j in range(len(Tab[i])):
			#conferindo posição válidas//epaços brancos
			if (j+1)%2 !=0  and abs(i)%2 != 0:
				Tab[i][j] = pos.pop(0)
			elif (j+1)%2 == 0 and abs(i)%2 == 0:
				Tab[i][j] = pos.pop(0)
		i-=1

def isSafeDSD(Tab, i, j):
	if i-2 >= 0 and j+2 < len(Tab[i]):
		if Tab[i-1][j+1] == 2 and Tab[i-2][j+2] == 0:
			return True
	return False

#confere movimento na Diagonal Superior Direita
def DSD(Tab, i, j):
	tabAux = [row[:] for row in Tab]
	tabAux[i][j] = 0
	tabAux[i-1][j+1] = 0
	tabAux[i-2][j+2] = 1
	return tabAux

def isSafeDSE(Tab, i, j):
	if i-2 >= 0 and j-2 >= 0:
		if Tab[i-1][j-1] == 2 and Tab[i-2][j-2] == 0:
			return True
	return False

#confere movimento na Diagonal Superior Esquerda
def DSE(Tab, i, j):
	tabAux = [row[:] for row in Tab]
	tabAux[i][j] = 0
	tabAux[i-1][j-1] = 0
	tabAux[i-2][j-2] = 1
	return tabAux
		
def isSafeDIE(Tab, i, j):
	if i+2 < len(Tab) and j-2 >= 0:
		if Tab[i+1][j-1] == 2 and Tab[i+2][j-2] == 0:
			return True
	return False
			
#confere movimento na Diagonal Inferior Esquerda
def DIE(Tab, i, j):
	tabAux = [row[:] for row in Tab]
	tabAux[i][j] = 0
	tabAux[i+1][j-1] = 0
	tabAux[i+2][j-2] = 1
	return tabAux
	
def isSafeDID(Tab, i, j):
	if i+2 < len(Tab) and j+2 < len(Tab[i]):
		if Tab[i+1][j+1] == 2 and Tab[i+2][j+2] == 0:
			return True
	return False

#confere movimento na Diagonal Inferior Direita
def DID(Tab, i, j):
	tabAux = [row[:] for row in Tab]
	tabAux[i][j] = 0
	tabAux[i+1][j+1] = 0
	tabAux[i+2][j+2] = 1
	return tabAux

def PDFS(Tab, i, j, pnt):
	pntsAux = []	

	if isSafeDID(Tab, i, j):
		tabDID = DID(Tab, i, j)
		pntsAux.append(PDFS(tabDID, i+2, j+2, pnt+1))
	if isSafeDSD(Tab, i, j):
		tabDSD = DSD(Tab, i, j)
		pntsAux.append(PDFS(tabDSD, i-2, j+2, pnt+1))
	if isSafeDIE(Tab, i, j):
		tabDIE = DIE(Tab, i, j)
		pntsAux.append(PDFS(tabDIE, i+2, j-2, pnt+1))
	if isSafeDSE(Tab, i, j):
		tabDSE = DSE(Tab, i, j)
		pntsAux.append(PDFS(tabDSE, i-2, j-2, pnt+1))

	if pntsAux != []:
		pnt = max(pntsAux)
	return pnt

def TDFS(Tab):
	pnt = [0]
	for i in range(len(Tab)):
		for j in range(len(Tab[i])):
			if Tab[i][j] == 1:
				pnt.append(PDFS(Tab, i, j, 0))
	return max(pnt)

if __name__ == '__main__':

	while True:
		inp = input()
		n, m = inp.split(' ')
		n = int(n)
		m = int(m)
		if n == 0 or m == 0:
			break
		Tab = CriaTabuleiro(n, m)
		pos = input()
		pos = pos.split(' ')
		for i in range(len(pos)):	pos[i] = int(pos[i])
		DispoePeças(Tab, pos)
		print(TDFS(Tab))
		