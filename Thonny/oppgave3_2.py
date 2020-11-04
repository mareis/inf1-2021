alder = int(input("Skriv inn alderen din: "))

if alder < 0:
    print("Du er ikke født enda!")
    
elif alder < 16:
    print("Du er i en alder der du skal være fri for bykymringer og ha det gøy")
    
elif alder < 18:
    print("Stressende alder der du strever med å passe inn. Du kan kjøre moped/scooter")
    
elif alder < 20:
    print(