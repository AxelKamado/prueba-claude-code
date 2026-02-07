"""
El Sombrero Seleccionador de Hogwarts
Un juego interactivo que determina a qué casa perteneces.
"""

import time
import random


def mostrar_lento(texto, pausa=0.03):
    """Imprime texto caracter por caracter para efecto dramático."""
    for char in texto:
        print(char, end="", flush=True)
        time.sleep(pausa)
    print()


def mostrar_banner():
    print(r"""
    _______________
   /               \
  /   ~~~~~~~~~~~   \
 |   /           \   |
 |  |  ^       ^  |  |
 |  |      ___     |  |
 |   \   '-----'  /   |
  \   '._________.'   /
   \    |       |    /
    '---'       '---'
  EL SOMBRERO SELECCIONADOR
    """)


def intro():
    mostrar_banner()
    time.sleep(0.5)
    mostrar_lento("Hmm... veamos, veamos...")
    time.sleep(0.3)
    mostrar_lento("Ah, otra mente joven que explorar.")
    time.sleep(0.3)
    mostrar_lento("Llevo mas de mil anos haciendo esto, asi que... confia en mi.")
    time.sleep(0.3)
    mostrar_lento("Responde con sinceridad. Yo veo mas alla de lo que crees.\n")
    time.sleep(0.5)


def hacer_pregunta(numero, pregunta, opciones):
    """Muestra una pregunta y recoge la respuesta del usuario."""
    print(f"--- Pregunta {numero} ---")
    mostrar_lento(pregunta)
    print()
    for letra, texto in opciones.items():
        print(f"  {letra}) {texto}")
    print()

    while True:
        respuesta = input("Tu respuesta (a/b/c/d): ").strip().lower()
        if respuesta in ("a", "b", "c", "d"):
            print()
            return respuesta
        print("Hmm... esa no es una opcion valida. Elige a, b, c o d.")


def obtener_preguntas():
    """Retorna la lista de preguntas con sus opciones y puntos por casa."""
    preguntas = [
        {
            "pregunta": "Estas caminando por un sendero y llegas a una bifurcacion. Que camino eliges?",
            "opciones": {
                "a": "El que lleva al bosque oscuro y misterioso",
                "b": "El que sube a la cima de una montana con vista al horizonte",
                "c": "El que lleva a una biblioteca antigua escondida",
                "d": "El que pasa por un jardin lleno de criaturas magicas",
            },
            "puntos": {
                "a": {"Slytherin": 2},
                "b": {"Gryffindor": 2},
                "c": {"Ravenclaw": 2},
                "d": {"Hufflepuff": 2},
            },
        },
        {
            "pregunta": "Un troll ha entrado en las mazmorras. Que haces?",
            "opciones": {
                "a": "Corres a enfrentarlo. Alguien tiene que hacerlo!",
                "b": "Buscas un hechizo en tu memoria que pueda detenerlo",
                "c": "Organizas a los demas para evacuar de forma segura",
                "d": "Encuentras la manera de usarlo a tu favor",
            },
            "puntos": {
                "a": {"Gryffindor": 2},
                "b": {"Ravenclaw": 2},
                "c": {"Hufflepuff": 2},
                "d": {"Slytherin": 2},
            },
        },
        {
            "pregunta": "Que materia de Hogwarts te emociona mas?",
            "opciones": {
                "a": "Defensa Contra las Artes Oscuras",
                "b": "Pociones",
                "c": "Encantamientos y Transformaciones",
                "d": "Herbologia y Cuidado de Criaturas Magicas",
            },
            "puntos": {
                "a": {"Gryffindor": 2},
                "b": {"Slytherin": 2},
                "c": {"Ravenclaw": 2},
                "d": {"Hufflepuff": 2},
            },
        },
        {
            "pregunta": "Encuentras un objeto magico muy poderoso. Que haces con el?",
            "opciones": {
                "a": "Lo usas para proteger a quienes amas",
                "b": "Estudias su magia para entender como funciona",
                "c": "Lo entregas al profesor mas cercano, es lo correcto",
                "d": "Lo guardas. El poder siempre puede ser util",
            },
            "puntos": {
                "a": {"Gryffindor": 2},
                "b": {"Ravenclaw": 2},
                "c": {"Hufflepuff": 2},
                "d": {"Slytherin": 2},
            },
        },
        {
            "pregunta": "Que cualidad valoras MAS en una persona?",
            "opciones": {
                "a": "La valentia y el coraje",
                "b": "La inteligencia y la creatividad",
                "c": "La lealtad y la justicia",
                "d": "La ambicion y la determinacion",
            },
            "puntos": {
                "a": {"Gryffindor": 2},
                "b": {"Ravenclaw": 2},
                "c": {"Hufflepuff": 2},
                "d": {"Slytherin": 2},
            },
        },
        {
            "pregunta": "Es medianoche y escuchas un ruido extrano en el pasillo de Hogwarts. Que haces?",
            "opciones": {
                "a": "Sales a investigar con tu varita en mano",
                "b": "Analizas el sonido y deduces que podria ser antes de actuar",
                "c": "Despiertas a tus companeros para ir juntos",
                "d": "Te escabulles en silencio para descubrir que pasa sin ser visto",
            },
            "puntos": {
                "a": {"Gryffindor": 2},
                "b": {"Ravenclaw": 2},
                "c": {"Hufflepuff": 2},
                "d": {"Slytherin": 2},
            },
        },
        {
            "pregunta": "El Espejo de Oesed muestra tu deseo mas profundo. Que ves?",
            "opciones": {
                "a": "Te ves como un heroe, reconocido por tus hazanas",
                "b": "Te ves descubriendo los secretos mas profundos de la magia",
                "c": "Te ves rodeado de amigos y familia, todos felices",
                "d": "Te ves en la cima, liderando y siendo respetado por todos",
            },
            "puntos": {
                "a": {"Gryffindor": 2},
                "b": {"Ravenclaw": 2},
                "c": {"Hufflepuff": 2},
                "d": {"Slytherin": 2},
            },
        },
    ]
    return preguntas


