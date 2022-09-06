from operator import index
import numpy as np
import pandas as pd

from tests import test_simpsons_columns as columns, test_simpsons_item as item, test_simpsons_shape as shape
import sys

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']
             
simpsons = pd.read_csv('C:\\Users\\Sean\\Documents\\GitHub\\RDP-Reading-Data-with-Python-and-Pandas\\unit-1-reading-data-with-python-and-pandas\\lesson-4-tsv-with-the-simpsons-episodes\\files\\simpsons-episodes.tsv',
                        sep='\t',
                        names=col_names,
                        usecols=['Title', 'Air date', 'Production code', 'IMDB rating'],
                        skiprows=4,
                        index_col=[2],
                        na_values='no_val',
                        parse_dates=[2])

# Testing calls
sys.path.insert(0, 'C:\\Users\\Sean\\Documents\\GitHub\\RDP-Reading-Data-with-Python-and-Pandas\\unit-1-reading-data-with-python-and-pandas\\lesson-4-tsv-with-the-simpsons-episodes\\tests')

columns.test_simpsons_columns(simpsons)
item.test_simpsons_item(simpsons)
shape.test_simpsons_shape(simpsons)
# print(simpsons.head())