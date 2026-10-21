# stocks dict with their names and prices
import random

theGameStocks = {
  "investorPlus" : {
    "price" : 44.9,
    "volatility" : 0.5
  },
  "reliableBank" : {
    "price" : 120,
    "volatility" : 0.1
  },
  "rocketStock" : {
    "price" : 9999,
     "volatility" : 0.9
  }
}


def updatePrices(stocks):
    for x in stocks:
        stocks[x]["price"] = (random.randint(-100,100) * stocks[x]["price"]) * stocks[x]["volatility"]
    newStockList = stocks
    return newStockList



def testRun(stocks):
    for p, obj in stocks.items():
        return
        #print(p)
        #print(stocks[p]["price"])
    #print(updatePrices(stocks))


#testRun(theGameStocks)