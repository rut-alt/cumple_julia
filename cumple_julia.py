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

    st.write("### ¿Hace cuántos años somos amigas? ")

    opcion = st.radio(
        "",
        (
            "Desde hace 5 años.",
            "Menos de 2 años.",
            "Desde la Primera Guerra Mundial por lo menos "
        )
    )

    if st.button("Responder ❤️"):

        if opcion == "Desde la Primera Guerra Mundial por lo menos ":
            st.session_state.respuesta1_ok = True
        else:
            st.error("¿Pero cómo? ¡Vuelve a intentarlo!")

    if st.session_state.respuesta1_ok:

        st.balloons()

        st.success("¡¡Correcto!! ❤️")

        st.image("foto1.jpeg", use_container_width=True)

        st.markdown("""
        ### ❤️

        La verdad es que parece que llevemos siendo amigas toda la vida.

        Y espero que todavía nos queden miles de aventuras juntas.
        """)

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

    st.write("### ¿Cuál es la carcajada que más recuerdo contigo?")

    opcion = st.radio(
        "",
        (
            "En tu pueblo cuando tu madre nos dijo que cómo le gustaba vernos así. ",
            "Con la canción de 'tu tu ru ru tu ru ru ru' volviendo de fiesta. ",
            "Da igual cuál recuerde más... ojalá añadir mil más. "
        )
    )

    if st.button("Responder ❤️"):

        if opcion == "Da igual cuál recuerde más... ojalá añadir mil más. ❤️":
            st.session_state.respuesta2_ok = True
        else:
            st.error("Mmmmm... esa también fue muy buena")

    if st.session_state.respuesta2_ok:

        st.success("❤️ Exactamente ❤️")

        st.balloons()

        st.image("foto2.jpeg", use_container_width=True)

        st.markdown("""
        ### ❤️

        Porque lo mejor nunca fue un momento concreto.

        Lo mejor ha sido compartir todos esos momentos contigo.
        """)

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
            "Un tesoro",
            "Un regalo del universo",
            "Es mi karma positivo",
            "Todas son correctas"
        )
    )

    if st.button("Elegir ❤️"):

        if opcion == "Todas son correctas":
            st.session_state.respuesta3_ok = True
        else:
            st.error("mmmmm, algo más no?")

    if st.session_state.respuesta3_ok:

        st.success("¡Exacto!")

        st.balloons()

        st.image("foto3.jpeg")

        st.markdown("""
    ### ❤️

    Estar contigo es tan genial que creo que cada vez que compartimos un ratito rejuvenezco. .
    """)

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

    st.markdown("""
    ### ❤️

    Hay personas que pasan por tu vida...

    Y otras que se quedan para siempre. Como tú jeje.
    """)

    if st.button("Última sorpresa 🎁"):

        st.session_state.pantalla = 5
        st.rerun()

# =====================================================
# FINAL
# =====================================================

elif st.session_state.pantalla == 5:

    st.progress(100)

    st.balloons()

    st.image("foto5.jpeg", use_container_width=True)

    escribir("🎂 FELICES 27 AÑOS 🎂", 0.08)

    st.markdown("---")

    st.markdown("""
# ❤️

Hoy celebramos mucho más que un cumpleaños.

Celebramos tu sonrisa.

Celebramos tu forma de hacer feliz a todas las personas que te rodean.

Celebramos todos los recuerdos que ya tenemos...

...y todos los que todavía nos quedan por vivir. Porque hasta los 89, flipas... queda mucho jeje.

❤️

Espero que este pequeño regalo te saque una enorme sonrisa.

Gracias por estar siempre.

Gracias por ser tú y por hacer que yo sea mejor.

Nunca cambies.

❤️ Te quiero muchísimo infinito❤️
""")

    st.markdown("""
<div style='text-align:center;font-size:45px;line-height:1.8'>
❤️ 💖 💕 💗 💘 💝 💞 💓 ❤️ 💖 💕 💗 💘 💝 💞 💓 ❤️<br>
💖 💕 ❤️ 💘 💝 💗 💞 💓 💖 💕 ❤️ 💘 💝 💗 💞 💓
</div>
""", unsafe_allow_html=True)

    st.balloons()

    st.success("🎉 Feliz cumpleaños 🎉")
