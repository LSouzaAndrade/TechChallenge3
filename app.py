import streamlit as st

st.title("Formulário de dados do estudante")

st.subheader("Sobre você:")

genero = st.radio("Com que genêro você se identifica?", options=["Masculino", "Feminino"])
atividades_extras = st.radio("Você pratica atividades extracurriculares?", options=["Não", "Sim"])
dificuldades_aprendizagem = st.radio("Você possui dificuldades de aprendizagem?", options=["Sim", "Não"])
horas_estudadas = st.slider("Quantas horas você dedica para estudo semanalmente?", min_value=0, max_value=168)
atividade_fisica = st.slider("Quantas horas você dedica para atividade física semanalmente?", min_value=0, max_value=168)
horas_de_sono = st.slider("Quantas horas de sono você dorme por noite?", min_value=0, max_value=12)
frequencia = st.slider("Qual sua taxa de presença em aulas? (%)", min_value=0, max_value=100)
notas_anteriores = st.slider("Qual sua nota no exame anteriormente aplicado?", min_value=0, max_value=100)
sessao_tutoria = st.slider("Quantas sessões de tutoria você participa mensalmente?", min_value=0, max_value=30)
nivel_motivacao = st.select_slider("Como você classificaria sua motivação para estudos?", options=["Baixa", "Média", "Alta"])

st.subheader("Sobre seu ambiente de apoio e recursos:")

acesso_internet = st.radio("Você possui acesso à internet?", options=["Não", "Sim"])
tipo_escola = st.radio("Em qual tipo de escola você estuda?", options=["Pública", "Privada"])
envolvimento_parental = st.select_slider("Seus pais lhe auxiliam nos estudos?", options=["Baixo", "Médio", "Alto"])
acesso_a_recursos = st.select_slider("Como você classificaria seu acesso a recursos?", options=["Baixo", "Médio", "Alto"])
renda_familiar = st.select_slider("Como você classificaria o nível de renda de sua família?", options=["Baixo", "Médio", "Alto"])
qualidade_professor = st.select_slider("Como você classificaria o nível de qualidade dos seus professores?", options=["Baixo", "Médio", "Alto"])
influencia_colegas = st.select_slider("Como você classificaria a influência de seus colegas a respeito de seus estudos?", options=["Negativa", "Neutra", "Positiva"])
nivel_educacao_parental = st.select_slider("Qual o grau de escolaridade dos seus pais?", options=["Ensino Médio", "Universidade", "Pós-Graduação"])
distancia_casa = st.select_slider("Como você classificaria a distância da sua casa até a escola?", options=["Próxima", "Moderada", "Distante"])

st.button("Enviar respostas")