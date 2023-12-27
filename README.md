# Spanish Wiktionary Parser

This package provides tools to parse the Spanish Wiktionary into a single, readable and easy to process file.

It has been developed in order to obtain files that are easy to use for machine learning purposes.

## Intended for Developers

As it's goal is to be used by software developers, it's programmatic interface may not be the most friendly.

If you are not a developer, you may find the files that this package generates more interesting that the package itself.

Check the [project releases](https://github.com/elcapo/eswiktionary_parser/releases) to find those files.

## Installation

To work with the package on your own, you'll need:

- Python ^3.9
- Poetry (^1.6 recommended)
- Git (^2.34 recommended)

In order to install this repository, first clone it (or manually download it):

```bash
git clone https://github.com/elcapo/spanish-wiktionary-parser.git
```

then install dependencies with **Poetry**:

```bash
cd spanish-wiktionary-parser
poetry install
```

and finally open a **Poetry** shell:

```bash
poetry shell

# now you can open a Python interpreter as usual
# and import stuff from eswiktionary_parser
python
```

## Usage

By default, the package is meant to be used by:

1. downloading a Spanish Wiktionary `.xml` dump into the `downloads/` folder,
2. parsing it in order to extract a `.csv` file from the dump.

Both tasks will be automatically executed by calling `dump_parser.py` from a **Poetry** shell:

```bash
python eswiktionary_parser/dump_parser.py

# the file can easily be sorted by running
# (assuming that you have the `sort` utility)
sort -o downloads/eswiktionary.csv downloads/eswiktionary.csv
```

The first time you run the command, a dump will be automatically downloaded and uncompressed in the `downloads/` folder as `eswiktionary-latest-pages-articles.xml`. Be pacient, as the download may take some time.

Once the file is downloaded, the script will run faster as the download phase will be skipped.

After the download is completed (also if it was completed in a previous execution), a `eswiktionary.csv` file will be generated along with the dump in the `downloads/` folder.

## Tests

A suite of tests lives with the code in order to facilitate refactors and also to provide some traceability of cases that have been found problematic during the development.

The test suite can be easily executed:

```bash
poetry run pytest -v
```