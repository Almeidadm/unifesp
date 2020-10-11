from math import sqrt
from math import pi
from math import exp
from random import randrange
from csv import reader
import timeit

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

#dividir os dados por valores de classe
def separate_byClass(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if class_value not in separated:
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated

#calcula a media da lista de numeros
def mean(numbers):
	return sum(numbers)/float(len(numbers))

#calcula o desvio padrão dos valores
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)

#sumariza os dados
def summarize_dataset(dataset):
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries

#divide os numeros por classe e os sumariza
def summarize_byClass(dataset):
	separated = separate_byClass(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = summarize_dataset(rows)
	return summaries

#calcula a função de distribuição de probabilidade Gaussiana pra x
def calculateProbability(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2)))
	return (1/ (sqrt(2 * pi) * stdev)) * exponent


#calcula as probabilidades de predição de cada classe para uma dada linha
def calculate_ClassProbability(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, count = class_summaries[i]
			probabilities[class_value] *= calculateProbability(row[i], mean, stdev)
	return probabilities

def predict(summaries, row):
	probabilities = calculate_ClassProbability(summaries, row)
	best_label, best_prob = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = class_value
	return best_label

def naive_bayes(train, test):
	summarize = summarize_byClass(train)
	predictions = list()
	for row in test:
		output = predict(summarize, row)
		predictions.append(output)
	return predictions


if __name__ == "__main__":
	
	start  = timeit.default_timer()		
	filename = "bezdekIris.csv"
	
	dataset = load_csv(filename)
	for i in range(len(dataset[0])-1):
		strColumn_toFloat(dataset, i)

	strColumn_toInt(dataset, len(dataset[0])-1)

	n_folds = 10
	scores = evaluate_algorithm(dataset, naive_bayes, n_folds)

	print('Scores: %s' % scores)
	print('Mean Accuracy: %5.3f%%' % (sum(scores)/float(len(scores))))

	stop = timeit.default_timer()
	print('\nTime: ', stop-start)	

#	model = summarize_byClass(dataset)
#	row = [5.7,2.9,4.2,1.3]
#	label = predict(model, row)
	
#	print('\nData=%s, Predicted: %s' % (row, label))