import sys

def getOrePrices(allOres, allMinerals):
    finalList = []
    for arg in sys.argv[1:]:
        try:
            parent = allOres[arg]
        except KeyError:
            print("Invalid selection. Input must be a valid Ice, Ore, or Moon Ore.")
            return
        tempList = []
        for ore in list(parent.keys()):
            volume = parent[ore]["volume"]
            bonus = int(parent[ore]["bonus"] * 100)
            bonus = f"+{bonus}%"
            minerals = list(parent[ore].items())[5:-2]
            mineralsList = [[key, val] for key, val in minerals if val != 0]
            refinedPrice = "{:.2f}".format(getRefinedPrice(mineralsList, volume, allMinerals))
            bidAskPrice = [parent[ore]["bidPrice"], parent[ore]["askPrice"]]
            tempList.append([ore, bonus, refinedPrice, bidAskPrice])
        finalList.append(tempList)
    return finalList


def getRefinedPrice(mineralList, volume, mineralData):
    total = 0
    for mineral, amount in mineralList:
        avg_price = (mineralData[mineral]["bidPrice"] + mineralData[mineral]["askPrice"]) / 2
        if volume < 1:
            total += (amount / volume) * avg_price * volume
            continue
        total += (amount * volume) * avg_price / volume
    return round(total,2)
