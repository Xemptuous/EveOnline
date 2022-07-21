# EveOrePrices
The EveOrePrices is a simple CLI tool to get **Refined values** and **Bid x Ask** values.

I found this much simpler than navigating to cerlestes.de and finding the market values, especially as I live in terminals. It also helps to quickly discern which ores to prioritize. Refine values are based on 100% refining.


## File Placement

for the oreprices-completion.sh file, link to `/usr/share/bash-completion/completions/`. 

oreprices.sh should link to `/bin/` to be run with ease.

also make sure to source your .bashrc or .zshrc file as such:

`source /path/to/your/oreprices-completion`


## Options
Files currently print out uncolored and ordered by original input order.

`-l` list - orders the items from greatest to least using _Refine Value_

`-c` color - colors output with gradient based on price. On its own, will color values based on top value, 90th%ile, and 66th%ile. When used in conjunction with `-l` in the case of `-lc or -cl`, will color items from greatest to least.


### Examples include:
```
oreprices arkonor
oreprices -cl bitumens zeolites titanite sperrylite
oreprices update # updates db of ore and mineral prices
```
