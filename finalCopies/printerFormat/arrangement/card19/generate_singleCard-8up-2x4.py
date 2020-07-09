# fronts
startPageBeginRange = 1
startPageEndRange   = 8
pageSkipSize        = 8
endPage = 423

with open('singleCard-8up-2x4-py.tex','w+') as f:
    f.write("\\documentclass[letterpaper]{article}")

# \usepackage[paperwidth= 18 in, paperheight=12 in,top=0in, bottom=0in, left=0in, right=0in
# ]{geometry}
#
# \usepackage[final]{pdfpages}
#
#
# % ---
#
# \pagenumbering{gobble}
#
# \begin{document}
# % --- All Postcard Backs
#
# \includepdfmerge[	noautoscale		,
# 								angle=-90			,
# 								nup=4x2
# 							]
# 		{
# 			% about pages
# 			compileCardsWOut19/cardsWOut19_front_1up.pdf,	1		-		8		,
# 			compileCardsWOut19/cardsWOut19_back_1up.pdf,	8		-		1		,
# 			compileCardsWOut19/cardsWOut19_front_1up.pdf,	9		-		16	,
# 			compileCardsWOut19/cardsWOut19_back_1up.pdf,	16	-		9		,
# 			compileCardsWOut19/cardsWOut19_front_1up.pdf,	17	-		24	,
# 			compileCardsWOut19/cardsWOut19_back_1up.pdf,	24	-		17	,
# 			% general cards
# 			compileCardsWOut19/cardsWOut19_front_1up.pdf,	25		-	32	,
# 			compileCardsWOut19/cardsWOut19_back_1up.pdf,	32		-	25	,
# 			compileCardsWOut19/cardsWOut19_front_1up.pdf,	33		-	40	,
# 			compileCardsWOut19/cardsWOut19_back_1up.pdf,	40	-		33	,
# 			compileCardsWOut19/cardsWOut19_front_1up.pdf,	41	-		48	,
# 			compileCardsWOut19/cardsWOut19_back_1up.pdf,	48	-		41	,
# 		}
#
# \end{document}
    # while startPageEndRange <= endPage:
    #     f.write( "\t\t\tfronts/884-fronts.pdf\t,\t"    + str(startPageBeginRange) + "\t-\t" + str(startPageEndRange) + "\t,\n" )
    #     f.write( "\t\t\t884-backs-1up.pdf\t\t,\t"        + str( startPageBeginRange + int((pageSkipSize/2) -1 ))  + "\t-\t" + str(startPageBeginRange) + "\t,\n" )
    #     f.write( "\t\t\t884-backs-1up.pdf\t\t,\t"        + str(startPageEndRange)  + "\t-\t" + str(int(startPageBeginRange + (pageSkipSize/2))) + "\t,\n" )
    #     startPageBeginRange += pageSkipSize
    #     startPageEndRange   += pageSkipSize
