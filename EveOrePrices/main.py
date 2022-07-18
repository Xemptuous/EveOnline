import json
import time
import sys
import printLines
import ores

# TODO: add triglavian and wormhole ores to orePrices.json (and bash-completions)
PRINT_LIST = False
PRINT_COLOR = False

def main():
    commandArguments()

    with open("orePrices.json") as orefile, open("mineralPrices.json") as mineralfile:
        allOres = json.load(orefile)
        allMinerals = json.load(mineralfile)

    orePrices = ores.getOrePrices(allOres, allMinerals)

    if PRINT_LIST:
        printLines.printListedItems(orePrices, PRINT_COLOR)
        return
    printLines.printTopItems(orePrices, PRINT_COLOR)


def updatePrices():
    from updateData import mineralPrices, orePrices
    print("Updating Mineral Prices...")
    start = time.time()
    mineralPrices()
    print(f"\nMinerals Updated in {round(time.time() - start, 2)} seconds.")

    print("Updating Ore Prices...")
    start = time.time()
    orePrices()
    print(f"\nMinerals Updated in {round(time.time() - start, 2)} seconds.")

    print("Updating Complete")


def commandArguments():
    global PRINT_LIST
    global PRINT_COLOR

    if sys.argv[1] == 'update':
        updatePrices()
        return
    if sys.argv[1] == '-l':
        PRINT_LIST = True
        sys.argv = sys.argv[1:]
    if sys.argv[1] == '-c':
        PRINT_COLOR = True
        sys.argv = sys.argv[1:]
    if sys.argv[1] in ['-lc', '-cl']:
        PRINT_LIST = True
        PRINT_COLOR = True
        sys.argv = sys.argv[1:]


if __name__ == "__main__":
    main()
