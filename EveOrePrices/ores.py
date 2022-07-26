import sys
import classes

def getOrePrices(allOres, allMinerals):
    finalList = []
    for arg in sys.argv[1:]:
        try:
            parent = allOres[arg]
        except KeyError:
            print(f"Invalid selection '{arg}'.\nInput must be a valid Ice, Ore, or Moon Ore.")
            return 1
        tempList = []
        for ore in list(parent.keys()):
            # initializing class for each ore in the parent category.
            Ore = classes.Ore(parent[ore])
            bonus = f"+{int(Ore.bonus * 100)}%"
            # returning list of all minerals for this ore that have values.
            mineralsList = [[key, val] for key, val in Ore.minerals.items() if val]
            refinedPrice = "{:.2f}".format(getRefinedPrice(mineralsList, Ore.volume, allMinerals))
            bidAskPrice = [Ore.bidPrice, Ore.askPrice]
            tempList.append([ore, bonus, refinedPrice, bidAskPrice])
        finalList.append(tempList)
    return finalList


def getRefinedPrice(mineralList, volume, mineralData):
    total = 0
    for mineral, amount in mineralList:
        # initializing class for current mineral.
        Mineral = classes.Mineral(mineralData[mineral])
        avg_price = (Mineral.bidPrice + Mineral.askPrice) / 2
        total += ((amount / volume) * avg_price * volume) if volume < 1 else ((amount * volume) * avg_price / volume)
    return round(total,2)
