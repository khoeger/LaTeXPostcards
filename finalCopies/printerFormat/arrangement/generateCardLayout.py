# fronts

startPageBeginRange = 1
startPageEndRange   = 8
pageSkipSize        = 8
endPage = 884

with open('latex-generator.txt','w+') as f:
    while startPageEndRange <= endPage:
        f.write( "\t\t\tfronts/884-fronts.pdf\t,\t"    + str(startPageBeginRange) + "\t-\t" + str(startPageEndRange) + "\t,\n" )
        f.write( "\t\t\t884-backs-1up.pdf\t\t,\t"        + str( startPageBeginRange + int((pageSkipSize/2) -1 ))  + "\t-\t" + str(startPageBeginRange) + "\t,\n" )
        f.write( "\t\t\t884-backs-1up.pdf\t\t,\t"        + str(startPageEndRange)  + "\t-\t" + str(int(startPageBeginRange + (pageSkipSize/2))) + "\t,\n" )
        startPageBeginRange += pageSkipSize
        startPageEndRange   += pageSkipSize
