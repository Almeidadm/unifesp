param q {1..30} >= 0 ;					# numero de pessoas por ponto
param d  {1..31, 1..31} >= 0 ;			# matriz de distância

var o {1..10} binary;				# i-esimo onibus usado
var m {1..30} binary;				# i-esimo micro usado

var a {1..10, 1..30} >= 0;			# a[i, j] pessoas ponto j alocado no i-esimo onibus
var b {1..30, 1..30} >= 0;			# b[i, j] pessoas ponto j alocado no i-esimo micro

var co {1..10, 1..30} binary; 		# começo de trajeto onibus
var cm {1..30, 1..30} binary; 		# começo de trajeto micro-onibus
var x {1..10, 1..31, 1..31} binary; 	# i-esimo onibus (j, k)
var y {1..30, 1..31, 1..31} binary; 	# i-esimo micro (j, k)
var fo {1..10, 1..30} binary; 		# fim de trajeto onibus
var fm {1..30, 1..30} binary; 		# fim de trajeto micro-onibus

minimize FO:
	(15000*sum{i in 1..10}o[i]) # soma onibus usado
	+(4000*sum{i in 1..30}m[i]) # soma micro usado
	+(3.2*sum{i in 1..10, j in 1..31, k in 1..31}d[j, k]*x[i, j, k]) # soma custo de viagem onibus
	+(2.8*sum{i in 1..30, j in 1..31, k in 1..31}d[j, k]*y[i, j, k]); # soma custo de viagem micro

subject to um {i in 1..10}:
	sum{j in 1..30}a[i, j] <= 48*o[i]; # pessoas alocadas deve ser menor que 48
	
subject to dois {i in 1..30}:
	sum{j in 1..30}b[i, j] <= 16*m[i]; # pessoas alocadas deve ser menor que 16
	
subject to tres {j in 1..30}: # alocar todos do j-esio ponto
	sum{i in 1..10} a[i,j] + sum{i in 1..30} b[i,j] = q[j]; 
	
subject to quatro {i in 1..10, p in 1..30}: # evitar saltos de onibus
	sum{j in 1..30}x[i, j, p]
	- sum{j in 1..30}x[i, p, j] = 0;
	
subject to cinco {i in 1..30, p in 1..30}: # evitar saltos de micro
	sum{j in 1..30}y[i, j, p]
	- sum{j in 1..30}y[i, p, j] = 0;
	
subject to seis {i in 1..10}: #numero de onibus igual ao que sai
	sum{j in 1..30}co[i,j] <= o[i];
	
subject to sete {i in 1..30}: #numero de micro-onibus igual ao que sai
	sum{j in 1..30}cm[i,j] <= m[i];
	
subject to oito {i in 1..10}: #numero de onibus igual ao que chega
	sum{j in 1..30}fo[i,j] <= o[i];
	
subject to nove {i in 1..30}: #numero de micro-onibus igual ao que chega
	sum{j in 1..30}fm[i,j] <= m[i];
	
subject to dez {i in 1..10, p in 1..30}: #O grau de saída menos o grau de entrada do vértice deve ser igual ao valor assumid
	sum{k in 1..30} x[i, p, k] - sum{j in 1..30}x[i, j, p] = co[i,p];
	
subject to onze{i in 1..30, p in 1..30}: #O grau de saída menos o grau de entrada do vértice deve ser igual ao valor assumid
	sum{k in 1..30} y[i, p, k] - sum{j in 1..30}y[i, j, p] = cm[i,p];	

subject to doze{i in 1..10, p  in 1..30}:
	sum{j in 1..30}x[i, j, p] - sum{k in 1..30} x[i, p, k] = fo[i,p];

subject to treze{i in 1..30, p  in 1..30}:
	sum{j in 1..30}y[i, j, p] - sum{k in 1..30} y[i, p, k] = fm[i,p];
	
subject to quatorze{i in 1..10, j in 1..30}:
	a[i,j] <= 48*sum{k in 1..30} x[i, j, k];
	
subject to quinze{i in 1..30, j in 1..30}:
	b[i,j] <= 16*sum{k in 1..30} y[i, j, k]; 	
	
subject to dezeseis{i in 1..10, j in 1..30, k in 1..30}:
	x[i,j,k] + x[i, k, j] <= 1;
	
subject to dezesete{i in 1..30, j in 1..30, k in 1..30}:
	y[i,j,k] + y[i, k, j] <= 1;
	
subject to dezoito{i in 1..10, j in 1..30, k in 1..30}:	
	x[i,j,k] <= sum{p in 1..30}x[i, p, j];
	
subject to dezenove{i in 1..30, j in 1..30, k in 1..30}:	
	y[i,j,k] <= sum{p in 1..30}y[i, p, j];
	
	
	
	
	
	
	
	
	
	








	
	

	
	
	