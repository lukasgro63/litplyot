import bibtexparser
import pandas as pd


def load_csv(file_path):
    return pd.read_csv(file_path)

def load_excel(file_path):
    return pd.read_excel(file_path)

def load_bib(file_path):
    with open(file_path) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries
