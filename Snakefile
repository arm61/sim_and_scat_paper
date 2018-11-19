FIGURES = 'reports/figures/chem_data_py.pdf'

rule all:
    input:
        'reports/paper.pdf'

rule make_pdf:
    input:
        'reports/paper.tex',
        'reports/iucr.bib',
        FIGURES
    output:
        'reports/paper.pdf'
    shell:
        """
        cd reports
        pdflatex paper.tex
        bibtex paper.aux
        pdflatex paper.tex
        pdflatex paper.tex
        """

rule clean:
    shell:
        """
        rm reports/figures/*
        rm reports/paper.pdf
        """

rule pdfclean:
    shell:
        "rm reports/paper.pdf"

rule make_figures:
    input:
        'scripts/plots.py'
    output:
        FIGURES
    shell:
        """
        python scripts/plots.py
        """
