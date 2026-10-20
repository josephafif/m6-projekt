def buy_shares(money, shares, stock_price, amount):
    """Kontrollerar att spelaren har råd och uppdaterar variablerna om köpet går igenom"""
    if amount <= 0:
        return money, shares, "Du måste köpa minst 1 aktie."

    cost = stock_price * amount

    if cost > money:
        return money, shares, "Du har inte tillräckligt med pengar för köpet."

    money = money - cost
    shares = shares + amount

    message = "Du köpte " + str(amount) + " aktie/aktier för " + str(cost) + " kr."
    return money, shares, message


def sell_shares(money, shares, stock_price, amount):
    """Säljer aktier om spelaren har tillräckligt många"""
    if amount <= 0:
        return money, shares, "Du måste sälja minst 1 aktie."

    if amount > shares:
        return money, shares, "Du äger inte så många aktier."

    income = stock_price * amount

    money = money + income
    shares = shares - amount

    message = "Du sålde " + str(amount) + " aktie/aktier för " + str(income) + " kr."
    return money, shares, message


def calculate_total_value(money, shares, stock_price):
    """Räknar ut pengar på kontot plus värdet av aktierna"""
    return money + shares * stock_price
