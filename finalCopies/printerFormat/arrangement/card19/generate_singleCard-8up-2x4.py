# fronts
startPageBeginRange = 1
startPageEndRange   = 8
pageSkipSize        = 8
endPage = 423

with open('finalCopies/printerFormat/arrangement/card19/run1/singleCard-8up-2x4-py.tex','w+') as f:
    f.write("\\documentclass[letterpaper]{article}\n")
    f.write("\\usepackage[\tpaperwidth= 18 in, "    +
            "\n\t\t\t\t\t\t\tpaperheight=12 in,"    +
            "\n\t\t\t\t\t\t\ttop=0in, "             +
            "\n\t\t\t\t\t\t\tbottom=0in, "          +
            "\n\t\t\t\t\t\t\tleft=0in, "            +
            "\n\t\t\t\t\t\t\tright=0in "            +
            "\n\t\t\t\t\t\t]{geometry}\n")
    f.write("\\usepackage[final]{pdfpages}\n")
    f.write("\\pagenumbering{gobble}\n\n")

    f.write("\\begin{document}\n\n")

    f.write("\\includepdfmerge[\tnoautoscale\t,"    +
            "\n\t\t\t\t\t\t\t\t\tangle=-90\t,"      +
            "\n\t\t\t\t\t\t\t\t\tnup=4x2\t"         +
            "\n\t\t\t\t\t\t\t\t]\n")
    f.write("\t\t\t\t\t\t\t\t{\n")
    while startPageEndRange <= endPage:
        f.write("\t\t\t\t\t\t\t\t\tcompileCardsWOut19/cardsWOut19_front_1up.pdf,\t\t"+str(startPageBeginRange)+"\t\t-\t\t"+str(startPageEndRange)+"\t\t,\n")
        f.write("\t\t\t\t\t\t\t\t\tcompileCardsWOut19/cardsWOut19_back_1up.pdf,\t\t\t"+str(startPageEndRange)+"\t\t-\t\t"+str(startPageBeginRange)+"\t\t,\n")
        startPageBeginRange += pageSkipSize
        startPageEndRange   += pageSkipSize
    f.write("\t\t\t\t\t\t\t\t\t%HARDCODED END\n")
    f.write("\t\t\t\t\t\t\t\t\tcompileCardsWOut19/cardsWOut19_front_1up.pdf,\t\t417\t\t-\t\t423		,\n")
    f.write("\t\t\t\t\t\t\t\t\t../../nBlankPages.pdf \t\t\t\t\t\t\t\t\t\t\t,\t\t\t1\t\t\t\t\t\t\t,\n")
    f.write("\t\t\t\t\t\t\t\t\tcompileCardsWOut19/cardsWOut19_back_1up.pdf,\t\t420\t\t-\t\t417		,\n")
    f.write("\t\t\t\t\t\t\t\t\t../../nBlankPages.pdf \t\t\t\t\t\t\t\t\t\t\t,\t\t\t1\t\t\t\t\t\t\t,\n")
    f.write("\t\t\t\t\t\t\t\t\tcompileCardsWOut19/cardsWOut19_back_1up.pdf,\t\t423\t\t-\t\t421		\n")
    f.write("\t\t\t\t\t\t\t\t}\n")
    f.write("\t\\end{document}")



#
# \end{document}
    # while startPageEndRange <= endPage:
    #     f.write( "\t\t\tfronts/884-fronts.pdf\t,\t"    + str(startPageBeginRange) + "\t-\t" + str(startPageEndRange) + "\t,\n" )
    #     f.write( "\t\t\t884-backs-1up.pdf\t\t,\t"        + str( startPageBeginRange + int((pageSkipSize/2) -1 ))  + "\t-\t" + str(startPageBeginRange) + "\t,\n" )
    #     f.write( "\t\t\t884-backs-1up.pdf\t\t,\t"        + str(startPageEndRange)  + "\t-\t" + str(int(startPageBeginRange + (pageSkipSize/2))) + "\t,\n" )
    #     startPageBeginRange += pageSkipSize
    #     startPageEndRange   += pageSkipSize
