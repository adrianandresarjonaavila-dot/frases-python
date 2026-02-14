import random

frases = [
    "Nunca te rindas 💪",
    "Cada día es una nueva oportunidad 🌅",
    "El éxito es la suma de pequeños esfuerzos 🔥",
    "Confía en el proceso 🙌",
    "Todo lo que quieres está del otro lado del miedo 🚀"
]

print("Bienvenido al generador de frases ✨")
print("Presiona ENTER para obtener una frase")
print("Escribe 'salir' para terminar\n")

while True:
    opcion = input("> ")
    if opcion.lower() == "salir":
        print("Hasta luego bro 👋")
        break
    print(random.choice(frases))
