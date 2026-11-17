# Previsão de Aprovação de Estudantes com Machine Learning

## Sobre o projeto

Este projeto utiliza conceitos de Machine Learning para desenvolver um modelo de classificação capaz de prever se um estudante será aprovado ou reprovado com base em duas variáveis:

- Horas de estudo.
- Frequência nas aulas.

O objetivo é aplicar conceitos fundamentais de Ciência de Dados e Aprendizado de Máquina, passando pelas etapas de geração e análise de dados, preparação da base, treinamento e avaliação de um modelo preditivo.

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **Pandas:** manipulação e análise dos dados.
- **Scikit-learn:** treinamento e avaliação do modelo de Machine Learning.
- **VS Code:** ambiente de desenvolvimento.
- **Git e GitHub:** versionamento e publicação do projeto.

## Como o projeto funciona

O projeto segue as seguintes etapas:

1. Geração de 100 registros de estudantes com dados sintéticos.
2. Organização dos dados em um DataFrame utilizando Pandas.
3. Análise exploratória por meio de estatísticas descritivas.
4. Separação das variáveis de entrada (*features*) e da variável-alvo (*target*).
5. Divisão dos dados em conjuntos de treinamento e teste.
6. Treinamento de um modelo de Árvore de Decisão.
7. Realização de previsões e avaliação do desempenho do modelo.

## Modelo de Machine Learning

Foi utilizado o algoritmo **Decision Tree Classifier (Árvore de Decisão)**, disponível na biblioteca Scikit-learn.

O modelo utiliza duas variáveis de entrada:

- `horas_estudo`: quantidade de horas dedicadas aos estudos.
- `frequencia`: percentual de frequência nas aulas.

A variável que o modelo busca prever é:

- `aprovado`: indica se o estudante foi aprovado (`1`) ou reprovado (`0`).

### Divisão dos dados

A base de dados foi dividida em:

- **80% para treinamento:** utilizados para ensinar o modelo.
- **20% para teste:** utilizados para avaliar as previsões.

## Métricas de avaliação

Para avaliar o desempenho do modelo, foram utilizadas as seguintes métricas:

- **Acurácia (Accuracy):** percentual de previsões corretas em relação ao total de previsões.
- **Precisão (Precision):** proporção de previsões positivas que realmente são positivas.
- **Revocação (Recall):** proporção dos casos positivos reais que foram identificados corretamente.
- **Pontuação F1 (F1-score):** combina Precision e Recall em uma única métrica.
- **Matriz de confusão:** permite visualizar os acertos e erros do modelo.

### Resultados obtidos

Resultados observados no conjunto de teste:

| Métrica | Resultado |
|---|---:|
| Acurácia (Accuracy) | 100% |
| Precisão (Precision) | 100% |
| Revocação (Recall) | 100% |
| F1-score | 100% |

## Limitações do projeto

Este projeto utiliza dados sintéticos, ou seja, dados criados artificialmente para fins de aprendizado.

A aprovação dos estudantes é definida por uma regra simulada: o estudante precisa ter pelo menos 5 horas de estudo e 75% de frequência para ser considerado aprovado.

Por esse motivo, os resultados demonstram que o modelo conseguiu aprender a regra utilizada na geração dos dados. Eles não comprovam que o modelo teria o mesmo desempenho em situações educacionais reais.

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Ibsantana/projeto-machine-learning.git
```

### 2. Acesse a pasta do projeto

```bash
cd projeto-machine-learning
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute o projeto

```bash
python main.py
```

## Estrutura do projeto

```text
projeto-machine-learning/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```

A pasta `.venv` corresponde ao ambiente virtual local e não precisa ser enviada ao GitHub.

## Status do projeto

**Concluído:** projeto desenvolvido para fins de aprendizado, com aplicação prática de conceitos de Python, análise de dados e Machine Learning.

O desenvolvimento também proporcionou prática com treinamento de modelos, classificação binária, avaliação de resultados e versionamento de código com Git e GitHub.
