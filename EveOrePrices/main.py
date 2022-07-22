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
    if orePrices == 1:
        return

    if PRINT_LIST:
        printLines.printListedItems(orePrices, PRINT_COLOR)
        return
    printLines.printTopItems(orePrices, PRINT_COLOR)


def updatePrices(options):
    from updateData import mineralPrices, orePrices
    print("Updating Mineral Prices...")
    og_start = time.time()
    mineralPrices(options)
    print(f"\nMinerals Updated in {round(time.time() - og_start, 2)} seconds.")

    print("Updating Ore Prices...")
    start = time.time()
    orePrices(options)
    print(f"\nMinerals Updated in {round(time.time() - start, 2)} seconds.\n")

    print(f"\nUpdating Complete in {round(time.time() - og_start, 2)} seconds.")


def commandArguments():
    if sys.argv[1][0] == '-':
        options = list(sys.argv[1])[1:]
        for opt in options:
            match opt:
                case 'l':
                    OPTIONS["list"] = 1
                case 'c':
                    OPTIONS["color"] = 1
                case 'r':
                    OPTIONS["reverse"] = 1
                case 'v':
                    OPTIONS["verbose"] = 1
        sys.argv = sys.argv[1:]
    if sys.argv[1] == 'update':
        updatePrices(OPTIONS["verbose"])
        return


if __name__ == "__main__":
    main()
