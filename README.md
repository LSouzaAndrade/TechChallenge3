# Tech Challenge - Fase 3 - Grupo 12 - MLET

# App: [tc3.deployapp.online](https://tc3.deployapp.online/)

## 🚀 Sobre o projeto 

### Objetivos da Fase 3
- **Coleta de Dados**: O dataset utilizado neste projeto pode ser encontrado na seguinte [publicação na plataforma Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors);

- **Definição do Problema**: Neste dataset estão contidos os dados de alunos, de seus ambientes de estudo e de seus respectivos desempenhos em um exame. (Os dados deste dataset foram gerados sinteticamente para fins de análise exploratória de dados, conforme informado pelo autor na [publicação anteriormente mencionada](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)). A partir desses dados, o modelo neste projeto produzido visa decompor quais são as contribuições dos hábitos de rotina e do ambiente de convívio no desempenho acadêmico de alunos;

- **Análise Exploratória de Dados**: A análise exploratória dos dados do dataset podem ser encontradas no arquivo [notebook.ipynb](notebook.ipynb), a explicação dos dados abordados nesta EDA pode ser acessada no seguinte [link para o vídeo](xpto.com); 

- **Modelo Produtivo**: O modelo pode ser consumido através da aplicação de forma local através das instruções apresentadas abaixo, ou online por meio do link presente no início desta documentação.

## 📝 Arquitetura do Projeto

A estrutura de pastas e arquivos do projeto se encontra disposta da seguinte maneira:

```bash
├── Datasets                            # Diretório de datasets e derivados
    ├── StudentPerformanceFactors.csv   # Conjunto de dados exportado do Kaggle
    └── StudentPerformanceFactors.db    # Conjunto de dados salvo em arquivo SQLite
├── Models                              # Diretório de modelos e derivados
    ├── model_svr.pkl                   # Modelo SVR serializado
    └── scaler.db                       # MinMaxScaler serializado
├── app.py                              # Aplicação Streamlit
├── LICENSE.txt                         # Licença MIT vigente sob este repositório
├── model_api.py                        # API para requests ao modelo treinado
├── notebook.ipynb                      # Notebook de EDA
├── README.md                           # Documentação do projeto
└── requirements.txt                    # Dependências externas utilizadas
```

## 📋 Pré-requisitos
Para execução do aplicativo e utilização do modelo gerado neste projeto, se fazem necessárias as seguintes dependências:
- FastAPI;
- Joblib;
- Pandas;
- Scikit-learn;
- Streamlit;
- Uvicorn.

## 🔧 Instalação
Todas dependências necessárias para reprodução do projeto contido neste repositório foram testadas com a versão 3.12.5 do Python. \
É recomendado que sejam utilizadas as versões de dependências incluídas no arquivo [requirements.txt](requirements.txt), a fim de evitar erros originados por incompatibilidade de versões.\
Para isso, navegue até o diretório do projeto, e no terminal execute a seguinte sequência de comandos:

```bash
# Crie um ambiente virtual para instalar as dependências:
python3 -m venv .venv

# Para ativar o ambiente virtual, caso esteja usando Linux ou macOS, execute:
source .venv/bin/activate

# Para ativar o ambiente virtual, caso esteja usando Windows, execute:
.venv\Scripts\activate

# Instale as dependências do projeto:
pip install -r requirements.txt

```
## ⚙️ Execução
Com o ambiente virtual ativo, e dependências necessárias instaladas, é necessario que sejam abertos em terminais distintos os servidores para a API do modelo, e para a aplicação.

### Terminal 1 - API do modelo
```bash
# Inicie o servidor Uvicorn para execução do FastAPI:
uvicorn model_api:app
```
### Terminal 2 - Aplicação de consumo do modelo
```bash
# Inicie o servidor Streamlit para execução da aplicação:
streamlit run app.py
```
Após ambos servidores estarem em execução simultaneamente, é possível realizar requisições para API do modelo por meio da aplicação. \
No caso do modelo desenvolvido neste projeto, a aplicação é um formulário de dados estudantis para predição do desempenho esperado do aluno em um exame hipotético.

## ✒️ Autores

Isabelli Andrade de Souza - https://github.com/Isabellitankian
<br>
Lucas Souza Andrade dos Santos - https://github.com/LSouzaAndrade
<br>
Michel de Lima Maia - https://github.com/Michel-Maia
<br>
Valquiria Rodrigues de Oliveira Pires - https://github.com/KyraPires
