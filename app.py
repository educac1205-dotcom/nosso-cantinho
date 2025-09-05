import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Nosso Cantinho 💖", page_icon="💘")

st.title("💘 Nosso Cantinho 💘")
st.write("Oia que fofo 💕")

menu = st.sidebar.radio(
    "Escolha uma opção:",
    ["Coração", "Carta Romântica", "Galeria de Fotos"]
)

# 1) Coração
if menu == "Coração":
    dedicatoria = st.text_input("Escreva sua mensagem:", "Edu & Emy — pra sempre 💘")

    t = np.linspace(0, 2*np.pi, 1000)
    x = 16*np.sin(t)**3
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

    fig, ax = plt.subplots()
    ax.fill(x, y, color="red", alpha=0.8)
    ax.axis("off")
    ax.text(0, -2, dedicatoria, ha="center", fontsize=14, color="black")
    st.pyplot(fig)

    st.success("💖 Feito com amor!")

# 2) Carta Romântica
elif menu == "Carta Romântica":
    nome = st.text_input("Nome da pessoa amada:", "Emy")
    autor = st.text_input("Quem escreve:", "Edu")

    if st.button("Gerar carta 💌"):
        temas = [
            "gratidão pela sua presença em cada detalhe do meu dia",
            "como você deixa meu dia mais alegre",
            "os lados que",
            "as pequenas lembranças que aquecem meu coração"
        ]
        lembrancas = [
            "nosso primeiro café juntos",
            "o passeio de mãos dadas na praia",
            "aquela risada que me faz esquecer o mundo",
            "o abraço que virou morada"
        ]
        promessas = [
            "ouvir você com o coração aberto",
            "celebrar suas conquistas, grandes e pequenas",
            "aprender, crescer e recomeçar quantas vezes for preciso",
            "ser seu porto seguro em mares calmos e revoltos"
        ]

        import random
        hoje = datetime.now().strftime("%d/%m/%Y")
        texto = f"""
{hoje}

Minha {nome},

Escrevo para agradecer {random.choice(temas)}. Penso em {random.choice(lembrancas)} 
e {random.choice(lembrancas)} e sorrio sem perceber. Ao seu lado, me sinto muito feliz
Prometo {random.choice(promessas)}. Que a nossa rota siga leve e verdadeira.

{autor},
🖊️
"""
        st.text_area("Sua carta:", texto, height=200)

elif menu == "Galeria de Fotos":
    st.header("📸 Nossa Galeria de Memórias")
    st.write("Alguns momentos especiais 💕")

    import os
    from PIL import Image

    pasta = "fotos"
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if arquivos:
        cols = st.columns(3)  
        for i, nome_arquivo in enumerate(arquivos):
            caminho = os.path.join(pasta, nome_arquivo)
            img = Image.open(caminho)
            with cols[i % 3]:
                st.image(img, use_container_width=True, caption=f"Memória {i+1}")

    else:
        st.warning("Nenhuma foto encontrada na pasta 'fotos'.")


