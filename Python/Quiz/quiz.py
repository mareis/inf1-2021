# -*- coding: utf-8 -*-
import os
import time

data = [
    {
        "sporsmol": "Hva heter årets julekalender på NRK?",
        "alternativer": [
            "Jul i svingen",
            "Jul i blåfjell",
            "Stjernestøv"
        ],
        "fasit": 2,
        "svar": -1
    },
    {
        "sporsmol": "Hvor bor julenissen?",
        "alternativer": [
            "Nordpolen",
            "Finnland",
            "Norge"
        ],
        "fasit": 0,
        "svar": -1
    }
]


def meny():
    rydd_terminal()

    linjer()
    print("")
    print("            ░██████╗░██╗░░░██╗██╗███████╗\n            ██╔═══██╗██║░░░██║██║╚════██║\n            ██║██╗██║██║░░░██║██║░░███╔═╝\n            ╚██████╔╝██║░░░██║██║██╔══╝░░\n            ░╚═██╔═╝░╚██████╔╝██║███████╗\n            ░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝\n")
    print("  1. Start quiz")
    print("  2. Om")
    print("  3. Avslutt")

    linjer()

    try:
        svar = int(input("\nSvar:\n"))
        if not 1 <= svar <= 3:
            raise ValueError()

        if svar == 1:
            return quiz()

        if svar == 2:
            return om()

        if svar == 3:
            return avslutt()

    except ValueError:
        rydd_terminal()
        print("Du skrev inn noe feil")
        time.sleep(1.5)
        meny()


def quiz():
    for d in data:
        skriv_ut_sporsmol(d)

    skriv_ut_resultat()


def skriv_ut_sporsmol(d):
    rydd_terminal()
    linjer()
    print("")
    print(f'{d["sporsmol"]}')
    for i, a in enumerate(d["alternativer"]):
        print(f'     {i +1}. {a} ')

    linjer()
    print("")

    try:
        svar = int(input("\nSvar:\n"))
        if not 1 <= svar <= 3:
            raise ValueError()

        d["svar"] = svar - 1

    except ValueError:
        print("Du skrev inn noe feil")
        time.sleep(1)
        skriv_ut_sporsmol(d)


def skriv_ut_resultat():
    poeng = 0
    for d in data:
        if d["fasit"] == d["svar"]:
            poeng += 1

    ant_sporsmol = len(data)

    rydd_terminal()
    linjer()
    print("")
    print(f"Du fik {poeng} riktig(e) av {ant_sporsmol} mulige.")

    linjer()

    svar = input("Trykk enter for å komme tilbake til menyen\n")
    if svar == "":
        return meny()

    else:
        skriv_ut_resultat()


def om():
    rydd_terminal()
    linjer()
    print("")
    print("Quiz eller kviss[1] er en form for spørrekonkurranse")
    print("der deltakerne konkurrerer om å svare riktig på flest")
    print("mulig av spørsmålene som deles ut eller stilles av en")
    print("leder, som gjerne kalles «quizmaster». Det er vanlig at")
    print("deltakerne danner lag som konkurrerer mot hverandre.\n")
    print("Quiz regnes av mange som en sosial aktivitet, og blir ")
    print("ofte brukt i ulike arrangementer for å skape")
    print("fellesskapsfølelse og glede.\n")

    print("Kopier fra Wikipedia")
    linjer()

    svar = input("Trykk enter for å komme tilbake til menyen\n")
    if svar == "":
        return meny()

    else:
        om()


def avslutt():
    rydd_terminal()
    quit()


def linjer():
    print("_"*52)
    print("-<>-"*13)


def rydd_terminal():
    """Dytter innholde i terminalen opp slik at det
    oppleves som terminalen tømmes.
     """

    # windows
    if os.name == 'nt':
        return os.system('cls')

   # andre operativsystem
    else:
        return os.system('clear')


meny()
