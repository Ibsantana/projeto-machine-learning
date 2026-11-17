
import random
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)


# ==========================================
# 1. GERAÇÃO DOS DADOS
# ==========================================

# Mantém os mesmos dados em cada execução
random.seed(42)

dados = []

for i in range(100):
    horas = random.randint(1, 10)
    frequencia = random.randint(50, 100)

    # Regra artificial de aprovação
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


# ==========================================
# 2. CRIAÇÃO DO DATAFRAME
# ==========================================

df = pd.DataFrame(dados)

print("\n===== DADOS DOS ESTUDANTES =====")
print(df.head())

print("\nTotal de estudantes:", len(df))


# ==========================================
# 3. ANÁLISE EXPLORATÓRIA DOS DADOS
# ==========================================

print("\n===== INFORMAÇÕES DO DATAFRAME =====")

print("Dimensões:", df.shape)
print("Colunas:", df.columns.tolist())

df.info()

print("\nEstatísticas descritivas:")
print(df.describe())

print("\n===== ANÁLISE DOS DADOS =====")

print("Média de horas de estudo:", df["horas_estudo"].mean())
print("Média de frequência:", df["frequencia"].mean())

print("Total de estudantes:", df["aprovado"].count())
print("Aprovados:", df["aprovado"].sum())

porcentagem_aprovacao = round(
    df["aprovado"].mean() * 100, 2
)

porcentagem_reprovacao = round(
    (df["aprovado"] == 0).mean() * 100, 2
)

print("Porcentagem de aprovação:", porcentagem_aprovacao, "%")
print("Porcentagem de reprovação:", porcentagem_reprovacao, "%")


# ==========================================
# 4. SEPARAÇÃO DAS FEATURES E DO TARGET
# ==========================================

# Características utilizadas pelo modelo
X = df[["horas_estudo", "frequencia"]]

# Resultado que o modelo deverá aprender a prever
y = df["aprovado"]

print("\n===== FEATURES =====")
print(X)

print("\n===== TARGET =====")
print(y)


# ==========================================
# 5. DIVISÃO DOS DADOS
# ==========================================

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n===== TAMANHO DOS CONJUNTOS =====")

print("X treino:", X_treino.shape)
print("X teste:", X_teste.shape)
print("y treino:", y_treino.shape)
print("y teste:", y_teste.shape)


# ==========================================
# 6. CRIAÇÃO E TREINAMENTO DO MODELO
# ==========================================

modelo = DecisionTreeClassifier(random_state=42)

modelo.fit(X_treino, y_treino)


# ==========================================
# 7. PREVISÕES
# ==========================================

previsoes = modelo.predict(X_teste)

print("\n===== PREVISÕES DO MODELO =====")
print(previsoes)


# ==========================================
# 8. AVALIAÇÃO DO MODELO
# ==========================================

acuracia = accuracy_score(y_teste, previsoes)

precision = precision_score(y_teste, previsoes, zero_division=0)

recall = recall_score(y_teste, previsoes, zero_division=0)

f1 = f1_score(y_teste, previsoes, zero_division=0)

print("\n===== MÉTRICAS DE AVALIAÇÃO =====")

print("Acurácia:", round(acuracia * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall:", round(recall * 100, 2), "%")
print("F1-score:", round(f1 * 100, 2), "%")


# ==========================================
# 9. MATRIZ DE CONFUSÃO
# ==========================================

matriz = confusion_matrix(y_teste, previsoes)

print("\n===== MATRIZ DE CONFUSÃO =====")
print(matriz)


# ==========================================
# 10. PREVISÃO DE UM NOVO ESTUDANTE
# ==========================================

novo_estudante = pd.DataFrame({
    "horas_estudo": [8],
    "frequencia": [90]
})

previsao = modelo.predict(novo_estudante)

print("\n===== PREVISÃO DE NOVO ESTUDANTE =====")

if previsao[0] == 1:
    print("Resultado previsto: Aprovado")
else:
    print("Resultado previsto: Reprovado")
