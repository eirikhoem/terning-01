import random  # Importerer random-modulen for å generere tilfeldige tall

def kast_terning():  # Definerer en funksjon for å simulere ett terningkast
    return random.randint(1, 6)  # Returnerer et tilfeldig tall mellom 1 og 6

try:  # Starter en try-except blokk for å håndtere brukerens input
    antall_kast = int(input("Skriv inn antall terningkast: "))  # Spør brukeren om antall terningkast og konverterer svaret til et heltall
except ValueError:  # Håndterer hvis brukeren skriver inn noe annet enn et heltall
    print("Vennligst skriv inn et gyldig heltall for antall terningkast.")  # Skriver ut en feilmelding
    exit()  # Avslutter programmet

if antall_kast <= 0:  # Sjekker om antallet terningkast er mindre enn eller lik null
    print("Antall terningkast må være større enn null.")  # Skriver ut en feilmelding
    exit()  # Avslutter programmet

print(f"\nSimulerer {antall_kast} terningkast:")  # Skriver ut en melding som angir hvor mange terningkast som skal simuleres
for kast in range(1, antall_kast + 1):  # Starter en løkke som går gjennom hvert terningkast
    resultat = kast_terning()  # Simulerer ett terningkast og lagrer resultatet
    print(f"Kast {kast}: {resultat}")  # Skriver ut resultatet av hvert terningkast sammen med nummeret på terningkastet
