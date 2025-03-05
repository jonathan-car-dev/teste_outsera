import re
import pandas as pd
from pandas import DataFrame
from typing import List
from app.models import Movie


class Parser:
    @staticmethod
    def _data_cleaning_producer_names(df) -> DataFrame:
        for _, row in df.iterrows():
            if row['producers'] != 'no-producers' and (',' in row['producers'] or 'and' in row['producers']):
                producers = row['producers'].replace(' and ', '|').replace(', ', '|')
                producers = producers.split('|')
                for p in producers:
                    df.loc[len(df)] = [row['year'], row['title'], row['studios'], p, row['winner']]

        return df

    @staticmethod
    def _is_valid_row(row) -> bool:
        return (re.match(r'^[1-9]\d*$', str(row['year'])) and row['producers'] != 'no-producer' and
                int(row["year"]) != 0000)

    @staticmethod
    def csv_to_movielist(path_to_csv) -> List[Movie]:
        movies = []
        df = pd.read_csv(path_to_csv, sep=';', on_bad_lines='warn')
        df.columns = df.columns.str.lower()

        wanted_columns = ['winner', 'producers', 'title', 'studios', 'year']

        if not all(element in wanted_columns for element in df.columns):
            raise SystemExit('The columns names in the movielist are different from the sample file')

        df.fillna({"winner": "no",
                   "producers": 'no-producer',
                   'title': 'no-title',
                   'studios': 'no-studio',
                   'year': 0000,
       },inplace=True)

        df = Parser._data_cleaning_producer_names(df)

        for _, row in df.iterrows():
            if Parser._is_valid_row(row):
                movies.append(Movie(year=int(row["year"]),
                                    title=row['title'],
                                    studios=row['studios'],
                                    producer=row['producers'],
                                    winner=(True if row['winner'] == 'yes' else False),
                                    uuid=None))

        return movies