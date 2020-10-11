from csv import reader
import timeit
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from statistics import mean




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

def split_label(dataset, c):
	label = list()
	for i in range(len(dataset)):
		label.append(dataset[i][c])
		dataset[i] = dataset[i][1:c]+dataset[i][c+1:]
	return dataset, label


if __name__ == '__main__':

	start = timeit.default_timer()

	filename = 'glass.data'
	dataset = load_csv(filename)
		
	print(dataset[0][-1])
	for i in range(len(dataset[0])-1):
		strColumn_toFloat(dataset, i)
		
	strColumn_toInt(dataset, -1)

	dataset, label = split_label(dataset, len(dataset[0])-1)	

	print(dataset)

	accuracy = []

	for _ in range(10):
		#dividindo dataset em treino e teste
		data_train, data_test, label_train, label_test = train_test_split(dataset, label, test_size=0.3)
	
		#criando um classificador svm
		clf = svm.SVC(kernel='linear')
	
		#treinando o modelo usando os sets de treino
		clf.fit(data_train, label_train)
	
		#predizendo para o dataset
		
		y_pred = clf.predict(data_test)
		
		accuracy.append(metrics.accuracy_score(label_test, y_pred))
		
		#print(label_pred)	

	print("\nMean Accuracy: %.4f" %mean(accuracy))

	stop = timeit.default_timer()
	print('\nTime: ', stop-start)
