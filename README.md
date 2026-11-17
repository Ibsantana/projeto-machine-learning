# Previsão de Aprovação de Estudantes com Machine Learning

## Sobre o projeto

Este projeto utiliza conceitos de **Ciência de Dados e Aprendizado de Máquina (Machine Learning)** para desenvolver um modelo de classificação capaz de prever se um estudante será aprovado ou reprovado com base em duas informações:

- Horas de estudo.
- Frequência nas aulas.

O objetivo é praticar as principais etapas de um projeto de Machine Learning, desde a criação e análise dos dados até o treinamento e a avaliação de um modelo preditivo.

## Tecnologias utilizadas

- Python
- Pandas
- Scikit-learn
- VS Code
- Git e GitHub

## Como funciona

O projeto segue as seguintes etapas:

1. São gerados 100 registros de estudantes com dados sintéticos.
2. Cada estudante recebe valores aleatórios de horas de estudo e frequência.
3. Os dados são organizados em um DataFrame utilizando Pandas.
4. São realizadas análises estatísticas para compreender os dados.
5. As variáveis são separadas em características (features) e variável-alvo (target).
6. Os dados são divididos em conjuntos de treinamento e teste.
7. Um modelo de Árvore de Decisão é treinado com os dados de treinamento.
8. O modelo realiza previsões com os dados de teste.
9. O desempenho é avaliado por meio de métricas de classificação.

## Modelo de Aprendizado de Máquina

Foi utilizado o algoritmo **Decision Tree Classifier (Árvore de Decisão)**, disponível na biblioteca Scikit-learn.

O modelo utiliza as seguintes características (features):

- `horas_estudo`
- `frequencia`

A variável-alvo (target) é:

- `aprovado`

A classificação é representada por:

- `1`: aprovado.
- `0`: reprovado.

## Regra utilizada para gerar os dados

Para criar os dados sintéticos, foi definida uma regra artificial:

- 5 ou mais horas de estudo e frequência igual ou superior a 75%: aprovado.
- Caso contrário: reprovado.

Essa regra é utilizada exclusivamente para fins didáticos.

## Análise dos dados

Com o Pandas, foram realizadas análises para compreender melhor os dados gerados, incluindo:

- Visualização dos primeiros registros.
- Verificação da quantidade de linhas e colunas.
- Identificação das colunas e dos tipos de dados.
- Cálculo de estatísticas descritivas.
- Cálculo da média de horas de estudo e frequência.
- Identificação da quantidade e da porcentagem de estudantes aprovados e reprovados.

## Divisão dos dados

Os dados foram separados em:

- **80% para treinamento:** utilizados para ensinar o modelo.
- **20% para teste:** utilizados para avaliar o desempenho do modelo.

Foi utilizado `random_state=42` para garantir a reprodução da divisão dos dados.

## Métricas de avaliação

O desempenho do modelo foi avaliado utilizando as seguintes métricas:

| Métrica | O que avalia |
|---|---|
| Acurácia (Accuracy) | Proporção total de previsões corretas. |
| Precisão (Precision) | Proporção das previsões positivas que realmente são positivas. |
| Recall | Proporção dos casos positivos reais identificados pelo modelo. |
| F1-score | Equilíbrio entre Precision e Recall. |
| Matriz de confusão | Apresenta os acertos e erros das classificações. |

## Resultados

No conjunto de teste, foram obtidos os seguintes resultados:

| Métrica | Resultado |
|---|---:|
| Acurácia (Accuracy) | 100% |
| Precisão (Precision) | 100% |
| Recall | 100% |
| F1-score | 100% |

A matriz de confusão apresentou:

```text
[[12  0]
 [ 0  8]]
```

Isso significa que o modelo classificou corretamente os 20 registros do conjunto de teste, sem apresentar falsos positivos ou falsos negativos.

Também foi realizada uma previsão com os dados de um novo estudante, utilizando 8 horas de estudo e 90% de frequência. O resultado previsto foi: **Aprovado**.

## Limitações do projeto

Este projeto utiliza dados sintéticos e uma regra artificial para definir a aprovação dos estudantes.

Por isso, os resultados demonstram a capacidade do modelo de aprender essa regra simulada, mas não comprovam sua eficácia em situações educacionais reais.

Em um cenário real, a aprovação de um estudante depende de diversos fatores que não são representados neste projeto.

## Como executar o projeto

### 1. Clonar o repositório

```bash

git clone https://github.com/Ibsantana/projeto-machine-learning.git

### 2. Entrar na pasta do projeto

```bash
cd projeto-machine-learning
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

No Windows, utilizando PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar o projeto

```bash
python main.py
```

## Estrutura do projeto

```text
projeto-machine-learning/
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Status do projeto

Projeto desenvolvido para fins de aprendizado, com aplicação prática de conceitos fundamentais de Python, análise de dados e Machine Learning.

## Autora

[Isabella Santana](https://github.com/lbsantana)
