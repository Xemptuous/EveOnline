import json
import time
import printLines
from ores import getOrePrices
from argparse import ArgumentParser

# load options at start of script
with open("options.json") as f:
    OPTIONS = json.load(f)


def main():
    # process command line arguments
    args = commandArguments()

    # open json files and read data
    with open("orePrices.json") as orefile, open("mineralPrices.json") as mineralfile:
        allOres = json.load(orefile)
        allMinerals = json.load(mineralfile)

    # get ore prices
    orePrices = getOrePrices(args, allOres, allMinerals)
    if orePrices == 1:
        return
    # print results
    printLines.printItems(orePrices, OPTIONS)


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
    quit()


def commandArguments():
    args = addParsers()
    ores = args['ores']
    sets = args['set']
    opt_list = ['list', 'color', 'reverse', 'verbose']
    opts = {key: args[key] for key in args if key in opt_list}

    # setting options for current run
    for k, v in opts.items():
        if v:
            # toggle between 1 and 0
            OPTIONS[k] ^= 1

    # setting persistent options
    if sets:
        setPersistentOptions(sets)
        quit()
    return ores


def addParsers():
    parser = ArgumentParser(description="Provides prices and relative values of various ores for determining "
                                        "the best ore to mine out of the given options.")
    parser.add_argument("-l", "--list",
                        help="Sorts items in a single list as opposed to grouping by original input order.",
                        action="store_true")
    parser.add_argument("-c", "--color",
                        help="Colors printed items according to relative value.",
                        action="store_true")
    parser.add_argument("-r", "--reverse",
                        help="Reverses the order of items printed. Most useful when used with '--list'.",
                        action="store_true")
    parser.add_argument("-v", "--verbose",
                        help="Prints out detailed information when updating prices.",
                        action="store_true")
    group = parser.add_argument_group('set options')
    group.add_argument("--set",
                       metavar=('OPTION', '{always, never}'), choices=["always", "never"], nargs=2,
                       help="Sets an option to a default behavior.",
                       action="store")
    parser.add_argument("ores", type=str, nargs="*", help="The ore(s) to fetch prices for.")
    return vars(parser.parse_args())


def setPersistentOptions(sets):
    if sets[0] == "refine":
        OPTIONS[sets[0]] = round(float(sets[1]) * .01, 4)
    else:
        OPTIONS[sets[0]] = 1 if sets[1] == "always" else 0
    with open("options.json", 'w') as wf:
        json.dump(OPTIONS, wf, indent=2, separators=(',', ': '))


if __name__ == "__main__":
    main()