def calcular_casa(puntuaciones):
    """Determina la casa ganadora. En caso de empate, elige aleatoriamente."""
    max_puntos = max(puntuaciones.values())
    casas_empatadas = [
        casa for casa, pts in puntuaciones.items() if pts == max_puntos
    ]
    return random.choice(casas_empatadas)


def mostrar_resultado(casa, puntuaciones):
    """Muestra el resultado con dramatismo y la descripcion de la casa."""
    comentarios_sombrero = [
        "Mmm, dificil. Muy dificil...",
        "Veo mucho potencial aqui...",
        "Interesante, muy interesante...",
        "Ah, creo que ya se donde ponerte...",
    ]

    for comentario in comentarios_sombrero:
        mostrar_lento(comentario)
        time.sleep(0.5)

    time.sleep(1)
    print()
    print("=" * 50)
    mostrar_lento(f'  "Mejor que sea... {casa.upper()}!"', pausa=0.06)
    print("=" * 50)
    print()

    descripciones = {
        "Gryffindor": {
            "lema": "Donde habitan los valientes de corazon!",
            "descripcion": (
                "Gryffindor valora el coraje, la audacia y la caballerosidad.\n"
                "Tu sala comun esta en la torre mas alta, porque a los valientes\n"
                "les gusta estar cerca del cielo (y lejos de las mazmorras).\n"
                "Companeros notables: Harry Potter, Hermione Granger, los Weasley.\n"
                "Advertencia: tendencia a meterse en problemas 'por el bien mayor'."
            ),
            "animal": r"""
       _,___
      /  -.-\
     / .-. |=\    << El leon de Gryffindor >>
    /  '-'  |=|
   |   .--. | |
   | /    \|/
    \|     /
     '----'
            """,
        },
        "Slytherin": {
            "lema": "Donde la astucia y la ambicion te llevaran a la grandeza!",
            "descripcion": (
                "Slytherin valora la ambicion, el liderazgo y la astucia.\n"
                "Tu sala comun esta en las mazmorras, bajo el lago. Nada mas\n"
                "elegante que tener un acuario natural como ventana.\n"
                "Companeros notables: Merlin (si, ESE Merlin), Severus Snape.\n"
                "Advertencia: no todos son malvados... pero el marketing es pesimo."
            ),
            "animal": """
          _____
         /     \\
        / ^   ^ \\
       |  (o o)  |   << La serpiente de Slytherin >>
        \\  ~~~  /
         \\_____/
          |   |
          ~~~~~
            """,
        },
        "Ravenclaw": {
            "lema": "Donde los de mente aguda siempre encontraran a sus iguales!",
            "descripcion": (
                "Ravenclaw valora la inteligencia, la sabiduria y el ingenio.\n"
                "Tu sala comun esta en una torre, y para entrar debes resolver\n"
                "un acertijo. Si, incluso a las 3 AM cuando vienes del bano.\n"
                "Companeros notables: Luna Lovegood, Cho Chang, Filius Flitwick.\n"
                "Advertencia: adiccion severa a los libros y debates a medianoche."
            ),
            "animal": r"""
        ,_,
       (O,O)
       /)  )    << El aguila de Ravenclaw >>
      / / /
     / / /
    (_(_/
            """,
        },
        "Hufflepuff": {
            "lema": "Donde son justos y leales, pacientes y sin temor al trabajo!",
            "descripcion": (
                "Hufflepuff valora la lealtad, la paciencia y el juego limpio.\n"
                "Tu sala comun esta junto a las cocinas. Coincidencia? No lo creo.\n"
                "Los Hufflepuff son los mejores amigos que puedas tener.\n"
                "Companeros notables: Newt Scamander, Cedric Diggory, Tonks.\n"
                "Advertencia: capacidad sobrenatural para encontrar comida a cualquier hora."
            ),
            "animal": r"""
       __
      (_  '.
        '-. \
     _     \ \    << El tejon de Hufflepuff >>
    ( '--.   \_)
     '.__.\
            """,
        },
    }

    info = descripciones[casa]
    print(info["animal"])
    mostrar_lento(f"  {info['lema']}")
    print()
    mostrar_lento(info["descripcion"], pausa=0.02)
    print()

    print("-" * 50)
    print("  Puntuaciones finales:")
    for c in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
        barra = "#" * puntuaciones[c]
        print(f"    {c:12s} | {barra} ({puntuaciones[c]} pts)")
    print("-" * 50)


def main():
    puntuaciones = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Ravenclaw": 0,
        "Hufflepuff": 0,
    }

    intro()

    preguntas = obtener_preguntas()

    for i, p in enumerate(preguntas, 1):
        respuesta = hacer_pregunta(i, p["pregunta"], p["opciones"])
        for casa, pts in p["puntos"][respuesta].items():
            puntuaciones[casa] += pts

        # Comentarios del sombrero entre preguntas
        if i == 3:
            mostrar_lento("Hmm... ya voy formandome una idea...\n")
            time.sleep(0.3)
        elif i == 5:
            mostrar_lento("Casi lo tengo... solo un poco mas...\n")
            time.sleep(0.3)

    casa = calcular_casa(puntuaciones)
    mostrar_resultado(casa, puntuaciones)

    print()
    mostrar_lento("Que comience la magia! Bienvenido a Hogwarts.")
    print()


if __name__ == "__main__":
    main()
