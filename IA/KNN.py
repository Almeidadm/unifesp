# k-nearest neighbors on the Iris Flowers Dataset
from random import seed
from random import randrange
from csv import reader
from math import sqrt
import timeit
from sklearn.metrics import confusion_matrix

#importar dados formato csv/data
def load_csv(filename):
	file = open(filename, "r")
	lines = reader(file)
	dataset = list(lines)
	return dataset[:-1]

#transformar colunas de string para Float
def strColumn_toFloat(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

#transformar colunas de string para Int
def strColumn_toInt(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
		print('[%s] => %d' % (value, i))
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup

#normalizar os dados para que não haja valores discrepantes
def normalizeDataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0])/(minmax[i][1] - minmax[i][1])

#avalia a corretude do algoritmo
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

#Divide o dataset em k partes
def crossValidationSplit(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset)/n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

#Avalia o algoritmo usando a cross validation split
def evaluate_algorithm(dataset, algorithm, n_fold, *args):
	folds = crossValidationSplit(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

# ------------Algoritmo---------------------#

#calcula a distancia euclidiana
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

#tomas os k vizinhos mais proximos
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

#Faz uma predição a partir dos k vizinhos
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
 
#KNN
def k_nearest_neighbors(train, test, num_neighbors):
	predictions = list()
	for row in test:
		output = predict_classification(train, row, num_neighbors)
		predictions.append(output)
	return(predictions)

if __name__ == "__main__":
	start  = timeit.default_timer()		
	seed(1)
	filename = 'bezdekIris.csv'

	dataset = load_csv(filename)
	for i in range(len(dataset[0])-1):
		strColumn_toFloat(dataset, i)

	strColumn_toInt(dataset, len(dataset[0])-1)

	n_folds = 10
	num_neighbors = 1
	scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)
	print('Scores: %s' % scores)
	print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

	stop = timeit.default_timer()
	print('\nTime: ', stop-start)	




#Algoritmo encontrado em
#https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
