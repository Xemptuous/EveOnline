from colors import TOP_COLORS, bcolors


def printListedItems(finalList, print_color):
    newList = [items for groups in finalList for items in groups]
    newList = sorted(newList, key=lambda x: float(x[2]), reverse=True)
    print(f"{'Ore':>25} | {'Bonus':^5} | {'Refined':^11}| Bid x Ask\n")
    if print_color:
        for item in newList:
            bidAsk = f"{item[3][0]} x {item[3][1]}"
            if len(TOP_COLORS):
                print(f"{TOP_COLORS[-1]}{item[0]:>25} | {item[1]:^5} | {float(item[2]):^10,.2f} | {bidAsk}")
                TOP_COLORS.pop()
                continue
            print(f"\033[38;2;143;8;8m{item[0]:>25} | {item[1]:^5} | {float(item[2]):^10,.2f} | {bidAsk}")
    else:
        for item in newList:
            bidAsk = f"{item[3][0]} x {item[3][1]}"
            print(f"{item[0]:>25} | {item[1]:^5} | {float(item[2]):^10,.2f} | {bidAsk}")


def printTopItems(finalList, print_color):
    print(f"{'Ore':>25} | {'Bonus':^5} | {'Refined':^11}| Bid x Ask\n")
    if print_color:
        vals = sorted([val[2] for item in finalList for val in item], key=float)
        top = vals[-1]
        vals.pop()
        size = len(vals)
        top10_perc = vals[int(size * .90):]
        top50_perc = vals[int(size * .66):int(size * .90)]
        for group in finalList:
            for ore in group:
                printColoredTopPrices(ore, top, top10_perc, top50_perc)
            print("")
    else:
        for group in finalList:
            for ore in group:
                fprice = "{:,.2f}".format(float(ore[2]))
                bidAsk = f"{ore[3][0]} x {ore[3][1]}"
                print(f"{ore[0]:>25} | {ore[1]:^5} | {fprice:^10} | {bidAsk}")
            print("")


def printColoredTopPrices(ore, top, top10_perc, top50_perc):
    price = ore[2]
    bidAsk = f"{ore[3][0]} x {ore[3][1]}"
    if price in top50_perc:
        print(f"{TOP_COLORS[-3]}{ore[0]:>25} | {ore[1]:^5} | {float(price):^10,.2f} | {bidAsk}{bcolors.ENDC}")
    elif price in top10_perc:
        print(f"{TOP_COLORS[-2]}{ore[0]:>25} | {ore[1]:^5} | {float(price):^10,.2f} | {bidAsk}{bcolors.ENDC}")
    elif price == top:
        print(f"{TOP_COLORS[-1]}{ore[0]:>25} | {ore[1]:^5} | {float(price):^10,.2f} | {bidAsk}{bcolors.ENDC}")
    else:
        print(f"{TOP_COLORS[-6]}{ore[0]:>25} | {ore[1]:^5} | {float(price):^10,.2f} | {bidAsk}")
