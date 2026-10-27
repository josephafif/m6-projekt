import random

from portfolio import buy_shares, sell_shares, calculate_stock_value, calculate_total_value
from save_load import save_game, load_game
from market import updatePrices, theGameStocks


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


def valj_aktie():
    """Låter spelaren välja en aktie med dess nummer och returnerar aktiens namn"""
    aktienamn = list(theGameStocks)
    nummer = fraga_om_antal("Vilken aktie (nummer)? : ")
    if nummer is None:
        return None
    if nummer < 1 or nummer > len(aktienamn):
        visa_meddelande(f"Välj ett nummer mellan 1 och {len(aktienamn)}.", TerminalFarger.ROD)
        return None
    return aktienamn[nummer - 1]


pengar = 1000
antal_aktier = {namn: 0 for namn in theGameStocks}
aktuell_dag = 1
antal_dagar = 365

while aktuell_dag <= antal_dagar:
    print("\n" + "=" * 34)
    visa_meddelande("          EKONOMISPEL", TerminalFarger.TITEL + TerminalFarger.FET)
    visa_meddelande(f"          DAG {aktuell_dag} AV {antal_dagar}", TerminalFarger.TURKOS)
    print("=" * 34)

    print(f"{TerminalFarger.GRON}Pengar på kontot:{TerminalFarger.NORMAL} {pengar} kr")
    print(f"{TerminalFarger.GUL}Aktievärde:{TerminalFarger.NORMAL} {calculate_stock_value(antal_aktier, theGameStocks)} kr")
    for nummer, namn in enumerate(theGameStocks, start=1):
        print(f"{TerminalFarger.TURKOS}{nummer}.{TerminalFarger.NORMAL} {namn} {theGameStocks[namn]['price']} kr"
              f"   {TerminalFarger.BLA}Du äger:{TerminalFarger.NORMAL} {antal_aktier[namn]} st")

    print(f"\n{TerminalFarger.FET}Vad vill du göra?{TerminalFarger.NORMAL}")
    print(f"{TerminalFarger.TURKOS}1.{TerminalFarger.NORMAL} Köpa aktier")
    print(f"{TerminalFarger.TURKOS}2.{TerminalFarger.NORMAL} Sälja aktier")
    print(f"{TerminalFarger.TURKOS}3.{TerminalFarger.NORMAL} Gå till nästa dag")
    print(f"{TerminalFarger.TURKOS}4.{TerminalFarger.NORMAL} Spara spelet")
    print(f"{TerminalFarger.TURKOS}5.{TerminalFarger.NORMAL} Ladda sparat spel")
    print(f"{TerminalFarger.TURKOS}6.{TerminalFarger.NORMAL} Avsluta spelet")

    val = input(f"{TerminalFarger.TURKOS}Välj ett alternativ: {TerminalFarger.NORMAL}")

    if val == "1":
        aktie = valj_aktie()
        antal = None
        if aktie is not None:
            antal = fraga_om_antal(f"Hur många {aktie} vill du köpa? : ")
        if antal is not None:
            pengar, antal_aktier[aktie], meddelande = buy_shares(
                pengar, antal_aktier[aktie], theGameStocks[aktie]["price"], antal
            )
            if meddelande.startswith("Du köpte"):
                visa_meddelande(meddelande, TerminalFarger.GRON)
            else:
                visa_meddelande(meddelande, TerminalFarger.ROD)

    elif val == "2":
        aktie = valj_aktie()
        antal = None
        if aktie is not None:
            antal = fraga_om_antal(f"Hur många {aktie} vill du sälja? : ")
        if antal is not None:
            pengar, antal_aktier[aktie], meddelande = sell_shares(
                pengar, antal_aktier[aktie], theGameStocks[aktie]["price"], antal
            )
            if meddelande.startswith("Du sålde"):
                visa_meddelande(meddelande, TerminalFarger.GRON)
            else:
                visa_meddelande(meddelande, TerminalFarger.ROD)

    elif val == "3":
        if aktuell_dag < antal_dagar:
            updatePrices(theGameStocks)

            for namn in theGameStocks:
                if theGameStocks[namn]["price"] < 1:
                    theGameStocks[namn]["price"] = 1

            aktuell_dag = aktuell_dag + 1
            visa_meddelande("Du går vidare till nästa dag.", TerminalFarger.TURKOS)
            
        else:
            aktuell_dag = antal_dagar + 1
            visa_meddelande("Du har nått den sista dagen.", TerminalFarger.GUL)

    elif val == "4":
        sparat = save_game(pengar, antal_aktier, aktuell_dag, antal_dagar, theGameStocks)
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
            theGameStocks.update(sparat_spel["stocks"])
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
for namn in theGameStocks:
    print(f"{TerminalFarger.BLA}{namn}: {antal_aktier[namn]} st à {theGameStocks[namn]['price']} kr{TerminalFarger.NORMAL}")
slutvarde = calculate_total_value(pengar, antal_aktier, theGameStocks)
visa_meddelande(f"Totalt värde: {slutvarde} kr", TerminalFarger.TITEL + TerminalFarger.FET)
