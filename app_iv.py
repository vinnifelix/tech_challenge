import streamlit as st

def page_home():
    st.title('Página Inicial')
    st.write('Bem-vindo à Página Inicial!')

def page_about():
    st.title('Sobre')
    st.write('Esta é a página Sobre. Aqui você pode descrever informações sobre o aplicativo.')

def page_data():
    st.title('Dados')
    st.write('Esta é a página de Dados. Aqui você pode exibir informações ou visualizações de dados.')

def page_settings():
    st.title('Configurações')
    st.write('Esta é a página de Configurações. Aqui você pode ajustar as configurações do aplicativo.')

# Configuração da barra lateral para navegação entre as páginas
st.sidebar.title('Navegação')
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
