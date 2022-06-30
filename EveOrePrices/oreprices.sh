#!/bin/zsh

while [ $# -gt 0 ]; do
	for input in "$@" ; do
		case $input in
			shortlist)
				echo arkonor bistot crokite dark_ochre gneiss hedbergite hemorphite jaspet kernite mercoxit omber plagioclase pyroxeres scordite spodumain veldspar bitumens carnotite chromite cinnabar cobaltite coesite euxenite loparite monazite otavite pollucite scheelite sperrylite sylvite titanite vanadinite xenotime ytterbite zeolites zircon blue_ice clear_icicle dark_glitter gelidus glacial_mass glare_crust krystallos white_glaze update
			;;
			*)
				python3 /home/user/Python/Projects/EveOrePrices/main.py "$@"
				exit
			;;
		esac
		shift
	done
done
