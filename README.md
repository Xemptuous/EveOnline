# EveOrePrices
The EveOrePrices is a simple CLI tool to get **Refined values** and **Bid x Ask** values.

I found this much simpler than navigating to cerlestes.de and finding the market values, especially as I live in terminals. It also helps to quickly discern which ores to prioritize. Refine values are based on 100% refining.


## File Placement

for the oreprices-completion.sh file, link to `/usr/share/bash-completion/completions/`. 

oreprices.sh should link to `/bin/` to be run with ease.

also make sure to source your .bashrc or .zshrc file as such:

`source /path/to/your/oreprices-completion`


## Options
Files currently print out uncolored and ordered by original input order by default.

`-l` list - orders the items from greatest to least using _Refine Value_

`-c` color - colors output with gradient based on price. On its own, will color values based on top value, 90th%ile, and 66th%ile. When used in conjunction with `-l` in the case of `-lc or -cl`, will color items from greatest to least.

`-r` reverse - used with `list` reverses the order so that greatest value appears on the bottom.

`-v` verbose - prints out more details when used with `update`. e.g., shows old and new prices as opposed to the simple progress bar.

#### Setting options

Options can be set by using `set` and then the option. 

`set refine <refine amount>` will set the base refine-yield % that will be used when calculating refine value.

Other options can be set with `always` and `never`
e.g. `set color always` will change options to set colored by default.


### Usage

base usage is   `oreprices [OPTION]... ORES`

option usage is `oreprices set [OPTION] [VALUE]`
### Examples include:
```
oreprices arkonor
oreprices -cl bitumens zeolites titanite sperrylite
oreprices update # updates db of ore and mineral prices
```
