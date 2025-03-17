import streamlit as st
from pipeline import resumo_chain


st.set_page_config(page_title="Leon - Resumidor de Texto", page_icon="📝")


st.title("Leon - Resumidor de Texto")


texto = st.text_area(
    "Insira o texto que deseja resumir:",
    height=150,
    placeholder='Exemplo :"A inteligência artificial (IA) é uma área da ciência da computação que se dedica..." ',
)


tom = st.selectbox("Escolha o tom do resumo:", ["Simplificado", "Formal", "Informal"])


if st.button("Gerar Resumo"):
    if texto:
        # Executar a pipeline
        resultado = resumo_chain.invoke({"texto": texto, "tom": tom})

        # Exibir o resumo
        st.subheader("Resumo:")
        st.write(resultado["resumo"])

        # Exibir os tópicos
        st.subheader("Tópicos Importantes:")
        for topico in resultado["topicos"]:
            st.write(f"- {topico}")
    else:
        st.warning("Por favor, insira um texto para resumir.")
