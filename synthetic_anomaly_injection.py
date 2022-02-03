from pandas import np
import pandas as pd
from PELL_street_lighting_data import DynamicDataManager


class SyntheticAnomalies:
    data_mgr = DynamicDataManager()
    df = data_mgr.load_jsons()

    def synthetic_anomalies(self, list_of_anomalies):
        number_of_anomalies = len(list_of_anomalies)

        # select the random rows with specific column value: 0 or 1 in our case but
        # not select the same row by more than one; and replace the ActiveEnergy value for the selected random rows
        # with the user anomalous values
        updated_df = self.df.dayORnight[self.df.dayORnight.eq('1')].sample(number_of_anomalies, replace=False).index
        self.df.loc[updated_df, 'ActiveEnergy'] = list_of_anomalies

        # print the updated dataframe

        pd.set_option('display.max_rows', 20000)
        print(self.df.head(18000))
        print(updated_df.tolist())





