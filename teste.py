import streamlit as st

# Fundo preto + texto branco
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
     /* Botões */
    .stLinkButton a {
        background-color: #262730;
        color: white !important;
        text-decoration: none;
    }

    .stLinkButton a:hover {
        background-color: #ff4b4b;
        color: white !important;
    }

    h1, h2, h3, p, div {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Empresas Parceiras")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("Cacau show.jpg", use_container_width=True)
    st.title("Cacau show")
    st.link_button("Acessar", "https://www.cacaushow.com.br/?https://www.cacaushow.com.br/&gclsrc=aw.ds&gad_source=1&gad_campaignid=11648467378&gbraid=0AAAAADtOyQxucXJ_APHhX0CTANKZgUR1c&gclid=CjwKCAjw4dDTBhAqEiwAkHYmSrHvFSi656Irb-14X94RuZaDRcw26M859aPWhnTUJMVjRJBVWJbi5hoCf1UQAvD_BwE")
    st.write("A **Cacau Show** é uma das maiores redes de chocolates do Brasil, conhecida pela qualidade e variedade de seus produtos. Oferece chocolates para todas as ocasiões, unindo sabor e inovação.
")

with col2:
    st.image("Milka.png", use_container_width=True)
    st.title("Milka")
    st.link_button("Acessar", "https://www.milka.com/de/")
    st.write("A **Milka** é uma marca de chocolates famosa por seu sabor suave e cremoso. Reconhecida mundialmente, oferece uma grande variedade de chocolates e doces.
")

with col3:
    st.image("Rafaello.avif", use_container_width=True)
    st.title("Rafaello")
    st.link_button("Acessar", "https://www.raffaello.com/br/pt/")
    st.write("A **Raffaello** é uma marca de bombons da Ferrero, conhecida pela combinação de coco, amêndoa e creme. É muito apreciada pelo sabor delicado e pela apresentação elegante.
")
