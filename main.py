money = 1000
shares = 0
stock_price = 100
current_day = 1
total_days = 365

while current_day <= total_days:
    print("\n--------------------")
    print("DAG", current_day, "AV", total_days)
    print("--------------------")

    print("Pengar:", money, "kr")
    print("Antal aktier:", shares)
    print("Aktiepris:", stock_price, "kr")

    print("\nVad vill du göra?")
    print("1. Köpa aktier")
    print("2. Sälja aktier")
    print("3. Gå till nästa dag")
    print("4. Visa totalt värde")
    print("5. Avsluta spelet")

    choice = input("Välj ett alternativ: ")

    if choice == "1":
        # TODO: Lägg till köp av aktier här senare.
        print()
        print("Köp av aktier är inte implementerat än.")

    elif choice == "2":
        # TODO: Lägg till försäljning av aktier här senare.
        print()
        print("Försäljning av aktier är inte implementerad än.")

    elif choice == "3":
        # TODO: Aktiepriset kan uppdateras när marknadsdelen är klar.
        current_day = current_day + 1
        print()
        print("Du går vidare till nästa dag.")

    elif choice == "4":
        total_value = money + shares * stock_price
        print()
        print("\033[92mTotalt värde:\033[0m", total_value, "kr")
        print("\033[92mPengar på kontot:\033[0m", money, "kr")
        print("\033[92mVärdet på dina aktier:\033[0m", shares * stock_price, "kr")
        print("\033[92mTotalt värde:\033[0m", total_value, "kr")

    elif choice == "5":
        print()
        print("Du avslutar spelet.")
        break

    else:
        print("Ogiltigt val. Välj ett alternativ mellan 1 och 5.")

print("\n====================")
print("SPELET ÄR AVSLUTAT")
print("====================")

final_value = money + shares * stock_price
print("Pengar på kontot:", money, "kr")
print("Antal aktier:", shares)
print("Aktiepris:", stock_price, "kr")
print("Totalt värde:", final_value, "kr")
