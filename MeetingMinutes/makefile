all: M1.pdf M2.pdf M3.pdf M4.pdf

M1.pdf: M1.tex
	pdflatex M1.tex
	rm M1.aux
	rm M1.log

M2.pdf: M2.tex
	pdflatex M2.tex
	rm M2.aux
	rm M2.log

M3.pdf: M3.tex
	pdflatex M3.tex
	rm M3.aux
	rm M3.log

M4.pdf: M4.tex
	pdflatex M4.tex
	rm M4.aux
	rm M4.log

clean:
	#rm *.aux
	#rm *.log
	rm *.pdf
