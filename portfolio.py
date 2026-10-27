def buy_shares(money, shares, stock_price, amount):
    """Kontrollerar att spelaren har råd och uppdaterar variablerna om köpet går igenom"""
    if amount <= 0:
        return money, shares, "Du måste köpa minst 1 aktie."

    cost = round(stock_price * amount, 2)

    if cost > money:
        return money, shares, "Du har inte tillräckligt med pengar för köpet."

    money = round(money - cost, 2)
    shares = shares + amount

    message = "Du köpte " + str(amount) + " aktie/aktier för " + str(cost) + " kr."
    return money, shares, message


def sell_shares(money, shares, stock_price, amount):
    """Säljer aktier om spelaren har tillräckligt många"""
    if amount <= 0:
        return money, shares, "Du måste sälja minst 1 aktie."

    if amount > shares:
        return money, shares, "Du äger inte så många aktier."

    income = round(stock_price * amount, 2)

    money = round(money + income, 2)
    shares = shares - amount

    message = "Du sålde " + str(amount) + " aktie/aktier för " + str(income) + " kr."
    return money, shares, message


def calculate_stock_value(shares, stocks):
    """Räknar ut värdet av alla aktier spelaren äger"""
    value = 0
    for name in shares:
        value = value + shares[name] * stocks[name]["price"]
    return round(value, 2)


def calculate_total_value(money, shares, stocks):
    """Räknar ut pengar på kontot plus värdet av aktierna"""
    return round(money + calculate_stock_value(shares, stocks), 2)
