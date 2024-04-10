ord_lista = ["Hej", "på", "dig", "!", "Hur", "mår", "du", "?"]

sammanlagd_sträng = ""

for ord in ord_lista:
    if ord == "dig" or ord == "du" or ord == "?":
        sammanlagd_sträng += ord
    else:
        sammanlagd_sträng += ord + " "

print(sammanlagd_sträng)
