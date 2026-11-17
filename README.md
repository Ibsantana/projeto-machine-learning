# Previsão de Aprovação de Estudantes com Machine Learning

## Sobre o projeto

Este projeto utiliza Machine Learning para desenvolver um modelo de classificação capaz de prever se um estudante será aprovado ou reprovado com base em duas informações:

- Horas de estudo.
- Frequência nas aulas.

O objetivo é aplicar conceitos fundamentais de Ciência de Dados e Machine Learning, desde a criação e análise dos dados até o treinamento e avaliação de um modelo preditivo.

## Tecnologias utilizadas

- Python
- Pandas
- Scikit-learn
- VS Code

## Como funciona

1. São gerados 100 registros de estudantes com dados sintéticos.
2. Os dados são organizados em um DataFrame utilizando Pandas.
3. As informações são analisadas por meio de estatísticas descritivas.
4. Os dados são separados em variáveis de entrada (features) e variável-alvo (target).
5. A base é dividida em conjuntos de treinamento e teste.
6. Um modelo de Árvore de Decisão é treinado.
7. O modelo realiza previsões e é avaliado por métricas de classificação.

## Modelo utilizado

**Decision Tree Classifier (Árvore de Decisão)**

O modelo utiliza as seguintes variáveis:

- `horas_estudo`
- `frequencia`

A variável que queremos prever é:

- `aprovado`

Os dados foram divididos em:
- 80% para treinamento.
- 20% para teste.

## Métricas de avaliação

O modelo foi avaliado utilizando:

- Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusão

Resultados obtidos no conjunto de teste:

| Métrica | Resultado |
|---|---:|
| Accuracy | 100% |
| Precision | 100% |
| Recall | 100% |
| F1-score | 100% |

## Limitações

Este projeto utiliza dados sintéticos e uma regra artificial para definir a aprovação dos estudantes: pelo menos 5 horas de estudo e 75% de frequência.

Portanto, os resultados representam a capacidade do modelo de aprender essa regra simulada e não comprovam precisão em situações educacionais reais.

## Como executar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd projeto-machine-learning
```

Crie e ative um ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

## Status do projeto

Projeto desenvolvido para fins de aprendizado e prática de conceitos de Machine Learning.