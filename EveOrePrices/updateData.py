import json
import requests
from printLines import printOreUpdates, printMineralUpdates


def mineralPrices(options):
    allMinerals = openFile("mineralPrices.json")
    sortedMinerals = sorted(list(allMinerals.keys()))
    total = len(sortedMinerals)
    for count, mineral in enumerate(sortedMinerals, start=1):
        bar = getProgressBar(sortedMinerals, mineral)
        old_mineral = allMinerals[mineral]
        new_mineral = setNewPrice(old_mineral)
        printMineralUpdates(count, bar, total, mineral, old_mineral, new_mineral, options)

    writeFile(allMinerals, "mineralPrices.json")


def orePrices(options):
    allOres = openFile("orePrices.json")
    sortedOres = sorted(list(allOres.keys()))
    total = sum(len(allOres[ore]) for ore in sortedOres)
    count = 0
    for parent in sortedOres:
        for ore in allOres[parent]:
            bar = getProgressBar(sortedOres, parent)
            old_ore = allOres[parent][ore]
            new_ore = setNewPrice(old_ore)
            count += 1
            printOreUpdates(count, bar, total, ore, old_ore, new_ore, options)
    writeFile(allOres, "orePrices.json")


def setNewPrice(current):
    bidAskPrice = getBidAskPrice(current)
    current['bidPrice'] = round(bidAskPrice[0], 2)
    current['askPrice'] = round(bidAskPrice[1], 2)
    return current


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


def getProgressBar(sortedOres, parent):
    width = sortedOres.index(parent) + 1
    return "[" + "#" * width + " " * (len(sortedOres) - width) + "]"


def openFile(name):
    with open(name) as file:
        return json.load(file)


def writeFile(write, name):
    with open(name, 'w') as file:
        json.dump(write, file, indent=2, separators=(',', ': '))
