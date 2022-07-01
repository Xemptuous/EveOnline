# EveOnline
a collection of different Eve Online tools.

## EveOrePrices
The EveOrePrices is a simple CLI tool that I use to get relative values of ores to determine which is the best to mine.

I found this much simpler than navigating to cerlestes.de and finding the market values. 

The script used to use mineral prices, but comparing compressed vs batch compressed vs raw, when not all prices were available on the market was proving tedious, so instead I changed it to what I actually needed: relative isk/m3 of the ores based on refine amount. This way, I simply type the ores I want, and it feeds me the mineral prices (which are easy to update through the API), and color codes them based on percentile placement.

Examples include:
```
oreprices arkonor
oreprices bitumens zeolites titanite sperrylite
oreprices update
```
## Unpro
The **Unpro** tools is for my corporation, whereby I use selenium to access current moon data (no API access to alliance leader character information). It returns moon/station location, time since last pop, whether it is a jackpot or not, and percentage mined of each ore (with progress bars). A simple tool, but more efficient than launching the browser and navigating to the site itself.
