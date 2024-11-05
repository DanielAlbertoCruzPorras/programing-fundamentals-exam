#Exercise 1
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def volt():
    Volt = float(input("Insert the Voltage: "))
    return Volt

# Main
numbers = [volt(), volt(), volt(), volt(), volt()]

if average(numbers) > 220:
    print(f"ALTO VOLTAJE")
else:
    print(f"VOLTAJE CORRECTO")

