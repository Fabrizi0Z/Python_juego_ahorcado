import random


def obtener_palabra_secreta() -> str: # De esta forma nos aseguramos que siempre se devuelva un string
    palabras = ["argentina", "messi" "campeon", "australia", "freud", "lacan", "edimmburgo", "dublin", "barcelona", "comida", "sevilla", "libros", "guitarra", "amor"]
    return random.choice(palabras)

def mostrar_avance(palabara_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabara_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 10
    juego_terminado = False

    print("Bienvenido al juego del ahorcado")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_avance(palabra_secreta, letras_adivinadas))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce letras hasta hallar la palabra secreta: ").lower()

        if len(adivinanza) !=1 or not adivinanza.isalpha():
            print("Por favor, solo introduce letras.")
        elif adivinanza in letras_adivinadas:
            print("Ya has introducido esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(f"{adivinanza} está en la palabra")
            else:
                intentos -=1
                print(f"Lo siento, la letra {adivinanza} no se encuentra en la palabra. Te quedan {intentos} intentos")

        progreso_actual = mostrar_avance(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"Felicitaciones! {palabra_secreta} era la palabra secreta")

    if intentos == 0:
                palabra_secreta = palabra_secreta.capitalize()

                print(f"Perdiste! La palabra que estabas buscando era {palabra_secreta}")

ahorcado()