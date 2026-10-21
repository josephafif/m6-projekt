import random

from portfolio import buy_shares, sell_shares, calculate_total_value
from save_load import save_game, load_game
from market.py import updatePrices


class TerminalFarger:
    """Spelets färgvariabler för terminalen"""
    TITEL = "\033[95m"
    TURKOS = "\033[96m"
    BLA = "\033[94m"
    GRON = "\033[92m"
    GUL = "\033[93m"
    ROD = "\033[91m"
    FET = "\033[1m"
    NORMAL = "\033[0m"


def visa_meddelande(text, farg):
    """Gör så att meddelandet printas med vald färg"""
    print(f"{farg}{text}{TerminalFarger.NORMAL}")


def fraga_om_antal(text):
    """Frågar efter ett heltal och ger error om man skrivver något annat"""
    try:
        antal = int(input(f"{TerminalFarger.TURKOS}{text}{TerminalFarger.NORMAL}"))
        return antal
    except ValueError:
        visa_meddelande("Skriv ett heltal, till exempel 1 eller 5.", TerminalFarger.ROD)
        return None


pengar = 1000
antal_aktier = 0
aktiepris = 100
aktuell_dag = 1
antal_dagar = 365

while aktuell_dag <= antal_dagar:
    print("\n" + "=" * 34)
    visa_meddelande("          EKONOMISPEL", TerminalFarger.TITEL + TerminalFarger.FET)
    visa_meddelande(f"          DAG {aktuell_dag} AV {antal_dagar}", TerminalFarger.TURKOS)
    print("=" * 34)

    print(f"{TerminalFarger.GRON}Pengar på kontot:{TerminalFarger.NORMAL} {pengar} kr")
    print(f"{TerminalFarger.GUL}Aktievärde:{TerminalFarger.NORMAL} {antal_aktier * aktiepris} kr")
    print(f"{TerminalFarger.BLA}Antal aktier:{TerminalFarger.NORMAL} {antal_aktier}")
    print(f"{TerminalFarger.GUL}Aktiepris:{TerminalFarger.NORMAL} {aktiepris} kr")

    print(f"\n{TerminalFarger.FET}Vad vill du göra?{TerminalFarger.NORMAL}")
    print(f"{TerminalFarger.TURKOS}1.{TerminalFarger.NORMAL} Köpa aktier")
    print(f"{TerminalFarger.TURKOS}2.{TerminalFarger.NORMAL} Sälja aktier")
    print(f"{TerminalFarger.TURKOS}3.{TerminalFarger.NORMAL} Gå till nästa dag")
    print(f"{TerminalFarger.TURKOS}4.{TerminalFarger.NORMAL} Visa totalt värde")
    print(f"{TerminalFarger.TURKOS}5.{TerminalFarger.NORMAL} Spara spelet")
    print(f"{TerminalFarger.TURKOS}6.{TerminalFarger.NORMAL} Ladda sparat spel")
    print(f"{TerminalFarger.TURKOS}7.{TerminalFarger.NORMAL} Avsluta spelet")

    val = input(f"{TerminalFarger.TURKOS}Välj ett alternativ: {TerminalFarger.NORMAL}")

    if val == "1":
        antal = fraga_om_antal("Hur många aktier vill du köpa? : ")
        if antal is not None:
            pengar, antal_aktier, meddelande = buy_shares(
                pengar, antal_aktier, aktiepris, antal
            )
            if meddelande.startswith("Du köpte"):
                visa_meddelande(meddelande, TerminalFarger.GRON)
            else:
                visa_meddelande(meddelande, TerminalFarger.ROD)

    elif val == "2":
        antal = fraga_om_antal("Hur många aktier vill du sälja? :")
        if antal is not None:
            pengar, antal_aktier, meddelande = sell_shares(
                pengar, antal_aktier, aktiepris, antal
            )
            if meddelande.startswith("Du sålde"):
                visa_meddelande(meddelande, TerminalFarger.GRON)
            else:
                visa_meddelande(meddelande, TerminalFarger.ROD)

    elif val == "3":
        if aktuell_dag < antal_dagar:
            # TODO: Ska tas bort när market.py är färdig
            prisandring = random.randint(-10, 10)
            aktiepris = aktiepris + prisandring

            if aktiepris < 1:
                aktiepris = 1

            aktuell_dag = aktuell_dag + 1
            visa_meddelande("Du går vidare till nästa dag.", TerminalFarger.TURKOS)

            if prisandring > 0:
                farg = TerminalFarger.GRON
            elif prisandring < 0:
                farg = TerminalFarger.ROD
            else:
                farg = TerminalFarger.GUL

            visa_meddelande(f"Aktiepriset ändrades med {prisandring:+} kr.", farg)
        else:
            aktuell_dag = antal_dagar + 1
            visa_meddelande("Du har nått den sista dagen.", TerminalFarger.GUL)

    elif val == "4":
        sparat = save_game(pengar, antal_aktier, aktiepris, aktuell_dag, antal_dagar)
        if sparat:
            visa_meddelande("Spelet har sparats i filen savegame.json.", TerminalFarger.GRON)
        else:
            visa_meddelande("Spelet kunde inte sparas.", TerminalFarger.ROD)

    elif val == "5":
        sparat_spel = load_game()
        if sparat_spel is None:
            visa_meddelande("Det gick inte att hitta eller läsa ett sparat spel.", TerminalFarger.ROD)
        else:
            pengar = sparat_spel["money"]
            antal_aktier = sparat_spel["shares"]
            aktiepris = sparat_spel["stock_price"]
            aktuell_dag = sparat_spel["current_day"]
            antal_dagar = sparat_spel["total_days"]
            visa_meddelande("Det sparade spelet har laddats.", TerminalFarger.GRON)

    elif val == "6":
        visa_meddelande("Du avslutar spelet.", TerminalFarger.GUL)
        break

    else:
        visa_meddelande("Ogiltigt val. Välj ett alternativ mellan 1 och 6.", TerminalFarger.ROD)

print("\n" + "=" * 34)
visa_meddelande("          SPELET ÄR AVSLUTAT", TerminalFarger.TITEL + TerminalFarger.FET)
print("=" * 34)
print(f"{TerminalFarger.GRON}Pengar på kontot: {pengar} kr{TerminalFarger.NORMAL}")
print(f"{TerminalFarger.BLA}Antal aktier: {antal_aktier}{TerminalFarger.NORMAL}")
print(f"{TerminalFarger.GUL}Aktiepris: {aktiepris} kr{TerminalFarger.NORMAL}")
slutvarde = calculate_total_value(pengar, antal_aktier, aktiepris)
visa_meddelande(f"Totalt värde: {slutvarde} kr", TerminalFarger.TITEL + TerminalFarger.FET)
