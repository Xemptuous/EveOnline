import json
import time
import sys
import printLines
import ores

# TODO: add triglavian and wormhole ores to orePrices.json (and bash-completions)
with open("options.json") as optionsfile:
    OPTIONS = json.load(optionsfile)

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
                    OPTIONS["list"] ^= 1
                case 'c':
                    OPTIONS["color"] ^= 1
                case 'r':
                    OPTIONS["reverse"] ^= 1
                case 'v':
                    OPTIONS["verbose"] ^= 1
        sys.argv = sys.argv[1:]
    elif sys.argv[1] == 'update':
        updatePrices(OPTIONS["verbose"])
        quit()
    elif sys.argv[1] == 'set':
        if 'refine' in sys.argv[2]:
            OPTIONS["refine"] = round(float(sys.argv[3]) * .01, 4)
            print(f"refine % set to {OPTIONS['refine']*100} %")
        else:
            if sys.argv[3] == "always":
                OPTIONS[sys.argv[2]] = 1
            elif sys.argv[3] == "never":
                OPTIONS[sys.argv[2]] = 0
            print(f"Option '{sys.argv[2]}' set to {sys.argv[3]}")
        with open("options.json", 'w') as writefile:
            json.dump(OPTIONS, writefile, indent=2, separators=(',', ': '))
        quit()


if __name__ == "__main__":
    main()
