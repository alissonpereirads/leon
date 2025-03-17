# Resumidor de Texto com IA 🤖📝

Bem-vindo ao meu projeto de estudo em Inteligência Artificial e LLMs (Large Language Models)! Este é um resumidor de texto que utiliza técnicas avançadas de processamento de linguagem natural (NLP) para gerar resumos claros e concisos a partir de textos extensos. Além disso, ele extrai os tópicos principais do texto, tornando a leitura mais eficiente e informativa.

Este projeto foi desenvolvido como parte do meu aprendizado em Ciência de Dados e IA, e faz parte do meu portfólio de estudos. Sou um estudante do 3º semestre de Ciência de Dados, apaixonado por IA e em busca de uma oportunidade de estágio para aplicar e expandir meus conhecimentos na prática.

## Recursos da Aplicação 🚀

- **Resumo de Texto**: Gera resumos claros e adaptados ao tom escolhido (simplificado, formal ou informal).
- **Extração de Tópicos**: Identifica e lista os principais tópicos do texto, facilitando a revisão rápida do conteúdo.
- **Interface Amigável**: Desenvolvida com Streamlit, permite que qualquer pessoa use a ferramenta de forma intuitiva.
- **Tecnologias Modernas**: Utiliza frameworks e ferramentas como LangChain, Groq (com o modelo LLaMA 3) e Pydantic para garantir robustez e eficiência.

## Ferramentas e Tecnologias Utilizadas 🛠️

Aqui estão as principais ferramentas e frameworks que utilizei neste projeto:

- **LangChain**: Framework para construção de pipelines de LLMs, permitindo a integração de modelos de linguagem com lógica personalizada.
- **Groq**: Plataforma de IA que oferece acesso a modelos avançados como o LLaMA 3, utilizado para gerar os resumos e extrair tópicos.
- **Streamlit**: Framework para criação de interfaces web simples e interativas, ideal para protótipos e projetos de estudo.
- **Pydantic**: Biblioteca para validação de dados e criação de modelos de dados estruturados, garantindo que as respostas do modelo estejam sempre no formato esperado.
- **Python**: Linguagem principal do projeto, com bibliotecas como dotenv para gerenciamento de variáveis de ambiente.

## Como Funciona? 🤔

1. **Entrada de Texto**: O usuário insere um texto longo que deseja resumir.
2. **Escolha do Tom**: O usuário seleciona o tom do resumo (simplificado, formal ou informal).
3. **Processamento**: O texto é enviado para o modelo LLaMA 3 via Groq, que gera um resumo e extrai os tópicos principais.
4. **Resultado**: O resumo e a lista de tópicos são exibidos na interface, prontos para uso.

## Como Executar o Projeto ▶️

Para rodar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/resumidor-de-texto.git
cd resumidor-de-texto
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Groq:
```
GROQ_API_KEY=sua_chave_aqui
```

4. Execute a aplicação:
```bash
streamlit run main.py
```

5. Acesse a interface:
   - Abra o navegador e acesse http://localhost:8501.

## Por Que Este Projeto? 🌟

Este projeto foi criado como parte da minha jornada de estudos em Inteligência Artificial e Ciência de Dados. Meu objetivo é explorar as capacidades dos LLMs e frameworks modernos, como LangChain e Groq, para criar soluções práticas e úteis. Além disso, busco demonstrar minha capacidade de:

- Integrar ferramentas de IA em aplicações funcionais.
- Desenvolver interfaces amigáveis para usuários finais.
- Trabalhar com pipelines de NLP e modelos de linguagem avançados.

## Sobre Mim 👋

Olá! Meu nome é [Alisson Pereira], sou estudante de Ciência de Dados no 3º semestre e um entusiasta de Inteligência Artificial. Estou em busca da minha primeira oportunidade de estágio para aplicar meus conhecimentos em projetos reais e continuar aprendendo com profissionais experientes.

Se você gostou deste projeto ou tem alguma sugestão, sinta-se à vontade para entrar em contato comigo pelo LinkedIn ou E-mail. Adoraria conversar sobre IA, Ciência de Dados e oportunidades de colaboração!

Você pode me encontrar no:

- **LinkedIn**: [Alisson Pereira](https://www.linkedin.com/in/alisson-pereira-ds/)
- **E-mail**: alissonpereira.contato@gmail.com
- **GitHub**: [alissonpereirads](https://github.com/alissonpereirads)

---

Obrigado por visitar meu repositório! Espero que este projeto demonstre meu entusiasmo e dedicação ao mundo da IA e da Ciência de Dados. Vamos construir o futuro juntos! 🚀
