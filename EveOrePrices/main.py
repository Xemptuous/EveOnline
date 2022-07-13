import json
import requests
import time
import sys
from colors import bcolors


def main():
    topColors = ['\033[38;2;143;8;8m','\033[38;2;157;67;0m','\033[38;2;151;114;0m','\033[38;2;121;158;0m',
                 '\033[38;2;0;200;0m','\033[38;2;0;255;255m']
    print_top = False
    if sys.argv[1] == 'update':
        print("Updating Mineral Prices...")
        updateMineralPrices()
        print("")
        print("Updating Complete")
        return
    if sys.argv[1] == '-t':
        print_top = True
        sys.argv = sys.argv[1:]

    with open("/home/user/Python/Projects/EveOrePrices/orePrices.json") as oreFile:
        try:
            allOres = json.load(oreFile)
        except KeyError:
            print("Invalid selection. Input must be a valid Ice, Ore, or Moon Ore.")
            return

    with open("/home/user/Python/Projects/EveOrePrices/mineralPrices.json") as mineralFile:
        allMinerals = json.load(mineralFile)

    finalList = []
    for i in sys.argv[1:]:
        tempList = []
        try:
            oreArgs = allOres[i]
        except KeyError:
            print("Invalid selection. Input must be a valid Ice, Ore, or Moon Ore.")
            return
        for ore in oreArgs:
            name = ore['ore']
            volume = ore['volume']
            yieldBonus = "+" + str(int(ore['bonus']*100)) + "%"
            minerals = list(ore.items())[6:-2]  # getting all minerals
            mineralsList = [[key, val] for key, val in minerals if val != 0]  # only minerals that have value > 0

            refinedPrice = str("{:.2f}").format(getRefinedPrice(mineralsList, volume, allMinerals))
            tempList.append([name, yieldBonus, refinedPrice])
        finalList.append(tempList)

    vals = sorted([val[-1] for item in finalList for val in item], key=float)

    if print_top:
        printTopItems(finalList,topColors,vals)
        return
    printOrderedItems(finalList,vals)


def printTopItems(finalList,topColors,vals):
    while len(finalList) != 0:
        for group in finalList:
            for item in group:
                try:
                    if len(topColors) == 0:
                        topColors.append('\033[38;2;143;8;8m')
                    if item[2] == vals[-1]:
                        print(f"{bcolors.BLUE}{item[0]:>25} | {item[1]:^5} |{topColors[-1]}{item[2]:^9}{bcolors.BLUE}|")
                        vals.pop()
                        topColors.pop()
                except IndexError:
                    return


def printOrderedItems(finalList,vals):
    top1 = max(vals, key=float)
    vals.pop()
    size = len(vals)
    top10_perc = vals[int(size * .90):]
    top50_perc = vals[int(size * .66):int(size * .90)]
    for i in finalList:
        for j in i:
            if j[2] == top1:
                print(f"{bcolors.CYAN}{j[0]:>25}{bcolors.BLUE} | {j[1]:^5} |"
                      f"{bcolors.CYAN}{j[2]:^9}{bcolors.BLUE}|"f"{bcolors.ENDC}")
            elif j[2] in top10_perc:
                print(f"{bcolors.GREEN}{j[0]:>25}{bcolors.BLUE} | {j[1]:^5} |"
                      f"{bcolors.GREEN}{j[2]:^9}{bcolors.BLUE}|{bcolors.ENDC}")
            elif j[2] in top50_perc:
                print(f"{bcolors.YELLOW}{j[0]:>25}{bcolors.BLUE} | {j[1]:^5} |"
                      f"{bcolors.YELLOW}{j[2]:^9}{bcolors.BLUE}|{bcolors.ENDC}")
            else:
                print(f"{bcolors.BLUE}{j[0]:>25} | {j[1]:^5} |{j[2]:^9}|{bcolors.ENDC}")
        print("")


def getRefinedPrice(mineralList, volume, oreData):
    total = 0
    for mineral, amount in mineralList:
        if volume < 1:
            total += ((oreData[mineral]['price'] / volume) * amount) * volume
        else:
            total += ((oreData[mineral]['price'] * volume) * amount) / volume
    return round(total,2)


def updateMineralPrices():
    start = time.time()
    with open("/home/user/Python/Projects/EveOrePrices/mineralPrices.json") as mineralFile:
        allMinerals = json.load(mineralFile)
    sortedMinerals = sorted(list(allMinerals.keys()))
    count = 0
    total = len(sortedMinerals)
    for mineral in sortedMinerals:
        idx = sortedMinerals.index(mineral)
        width = idx + 1
        bar = f"{bcolors.BLUE}[" + "#" * width + " " * (len(sortedMinerals) - width) + f"]{bcolors.ENDC}"
        type_id = allMinerals[mineral]['typeID']
        
        url = f'https://api.evemarketer.com/ec/marketstat/json?typeid={type_id}&usesystem=30000142'
        data = requests.get(url).json()[0]

        newPrice = round(data['sell']['fivePercent'],2)
        if newPrice == 0.0 or newPrice == 0:
            url = f'https://api.evemarketer.com/ec/marketstat/json?typeid={type_id}&usesystem=30000142'
            data = requests.get(url).json()[0]
            newPrice = round(data['buy']['fivePercent'],2)
        allMinerals[mineral]['price'] = newPrice
        count += 1
        if count < 10:
            print(u"\u001b[1000D" + bar + f" {count} / {total}" + f" {mineral:^5}", end=f"{' ' * (20 - (len(mineral)))}")
        else:
            print(u"\u001b[1000D" + bar + f" {count} / {total}" + f" {mineral:^5}", end=f"{' ' * (20 - (len(mineral)))}")

        sys.stdout.flush()

    with open("/home/user/Python/Projects/EveOrePrices/mineralPrices.json", 'w') as outfile:
        json.dump(allMinerals, outfile)
        end = time.time()
        time_elapsed = (end - start)
    print(f"\nFinished in {round(time_elapsed,2)} seconds")


def printANSIColors():
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[0m")
        

if __name__ == "__main__":
    main()
