"""module with tests for data loading"""
import pandas as pd
from django.test.testcases import TestCase
from backend.data_loading.load_diseases_data import PreProcessDiseasesData, get_diseases_data
from backend.data_loading.cleaning_column_names import (map_original_column_names,
                                                        replace_original_column_names,
                                                        processed_disease_column_names)

test_df = pd.read_csv(
    './backend/data_loading/data/test_csv.csv')


class CleaningColumnNamesTest(TestCase):
    """test to know that column names are being cleaned ok"""

    @classmethod
    def setUpTestData(cls) -> None:
        """ class methods and variables """
        cls.test_df = test_df

    def test_original_names(self):
        """test that column names in csv are as expected"""
        original_names = self.test_df.columns.to_list()
        expected_names = list(map_original_column_names.keys())
        self.assertEqual(original_names, expected_names)

    def test_replace_column_names(self):
        """test if names are replaces correctly"""
        df_new_names = replace_original_column_names(self.test_df)
        new_column_names = df_new_names.columns.to_list()
        expected_column_names = list(map_original_column_names.values())
        self.assertEqual(new_column_names, expected_column_names)


class LoadDataTest(TestCase):
    """ class to test functions related to geo point cases module """

    @classmethod
    def setUpTestData(cls):
        """ class methods and variables """
        cls.preprocess_utils = PreProcessDiseasesData(diseases_df=test_df)
        cls.diseases_df = cls.preprocess_utils.diseases_df

    def test_save_isolation_time_data(self):
        """ save_isolation_time_data funcion """
        isolation_time_column = self.diseases_df.loc[:, 'tiempo_de_aislamiento']
        self.preprocess_utils.save_isolation_time_data(isolation_time_column=isolation_time_column)

        row_num_df = len(isolation_time_column)

        self.assertEqual(row_num_df, len(self.preprocess_utils.isolation_time_clean_column))
        self.assertEqual(row_num_df, len(self.preprocess_utils.units_of_time))

    def test_save_with_atb_data(self):
        """test save_with_atb_param funcion"""
        isolation_time_column = self.diseases_df.loc[:, 'tiempo_de_aislamiento']
        self.preprocess_utils.save_with_atb_param(isolation_time_column=isolation_time_column)

        row_num_df = len(isolation_time_column)

        self.assertEqual(row_num_df, len(self.preprocess_utils.with_atb))

    def test_get_diseases_data(self):
        """test for get_diseases_data function"""
        diseases_data = get_diseases_data(diseases_df=test_df)

        expected_colum_names = processed_disease_column_names

        first_row = diseases_data[0]
        got_colum_names = list(first_row.keys())

        self.assertListEqual(expected_colum_names, got_colum_names)
