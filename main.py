import random

frases = [
    "Nunca te rindas 💪",
    "Cada día es una nueva oportunidad 🌅",
    "El éxito es la suma de pequeños esfuerzos 🔥",
    "Confía en el proceso 🙌",
    "Todo lo que quieres está del otro lado del miedo 🚀"
]

def mostrar_menu():
    print("\n📌 MENÚ")
    print("1️⃣ Mostrar frase motivacional")
    print("2️⃣ Agregar nueva frase")
    print("3️⃣ Ver todas las frases")
    print("4️⃣ Salir")

while True:
    mostrar_menu()
    opcion = input("👉 Elige una opción: ")

    if opcion == "1":
        print("\n✨", random.choice(frases))

    elif opcion == "2":
        nueva = input("✍️ Escribe la nueva frase: ")
        frases.append(nueva)
        print("✅ Frase agregada")

    elif opcion == "3":
        print("\n📚 Frases guardadas:")
        for i, frase in enumerate(frases, 1):
            print(f"{i}. {frase}")

    elif opcion == "4":
        print("👋 Hasta luego bro")
        break

    else:
        print("❌ Opción inválida")
