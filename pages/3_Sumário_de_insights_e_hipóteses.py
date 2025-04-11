import streamlit as st 

st.header("🧠 Sumário de insights e hipóteses")
st.image("image/orange.jpg", use_container_width=True)

st.markdown("""
Este projeto visa desenvolver uma aplicação que utilize um conjunto de características das laranjas — como **acidez**, **tempo de colheita**, **maturidade**, **doçura**, entre outras — para fornecer uma **classificação precisa**.

📌 **Objetivo da análise**  
Melhorar os processos de produção e logística das laranjas. Por exemplo, com a classificação, é possível:
- Determinar o melhor aproveitamento para cada fruta;
- Estimar o **tempo ideal para colheita**.

🔎 **Padrões identificados para investigação futura**  
Durante esta análise exploratória, foram elencados alguns possíveis padrões que merecem investigação mais aprofundada em etapas seguintes.

⚠️ **Dificuldades encontradas e desafios futuros**
- Algumas variáveis apresentam categorias com **baixa frequência**, dificultando a obtenção de informações confiáveis.
- **Causas das manchas** ou **variedades de laranjas** específicas poderiam render boas análises, mas a distribuição dos dados representa uma limitação.
  
💡 **Reflexão**
Talvez seja interessante **definir um objetivo mais específico** para o projeto.  
Por exemplo: focar na **qualidade da fruta** como variável-alvo ou investigar **o impacto do tempo de colheita** na doçura.

""")