# Generate your own Postal Score Postcards using TeX

This is the current code used used to create
[QuGyrs R. Katzu Press](https://qugyrsrkatztu.github.io)'s Postal Scores.

There are 20 postcards in a Postal Score set, along with one instruction card.
The cards are 5.5"x4.25" by default.

Work & README in progress.

## Compile Your own Set of Postal Scores
To compile a set of postal scores on your own, compile the files using LaTeX. Compile using the order shown below.

I used XeLaTeX to generate files because of my font choice.

Generate Postcard Fronts -> Generate Postcard Backs ->

### Global Values
Global variables are found in 'globalVariables.tex' in the root folder.
Make changes there.
Place a logo .png file in the root folder to add a logo.


### Generate Postcard Fronts
Please generate postcard front files in the order given below, in Files to Compile and Run.

#### File System Specifics

##### Constants
The constant files contain the constants necessary to generate each card.
To create a custom set of cards, modify the constants.

##### Layouts
Card layouts are in the layout folder.
To modify the placement of elements of a card, modify the card layouts. If you do not want to change the layout, and only want to change the content, you do not need to modify the layout files.

Layouts are identified by the number of senders and receivers.
For example, the file named '0s_1r_layout.tex' is the layout for a card with 0 senders and 1 recipient.

#### Files to Compile and Run
1. Run 'generate_postcard_front.tex'. This generates all postcard fronts at 100% scale
2. Run 'front_in_order_small.tex'. This reduces all postcards to 95% so that there is a defined border. It lays the cards out in sequential order, ready to be rearranged for printing.

### Generate Postcard Backs

### Put it all together - Printing layout

#### Personal Printer

#### Print Shop

## Works Referenced
- [Business Card Template](https://www.overleaf.com/gallery/tagged/business-cards)
Specifically, [Karol Koziol](https://www.overleaf.com/latex/templates/business-card-template/yrqjgydpprrb)'s and [Helena Rasche and LianTze Lim](https://www.overleaf.com/latex/templates/business-card-for-programmers-slash-developers-with-photo/wymnjgtxkdwh)
- [Front Back Business Card](https://olivierpieters.be/blog/2017/02/11/designing-a-business-card-in-latex) by Olivier Pieters
- [Memoir Class TeX Docs](http://texdoc.net/texmf-dist/doc/latex/memoir/memman.pdf)
- [TikZ \& PGF Manual](http://ctan.math.utah.edu/ctan/tex-archive/graphics/pgf/base/doc/pgfmanual.pdf)
- [PDF Pages](http://mirror.utexas.edu/ctan/macros/latex/contrib/pdfpages/pdfpages.pdf)
- [This Page Style](http://www.personal.ceu.hu/tex/pagestyl.htm#thispgstyle)
- [Overlay Text On Photos](https://tex.stackexchange.com/questions/20792/how-to-superimpose-latex-on-a-picture) - make a grid of 4
