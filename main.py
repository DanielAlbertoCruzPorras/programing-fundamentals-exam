#Exercise 3
def average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)

def volt():
    Volt = float(input("Insert the Voltage: "))
    return Volt

# Main
numbers = [volt(), volt(), volt()]

if average(numbers) >= 220:      #Enunciado no especificaba menor/mayor ó IGUAL, así que así lo dejo...
    print(f"PELIGRO")
elif average(numbers) <= 115:
    print(f"VOLTAJE CORRECTO")
else:
    print(f"ALTO VOLTAJE")