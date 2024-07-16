import streamlit as st

def page_home():
    st.title('Preço do Petróleo Brent📊')
    st.write('Fomos selecionados para resolver um problema de um grande cliente:  Analisar a fundo o preço do Petróleo!')
    st.title('O que é Petróleo Brent?')
    st.write('''O Petróleo Brent é uma das principais referências globais para o preço do petróleo bruto. 
    Originário do Mar do Norte, entre o Reino Unido e a Noruega, ele é classificado como um petróleo leve e doce, devido à sua baixa densidade e baixo teor de enxofre, o que facilita seu refino em produtos como gasolina e diesel.
    Em resumo, o Petróleo Brent é uma referência essencial no mercado de energia, impactando decisões de empresas, governos e investidores em todo o mundo.''')

def page_analises():
    st.title('Analises')
    st.write('Esta é a página Sobre. Aqui você pode descrever informações sobre o aplicativo.')

def page_previsoes():
    st.title('Previsões')
    st.write('Esta é a página de Dados. Aqui você pode exibir informações ou visualizações de dados.')

def page_sobre():
    st.title('Sobre')
    st.write('Esta é a página de Configurações. Aqui você pode ajustar as configurações do aplicativo.')

# Configuração da barra lateral para navegação entre as páginas
st.sidebar.title('Menu')
page = st.sidebar.radio('Selecione uma página:',
                        ['Página Inicial', 'Sobre', 'Dados', 'Configurações'])

# Mostrar a página correspondente com base na seleção na barra lateral
if page == 'Página Inicial':
    page_home()
elif page == 'Sobre':
    page_about()
elif page == 'Dados':
    page_data()
elif page == 'Configurações':
    page_settings()
