import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score

random.seed(42)

dados = []

for i in range(100):
    horas = random.randint(1, 10)
    frequencia = random.randint(50, 100)

    if horas >= 5 and frequencia >= 75:
        aprovado = 1
    else:
        aprovado = 0

    estudante = {
        "horas_estudo": horas,
        "frequencia": frequencia,
        "aprovado": aprovado
    }

    dados.append(estudante)

df = pd.DataFrame(dados)

print(df)

print(df.head())

print("Total de estudantes:", len(df))

print(df.shape)

print(df.columns)

df.info()

print(df.describe())

print("Média de horas:", df["horas_estudo"].mean())

print("Média de frequência:", df["frequencia"].mean())

print("Total de estudantes:", df["aprovado"].count())

print("Aprovados:", df["aprovado"].sum())


porcentagem = round(df["aprovado"].mean() * 100, 2)

print("Porcentagem de aprovação:", porcentagem, "%")

porcentagem_reprovacao = (df["aprovado"] == 0).mean() * 100

print("Porcentagem de reprovação:", porcentagem_reprovacao, "%")

# Separando as características (Features)
X = df[["horas_estudo", "frequencia"]]

# Separando o resultado que queremos prever (Target)
y = df["aprovado"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Criando o modelo
modelo = DecisionTreeClassifier(random_state=42)

# Treinando o modelo
modelo.fit(X_treino, y_treino)

# Fazendo previsões com os dados de teste
previsoes = modelo.predict(X_teste)

# Criando a matriz de confusão
matriz = confusion_matrix(y_teste, previsoes)

print("Matriz de confusão:")
print(matriz)

print("Previsões do modelo:")
print(previsoes)

# Avaliando o modelo
precisao = accuracy_score(y_teste, previsoes)

print("Precisão do modelo:", precisao * 100, "%")

# Calculando Precision
precision = precision_score(y_teste, previsoes)

print("Precision:", precision * 100, "%")

# Calculando Recall
recall = recall_score(y_teste, previsoes)

print("Recall:", recall * 100, "%")

# Calculando F1-score
f1 = f1_score(y_teste, previsoes)

print("F1-score:", f1 * 100, "%")

# Criando um novo estudante
novo_estudante = pd.DataFrame({
    "horas_estudo": [8],
    "frequencia": [90]
})

# Fazendo a previsão
previsao = modelo.predict(novo_estudante)

print("Previsão:", previsao)

# Verificando o tamanho de cada conjunto
print("X treino:", X_treino.shape)
print("X teste:", X_teste.shape)
print("y treino:", y_treino.shape)
print("y teste:", y_teste.shape)


print("Features:")
print(X)

print("Target:")
print(y)