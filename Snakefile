FIGURES = 'reports/figures/chem_data_py.pdf'

rule all:
    input:
        'reports/preprint.pdf'

rule make_preprint:
    input:
        'reports/preprint.tex',
        'reports/bib.bib',
        FIGURES
    output:
        'reports/preprint.pdf'
    shell:
        """
        cd reports
        pdflatex preprint.tex
        bibtex preprint.aux
        pdflatex preprint.tex
        pdflatex preprint.tex
        """

rule clean:
    shell:
        """
        rm reports/figures/*
        rm reports/preprint.pdf
        """

rule pdfclean:
    shell:
        "rm reports/preprint.pdf"

rule make_figures:
    input:
        'scripts/plots.py'
    output:
        FIGURES
    shell:
        """
        python scripts/plots.py
        """
