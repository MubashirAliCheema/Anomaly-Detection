from pandas import np
import pandas as pd
from PELL_street_lighting_data import DynamicDataManager
import random


class SyntheticAnomalies:
    data_mgr = DynamicDataManager()
    df = data_mgr.load_jsons()

    # S1: To handle random positive high peaks at the night time. For example, a
    # terminal operating at the night time and some random high peaks encountered, which deviates
    # from the normal consumption measures.
    def synthetic_anomalies_S1(self):

        # For night, filter the data frame
        updated_df = self.df[self.df['dayORnight'] == '0']

        min_range = 250
        max_range = 270
        number_of_anomalies = 5

        list_of_anomalies = []

        for _ in range(5):
            list_of_anomalies.append(random.randint(min_range, max_range))
        print(list_of_anomalies)

        random_rows = updated_df.sample(number_of_anomalies, replace=False).index
        print(random_rows)
        updated_df.loc[random_rows, 'ActiveEnergy'] = list_of_anomalies

        return updated_df

    # S2: To handle random negative high peaks at the day time. For example, a
    # terminal is switched off during the day time and some random negative peaks encountered.
    def synthetic_anomalies_S2(self):

        # For day, filter the data frame
        updated_df = self.df[self.df['dayORnight'] == '1']

        min_range = -50
        max_range = -30
        number_of_anomalies = 5

        list_of_anomalies = []

        for _ in range(5):
            list_of_anomalies.append(random.randint(min_range, max_range))
        print(list_of_anomalies)

        random_rows = updated_df.sample(number_of_anomalies, replace=False).index
        print(random_rows)
        updated_df.loc[random_rows, 'ActiveEnergy'] = list_of_anomalies

        return updated_df

    # S3: To handle random low peaks at the night time. For example, a terminal is
    # operating at the night and some random low peaks encountered, which are different from the
    # normal consumption measures.
    def synthetic_anomalies_S3(self):

        # For night, filter the data frame
        updated_df = self.df[self.df['dayORnight'] == '0']

        min_range = 0.50
        max_range = 2.90
        number_of_anomalies = 5

        list_of_anomalies = []

        for _ in range(5):
            list_of_anomalies.append(round(random.uniform(min_range, max_range), 2))
        print(list_of_anomalies)

        random_rows = updated_df.sample(number_of_anomalies, replace=False).index
        print(random_rows)
        updated_df.loc[random_rows, 'ActiveEnergy'] = list_of_anomalies

        return updated_df

    # S5: To handle random high peaks at the day time. For example, a terminal was
    # switched off at the day time and some random high peaks encountered, which deviates from
    # the normal consumption measures at the day time.
    def synthetic_anomalies_S5(self):

        # For day, filter the data frame
        updated_df = self.df[self.df['dayORnight'] == '1']

        min_range = 250
        max_range = 290
        number_of_anomalies = 5

        list_of_anomalies = []

        for _ in range(5):
            list_of_anomalies.append(random.randint(min_range, max_range))
        print(list_of_anomalies)

        random_rows = updated_df.sample(number_of_anomalies, replace=False).index
        print(random_rows)
        updated_df.loc[random_rows, 'ActiveEnergy'] = list_of_anomalies

        return updated_df

    # S4: To handle continuous low peaks at the night. For example, a terminal is
    # switched off for a duration of three to four hours at the night time.
    def synthetic_anomalies_S4(self):

        # For night, filter the data frame
        updated_df = self.df[self.df['dayORnight'] == '0']

        min_range = 0.50
        max_range = 2.90
        number_of_anomalies = 10

        list_of_anomalies = []

        for _ in range(number_of_anomalies):
            list_of_anomalies.append(round(random.uniform(min_range, max_range), 2))
        print(list_of_anomalies)

        n = random.randint(0, len(updated_df) - number_of_anomalies)
        random_consecutive_rows = updated_df[n:n + number_of_anomalies].index
        print(random_consecutive_rows)

        updated_df.loc[random_consecutive_rows, 'ActiveEnergy'] = list_of_anomalies

        return updated_df

    # S6: To handle continuous high peaks at the day time. For example, a terminal
    # switched on for a duration of three to four hours at day time.
    def synthetic_anomalies_S6(self):

        # For day, filter the data frame
        updated_df = self.df[self.df['dayORnight'] == '1']

        min_range = 180
        max_range = 200
        number_of_anomalies = 10

        list_of_anomalies = []

        for _ in range(number_of_anomalies):
            list_of_anomalies.append(random.randint(min_range, max_range))
        print(list_of_anomalies)

        n = random.randint(0, len(updated_df) - number_of_anomalies)
        random_consecutive_rows = updated_df[n:n + number_of_anomalies].index
        print(random_consecutive_rows)

        updated_df.loc[random_consecutive_rows, 'ActiveEnergy'] = list_of_anomalies

        return updated_df
