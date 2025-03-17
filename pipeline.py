from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnablePassthrough
from config import llm
from parsers import ResumoResposta


prompt = PromptTemplate(
    template="""
    Você é um especialista em resumir textos e extrair tópicos importantes. Seu objetivo é:
    1. Criar um resumo do texto fornecido, seguindo o tom especificado: {tom}.
    2. Extrair uma lista de tópicos principais que representam as ideias mais importantes do texto.

    O resumo deve ser claro, conciso e manter as informações mais relevantes do texto original. A lista de tópicos deve conter os conceitos ou ideias-chave do texto.

    Após criar o resumo e a lista de tópicos, retorne um JSON com as seguintes chaves:
    - "resumo": o texto resumido no tom especificado.
    - "topicos": uma lista de tópicos importantes extraídos do texto.

    Texto para resumir:
    {texto}

    JSON:
    """,
    input_variables=["texto", "tom"],
)
# Definir o parser que converte a resposta JSON para um dicionário
parser = JsonOutputParser(pydantic_object=ResumoResposta)

# Construir a chain LCEL
resumo_chain = (
    {"texto": RunnablePassthrough(), "tom": RunnablePassthrough()}
    | prompt
    | llm
    | parser
)
