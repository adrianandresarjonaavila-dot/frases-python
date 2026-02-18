import random
import time

def get_price():
    return round(random.uniform(90, 110), 2)

print("Trading bot iniciado correctamente 🚀")

while True:
    price = get_price()
    print(f"Precio actual: ${price}")
    time.sleep(2)