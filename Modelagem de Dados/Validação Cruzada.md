# Validação Cruzada

A capacidade de generalização de um modelo é um atributo importante a ser analisado em sua construção. A partir dos métodos de validação podemos estimar quão eficaz um modelo é em generalizar o seu aprendizado sob os dados.

## Treino e teste

Tradicionalmente dividimos o conjunto de dados em dois, sendo um deles utilizado para o treinamento do modelo de previsão, e o outro para teste, ou avaliação, do modelo em questão.

Podemos separar o conjunto de dados de maneira arbitrária. Podemos definir, por exemplo, que 80% dos dados serão utilizados para treinamento e os 20% restante para teste. 

Frequentemente é necessário realizar a otimização de hiperparâmetros, dessa forma, ainda podemos tomar um conjunto de validação. A imagem abaixo exemplifica o caso.



![image-20211208174752458](/home/ddeam/.config/Typora/typora-user-images/image-20211208174752458.png)

Uma vez realizada a otimização de hiperparâmetros, podemos então selecionar o modelo com os hiperparâmetros que melhores se ajustaram aos nossos dados e então treina-lo com os dados de treino e validação para, só então, avaliarmos sua capacidade preditiva nos dados de teste.

Ao separarmos os conjuntos de dados desta forma podemos encontrar diversos valores diferentes para as métricas de avaliação, uma vez que o desempenho está intimamente ligado a como o conjunto de dados foi particionado.

Dessa forma, as métricas de desempenho apresentarão resultados imprecisos sobre a real capacidade preditiva dos modelos, com grande variância nos valores de métrica obtidos em cada partição de dados diferentes.

Para resolver este problema, podemos utilizar a validação cruzada.

## Validação cruzada tradicional

