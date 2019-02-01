# ESI for "Introducing classical molecular dynamics simulation to users of scattering"

<!--- [![arXiv](https://img.shields.io/badge/arXiv-1810.07616-orange.svg)](https://arxiv.org/abs/1810.07616) [![DOI](https://zenodo.org/badge/144010644.svg)](https://zenodo.org/badge/latestdoi/144010644) -->

[Andrew R. McCluskey](https://orcid.org/0000-0003-3381-5911)&ast;, [James Grant](https://orcid.org/0000-0003-1362-2055), [Adam R.Symington](https://orcid.org/0000-0001-6059-497X), [Tim Snow](https://orcid.org/0000-0001-7146-6885), James Doutch, [Benjamin J. Morgan](https://orcid.org/0000-0002-3056-8233)&ast;, [Stephen C. Parker](https://orcid.org/0000-0003-3804-0975), [Karen J. Edler](https://orcid.org/0000-0001-5822-0127).

&ast;[a.r.mccluskey@bath.ac.uk](mailto:a.r.mccluskey@bath.ac.uk)/[andrew.mccluskey@diamond.ac.uk](mailto:aandrew.mccluskey@diamond.ac.uk) & [b.j.morgan@bath.ac.uk](mailto:b.j.morgan@bath.ac.uk)

This is the electronic supplementary information (ESI) associated with the publication "Introducing classical molecular dynamics simulation to users of scattering".
This ESI provides full details of the analyses performed in the work and access to an automated analysis workflow, through this we aim to provide better access to analysis reproduciblility.
For more information about reproducible workflows in Python, check out [Tania Allard's talk from Pycon2018](http://bitsandchips.me/Talks/PyCon.html#/title).

## Analysis

This ESI aims to provide a fully reproducible workflow to the data analysis presented within the paper.

Requirements:

- anaconda or miniconda python

The supplied Snakemake file, will reproduce all of the analysis, plot the figures, and build a preprint version of the paper (`reports/paper.pdf`) when run.

If you want to re-run the analysis, the following commands:

```
conda create --name paper_env python

source activate paper_env

conda install -c biopython snakemake

pip install -r requirements.txt

snakemake clean # this will remove all of the output from previous runs

snakemake
```

## [Figures](/reports/figures)

PDF versions of the figures, can be found in the `reports/figures` directory.

## Acknowledgements

A. R. M. is grateful to the University of Bath and Diamond Light Source for co-funding a studentship (Studentship No. STU0149).
B. J. M. acknowledges support from the Royal Society (Grant No. UF130329).

## Project Organization

    .
    ├── AUTHORS.md
    ├── LICENSE         # CC-BY-SA-4.0
    ├── README.md       # You are here
    ├── Snakefile       # Makefile to outline workflow
    ├── config          # requirements.txt file
    ├── notebooks       # Notebook for plotting
    ├── reports         # Paper and ESI
        └── figures
