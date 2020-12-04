tall = input("Skriv inn et tall: ")
tall = float(tall)

if tall > 0:     #Hvis tallet er større enn 0...
    print("Tallet er positivt.")
    
elif tall == 0:  #Hvis ikke tallet er større enn null men lik 0
    print("Tallet er lik 0.")
    
else:            #Hvis tall ikke er noe av det over så....
    print("Tallet er negativt")