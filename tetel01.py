db = 0
vege = 0
min = 2147483648
while (szam := int(input("szam: "))) != vege:
    if szam < min:
        min = szam
    db += 1
print(f"{db} db számból a legkisebb: {min}")