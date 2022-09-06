import numpy as np
import pandas as pd

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

movies = pd.read_csv('C:\\Users\\Sean\\Documents\\GitHub\\RDP-Reading-Data-with-Python-and-Pandas\\unit-1-reading-data-with-python-and-pandas\\lesson-2-load-movies-dataset\\files\\movies.csv',
                     header=None,
                     names=column_names,
                     sep='|',
                    #  na_values=['','?','-'],
                     skiprows=3)


