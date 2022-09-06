import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

playstore_df = pd.read_excel('https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx',
                              usecols=['App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'],
                              parse_dates='Last_Updated',
                              )