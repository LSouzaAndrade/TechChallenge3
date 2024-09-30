import streamlit as st
import requests

st.title("Formulário de dados do estudante")

st.subheader("Sobre você:")

request = {}
request['Gender'] = st.radio("Com que genêro você se identifica?", options=["Masculino", "Feminino"])
request['Extracurricular_Activities'] = st.radio("Você pratica atividades extracurriculares?", options=["Não", "Sim"])
request['Learning_Disabilities'] = st.radio("Você possui dificuldades de aprendizagem?", options=["Não", "Sim"])
request['Hours_Studied'] = st.slider("Quantas horas você dedica para estudo semanalmente?", min_value=1, max_value=44)
request['Physical_Activity'] = st.slider("Quantas horas você dedica para atividade física semanalmente?", min_value=0, max_value=6)
request['Sleep_Hours'] = st.slider("Quantas horas de sono você dorme por noite?", min_value=4, max_value=10)
request['Attendance'] = st.slider("Qual sua taxa de presença em aulas? (%)", min_value=60, max_value=100)
request['Previous_Scores'] = st.slider("Qual sua nota no exame anteriormente aplicado?", min_value=50, max_value=100)
request['Tutoring_Sessions'] = st.slider("Quantas sessões de tutoria você participa mensalmente?", min_value=0, max_value=8)
request['Motivation_Level'] = st.select_slider("Como você classificaria sua motivação para estudos?", options=["Baixa", "Média", "Alta"])

st.subheader("Sobre seu ambiente de apoio e recursos:")

request['Internet_Access'] = st.radio("Você possui acesso à internet?", options=["Não", "Sim"])
request['School_Type'] = st.radio("Em qual tipo de escola você estuda?", options=["Pública", "Privada"])
request['Parental_Involvement'] = st.select_slider("Seus pais lhe auxiliam nos estudos?", options=["Baixo", "Médio", "Alto"])
request['Access_to_Resources'] = st.select_slider("Como você classificaria seu acesso a recursos?", options=["Baixo", "Médio", "Alto"])
request['Family_Income'] = st.select_slider("Como você classificaria o nível de renda de sua família?", options=["Baixo", "Médio", "Alto"])
request['Teacher_Quality'] = st.select_slider("Como você classificaria o nível de qualidade dos seus professores?", options=["Baixo", "Médio", "Alto"])
request['Peer_Influence'] = st.select_slider("Como você classificaria a influência de seus colegas a respeito de seus estudos?", options=["Negativa", "Neutra", "Positiva"])
request['Parental_Education_Level'] = st.select_slider("Qual o grau de escolaridade dos seus pais?", options=["Ensino Médio", "Universidade", "Pós-Graduação"])
request['Distance_from_Home'] = st.select_slider("Como você classificaria a distância da sua casa até a escola?", options=["Próxima", "Moderada", "Distante"])

if st.button("Enviar respostas"):
    assortment_dict = {'Masculino': 0, 'Feminino': 1,
                       'Não': 0, 'Sim': 1,
                       'Baixa': 1, 'Média': 2, 'Alta': 3,
                       'Pública': 0, 'Privada': 1,
                       'Baixo': 1, 'Médio': 2, 'Alto': 3,
                       'Negativa': 1, 'Neutra': 2, 'Positiva': 3,
                       'Ensino Médio': 1, 'Universidade': 2, 'Pós-Graduação': 3,
                       'Próxima': 1, 'Moderada': 2, 'Distante': 3,}
    
    for key in request.keys():
        if request[key] in assortment_dict.keys():
            request[key] = assortment_dict[request[key]]

    url = "http://127.0.0.1:8000/"
    response = requests.post(url, json=request)

    try:
        response = requests.post(url, json=request, timeout=5)
        response.raise_for_status()
        resultado = response.json()
        nota_estimada = resultado.get("prediction", "Chave não encontrada")
        st.subheader("Nota prevista:")
        st.markdown(f"<h2 style='font-size: 40px;'>{nota_estimada}</h2>",
                    unsafe_allow_html=True)
    except requests.exceptions.Timeout:
        st.error("A requisição demorou demais e excedeu o tempo limite.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao enviar dados: {e}")