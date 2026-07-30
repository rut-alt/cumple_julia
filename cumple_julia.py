import streamlit as st
import time

# ---------------- CONFIG ----------------

st.set_page_config(
    page_title="❤️ Feliz Cumpleaños ❤️",
    page_icon="🎂",
    layout="centered"
)

# ---------------- ESTADO ----------------

if "pantalla" not in st.session_state:
    st.session_state.pantalla = 0

if "respuesta1_ok" not in st.session_state:
    st.session_state.respuesta1_ok = False

if "respuesta2_ok" not in st.session_state:
    st.session_state.respuesta2_ok = False

if "respuesta3_ok" not in st.session_state:
    st.session_state.respuesta3_ok = False

# ---------------- FUNCIONES ----------------

def escribir(texto, velocidad=0.03):
    lugar = st.empty()
    acumulado = ""

    for letra in texto:
        acumulado += letra
        lugar.markdown(
            f"<h3 style='text-align:center;color:#ff4b7d'>{acumulado}</h3>",
            unsafe_allow_html=True,
        )
        time.sleep(velocidad)


def corazones():
    st.markdown("""
    <div style='text-align:center;font-size:35px'>
    ❤️ 💖 💕 💗 💘 💝 💞 💓 ❤️ 💖 💕 💗 💘 💝 💞 💓 ❤️
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# PORTADA
# =====================================================

if st.session_state.pantalla == 0:

    corazones()

    st.title("🎉 FELIZ CUMPLEAÑOS 🎉")

    escribir("Hoy no quiero regalarte solo un mensaje...")

    st.write("")

    escribir("Quiero regalarte un pequeño viaje por algunos de nuestros recuerdos ❤️")

    st.progress(0)

    st.balloons()

    if st.button("✨ Empezar ✨", use_container_width=True):
        st.session_state.pantalla = 1
        st.rerun()

# =====================================================
# PANTALLA 1
# =====================================================

elif st.session_state.pantalla == 1:

    st.progress(20)

    st.header("💖 Primera misión")

    st.write("### ¿Hace cuántos años somos amigas? 🤔❤️")

    opcion = st.radio(
        "",
        (
            "Desde hace 5 años.",
            "Menos de 2 años.",
            "Desde la Primera Guerra Mundial por lo menos 😂❤️"
        )
    )

    if st.button("Responder ❤️"):

        if opcion == "Desde la Primera Guerra Mundial por lo menos 😂❤️":
            st.session_state.respuesta1_ok = True
        else:
            st.error("¿Pero cómo que eso? 😂 ¡Vuelve a intentarlo!")

    if st.session_state.respuesta1_ok:

        st.balloons()

        st.success("¡¡Correcto!! ❤️")

        st.image("foto1.jpeg", use_container_width=True)

        escribir("La verdad es que parece que llevemos siendo amigas toda la vida... ❤️")

        escribir("Y espero que todavía nos queden miles de aventuras juntas.")

        if st.button("Siguiente ➜"):

            st.session_state.pantalla = 2
            st.session_state.respuesta1_ok = False
            st.rerun()

# =====================================================
# PANTALLA 2
# =====================================================

elif st.session_state.pantalla == 2:

    st.progress(40)

    st.header("💖 Segunda misión")

    edad = st.number_input("¿Cuántos años cumples hoy?", 1, 100)

    if st.button("Responder ❤️"):

        if edad == 27:
            st.session_state.respuesta2_ok = True
        else:
            st.error("Pista... naciste en 1999 😉")

    if st.session_state.respuesta2_ok:

        st.success("¡Correcto!")

        st.balloons()

        st.image("foto2.jpeg")

        escribir("Gracias por cada risa, cada locura y cada momento juntas ❤️")

        if st.button("Continuar ➜"):

            st.session_state.pantalla = 3
            st.session_state.respuesta2_ok = False
            st.rerun()

# =====================================================
# PANTALLA 3
# =====================================================

elif st.session_state.pantalla == 3:

    st.progress(60)

    st.header("💕 Tercera misión")

    opcion = st.radio(
        "¿Qué significa nuestra amistad?",
        (
            "Solo unas fotos",
            "Una amistad cualquiera",
            "Un tesoro ❤️",
            "Nada especial"
        )
    )

    if st.button("Elegir ❤️"):

        if opcion == "Un tesoro ❤️":
            st.session_state.respuesta3_ok = True
        else:
            st.error("No te creo ni tú 😂")

    if st.session_state.respuesta3_ok:

        st.success("¡Exacto!")

        st.balloons()

        st.image("foto3.jpeg")

        escribir("Siempre consigues hacer mejores incluso los días normales ❤️")

        if st.button("Seguir ➜"):

            st.session_state.pantalla = 4
            st.session_state.respuesta3_ok = False
            st.rerun()

# =====================================================
# PANTALLA 4
# =====================================================

elif st.session_state.pantalla == 4:

    st.progress(80)

    st.header("💝 Penúltima parada")

    st.image("foto4.jpeg")

    escribir("Hay personas que pasan por tu vida...")

    escribir("Y otras que se quedan para siempre ❤️")

    if st.button("Última sorpresa 🎁"):

        st.session_state.pantalla = 5
        st.rerun()

# =====================================================
# FINAL
# =====================================================

elif st.session_state.pantalla == 5:

    st.progress(100)

    st.balloons()
    st.snow()

    corazones()

    st.image("foto5.jpeg")

    escribir("🎂 FELICES 27 AÑOS 🎂", 0.08)

    st.markdown("---")

    st.markdown(
        """
# ❤️

Hoy celebramos mucho más que un cumpleaños.

Celebramos tu sonrisa.

Celebramos tu forma de hacer feliz a la gente.

Celebramos todos los recuerdos que ya tenemos...

...y todos los que todavía nos quedan por vivir.

❤️

Espero que este pequeño regalo te saque una enorme sonrisa.

Gracias por estar siempre.

Gracias por ser tú.

Nunca cambies.

❤️ Te quiero muchísimo ❤️
"""
    )

st.markdown("""
    <div style='text-align:center;font-size:45px;line-height:1.8'>
    ❤️ 💖 💕 💗 💘 💝 💞 💓 ❤️ 💖 💕 💗 💘 💝 💞 💓 ❤️<br>
    💖 💕 ❤️ 💘 💝 💗 💞 💓 💖 💕 ❤️ 💘 💝 💗 💞 💓
    </div>
    """, unsafe_allow_html=True)
st.balloons()
corazones()

st.success("🎉 Feliz cumpleaños 🎉")
