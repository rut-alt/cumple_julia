import streamlit as st
import random
import time

st.set_page_config(
    page_title="Feliz Cumple ❤️",
    page_icon="🎂",
    layout="centered"
)

# -----------------------------
# ESTADO
# -----------------------------

if "nivel" not in st.session_state:
    st.session_state.nivel = 0

# -----------------------------
# PORTADA
# -----------------------------

if st.session_state.nivel == 0:

    st.title("🎉 Feliz Cumpleaños 🎉")

    st.markdown(
        """
# Para la mejor amiga del mundo ❤️

Hoy no quería regalarte simplemente un mensaje...

Quería regalarte un pequeño viaje por algunos de nuestros recuerdos.

¿Preparada?
"""
    )

    if st.button("✨ Empezar la aventura"):
        st.session_state.nivel = 1
        st.rerun()

# -----------------------------
# PREGUNTA 1
# -----------------------------

elif st.session_state.nivel == 1:

    st.header("Primera misión")

    st.write("¿Qué día naciste? 😏")

    respuesta = st.text_input("Escribe la fecha (dd/mm/aaaa)")

    if st.button("Comprobar"):

        if respuesta.strip() == "31/07/1999":

            st.success("¡¡Correcto!! ❤️")

            st.image("foto1.jpg", use_container_width=True)

            st.markdown("""
### Nuestro primer recuerdo

No sé si tú recuerdas este día igual que yo...

Pero para mí fue uno de esos momentos que nunca se olvidan.
""")

            if st.button("Continuar"):
                st.session_state.nivel = 2
                st.rerun()

        else:
            st.error("¡Esa no era! 😂")

# -----------------------------
# PREGUNTA 2
# -----------------------------

elif st.session_state.nivel == 2:

    st.header("Segunda misión")

    st.write("¿Cuántos años cumples hoy? 🎂")

    edad = st.number_input("", 1, 100)

    if st.button("Responder"):

        if edad == 27:

            st.success("¡Correctísimo!")

            st.image("foto2.jpg", use_container_width=True)

            st.markdown("""
### Otro recuerdo ❤️

Gracias por estar siempre.

Las risas.

Los viajes.

Las tonterías.

Y todos los momentos que aún nos quedan.
""")

            if st.button("Siguiente"):
                st.session_state.nivel = 3
                st.rerun()

        else:
            st.error("Pista... naciste en 1999 😉")

# -----------------------------
# PREGUNTA 3
# -----------------------------

elif st.session_state.nivel == 3:

    st.header("Última misión")

    st.write("Escribe una palabra:")

    palabra = st.text_input("")

    if st.button("Enviar"):

        st.balloons()

        st.image("foto3.jpg", use_container_width=True)

        st.markdown("""
# ❤️ FELICES 27 ❤️

Hoy cumples un año más...

pero lo que realmente celebramos es la suerte que tengo de tenerte.

Gracias por cada risa.

Gracias por cada aventura.

Gracias por ser tú.

Nunca cambies.

Te quiero muchísimo.

🎂❤️🥂
""")

        st.snow()
