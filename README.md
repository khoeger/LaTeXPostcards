# Make a Postal Score Postcards using TeX

This is the current code used used to create
[QuGyrs R. Katzu Press](https://qugyrsrkatztu.github.io)'s Postal Scores.

## How to Compile A Set of Postal Scores
To compile a set of postal scores on your own, files need to be compiled in order.
Certain files take in specific output.
### Generate Postcard Fronts
#### File System
##### Layouts
Card layouts are in the layout folder.
Layouts are identified by the number of senders and receivers.
For example, the file named '0s_1r_layout.tex' is the layout for a card with 0 senders and 1 recipient.

#### Files to Compile and Run
1. Run 'generate_postcard_front.tex'.
2. Run 'front_in_order_small.tex'.

## Works Referenced
- [Business Card Template](https://www.overleaf.com/gallery/tagged/business-cards)
Specifically, [Karol Koziol](https://www.overleaf.com/latex/templates/business-card-template/yrqjgydpprrb)'s and [Helena Rasche and LianTze Lim](https://www.overleaf.com/latex/templates/business-card-for-programmers-slash-developers-with-photo/wymnjgtxkdwh)
- [Front Back Business Card](https://olivierpieters.be/blog/2017/02/11/designing-a-business-card-in-latex) by Olivier Pieters
- [Memoir Class TeX Docs](http://texdoc.net/texmf-dist/doc/latex/memoir/memman.pdf)
- [TikZ \& PGF Manual](http://ctan.math.utah.edu/ctan/tex-archive/graphics/pgf/base/doc/pgfmanual.pdf)
- [PDF Pages](http://mirror.utexas.edu/ctan/macros/latex/contrib/pdfpages/pdfpages.pdf)
- [This Page Style](http://www.personal.ceu.hu/tex/pagestyl.htm#thispgstyle)
- [Overlay Text On Photos](https://tex.stackexchange.com/questions/20792/how-to-superimpose-latex-on-a-picture) - make a grid of 4
