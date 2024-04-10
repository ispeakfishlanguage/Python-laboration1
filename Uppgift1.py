gräns = int(input("Ange ett tal: "))
summa = 0

for i in range(1, gräns + 1):
    summa += i

print(f"Summan av alla tal från 1 till {gräns} är {summa}")