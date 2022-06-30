_autocompleteOres() 
{
	_autocomplete_commands=$(~/Scripts/oreprices shortlist)
	
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="arkonor bistot crokite dark_ochre gneiss hedbergite hemorphite jaspet kernite mercoxit omber plagioclase pyroxeres scordite spodumain veldspar bitumens carnotite chromite cinnabar cobaltite coesite euxenite loparite monazite otavite pollucite scheelite sperrylite sylvite titanite vanadinite xenotime ytterbite zeolites zircon blue_ice clear_icicle dark_glitter gelidus glacial_mass glare_crust krystallos white_glaze update"
    COMPREPLY=( $(compgen -W "$opts" -- ${cur}) )
  return 0

}
complete -F _autocompleteOres oreprices
