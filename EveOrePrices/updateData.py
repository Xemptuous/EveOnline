import json
import requests
import sys


def mineralPrices():
    allMinerals = openFile("mineralPrices.json")
    sortedMinerals = sorted(list(allMinerals.keys()))
    total = len(sortedMinerals)
    for count, mineral in enumerate(sortedMinerals, start=1):
        bar = getProgressBar(sortedMinerals, mineral)
        setNewPrice(allMinerals[mineral])
        printMinerals(count, bar, total, mineral)

    writeFile(allMinerals, "mineralPrices.json")


def orePrices():
    allOres = openFile("orePrices.json")
    sortedOres = sorted(list(allOres.keys()))
    total = sum(len(allOres[ore]) for ore in sortedOres)
    count = 0
    for parent in sortedOres:
        for ore in allOres[parent]:
            bar = getProgressBar(sortedOres, parent)
            setNewPrice(allOres[parent][ore])
            count += 1
            printOres(count, bar, total, ore)
    writeFile(allOres, "orePrices.json")


def getBidAskPrice(current):
    try:
        types = [current['compressedID'], current['typeID']]
    except KeyError:
        types = [current['typeID']]
    bid_price = current['bidPrice']
    ask_price = current['askPrice']

    for _type in types:
        url = f'https://api.evemarketer.com/ec/marketstat/json?typeid={_type}&usesystem=30000142'
        data = requests.get(url).json()[0]
        new_bid = getNewPrice(data, "buy")
        new_ask = getNewPrice(data, "sell")
        if new_bid and new_ask:
            bid_price = new_bid
            ask_price = new_ask
            break
    return [bid_price, ask_price]


def getNewPrice(data, side):
    new_price = round(data[side]['fivePercent'], 2)
    if new_price > 0:
        return new_price
    return 0


def setNewPrice(current):
    bidAskPrice = getBidAskPrice(current)
    current['bidPrice'] = round(bidAskPrice[0], 2)
    current['askPrice'] = round(bidAskPrice[1], 2)


def getProgressBar(sortedOres, parent):
    width = sortedOres.index(parent) + 1
    return "[" + "#" * width + " " * (len(sortedOres) - width) + "]"


def printOres(count, bar, total, ore):
    print(u"\u001b[1000D" + bar + f" {count:<3}/{total}" + f" {ore:^5}", end=f"{' ' * (25 - (len(ore)))}")
    sys.stdout.flush()


def printMinerals(count, bar, total, mineral):
    print(u"\u001b[1000D" + bar + f" {count:<2}/{total}" + f" {mineral:^5}", end=f"{' ' * (20 - (len(mineral)))}")
    sys.stdout.flush()


def openFile(name):
    with open(name) as file:
        return json.load(file)


def writeFile(write, name):
    with open(name, 'w') as file:
        json.dump(write, file, indent=2, separators=(',', ': '))
