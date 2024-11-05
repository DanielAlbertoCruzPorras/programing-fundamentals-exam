#Exercise 4
def toKm():
    distoKm = float(input("Inserte la distancia en metros: ")) / 1000

    return distoKm

# Main
distKm = print(f"Esa distancia equivale a: {toKm():.2f} Km")