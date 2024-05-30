import numpy as np
import pandas as pd
from typing import List
from clean_text_rhoni import clean_text
from backend.data_loading.cleaning_column_names import replace_original_column_names


diseases_df = pd.read_csv(
    './backend/data_loading/data/diseases_table_csv.csv')


def get_diseases_data(diseases_df: "pd.DataFrame"= diseases_df) -> List[dict]:
    """get diseases data as a list of dictionaries"""
    preprocess_utils = PreProcessDiseasesData(diseases_df=diseases_df)
    diseases_data = preprocess_utils.get_diseases_data()
    return diseases_data


class PreProcessDiseasesData():
    """class with functions to read and clean diseases data from a pandas dataframe"""
    
    not_found = -1

    def __init__(self, diseases_df: "pd.Dataframe") -> None:
        self.diseases_df = diseases_df
        self.diseases_df = self.replace_column_names()
        self.diseases_df = self.replace_npnan_by_none(self.diseases_df)
        self.units_of_time = []
        self.isolation_time_clean_column = []
        self.with_atb = []

    def replace_column_names(self): 
        """replace original column names with cleaner names"""
        cleaned_columns_df = replace_original_column_names(df_data=self.diseases_df)
        return cleaned_columns_df

    def replace_npnan_by_none(self, diseases_df):
        """replace np nan values in dataframe for None"""
        df_with_none = diseases_df.replace(to_replace=np.nan, value=None)
        return df_with_none

    def get_diseases_data(self) -> List[dict]:
        """process and get diseases data as a list of dictionaries"""
        diseases_df = self.split_cleaning_type_column_in_different_types(self.diseases_df)
        diseases_df = self.add_time_related_columns_to_diseases_dataframe(diseases_df)
        diseases_df = self.add_atb_column_to_diseases_dataframe(diseases_df=diseases_df)
        diseases_data = diseases_df.to_dict(orient='records')
        return diseases_data

    def split_cleaning_type_column_in_different_types(self, diseases_df: "pd.DataFrame") -> "pd.DataFrame":
        """change string of cleaning types to arrays and split them in different types if necessary"""
        cleaning_type_column = diseases_df.loc[:, 'modo_de_limpieza']
        cleaning_type_as_array = []

        for row in cleaning_type_column:
            if row is not None:
                row = row.split(" y ")
                cleaning_type_as_array.append(row)
            else:
                cleaning_type_as_array.append(None)

        diseases_df['modo_de_limpieza'] = cleaning_type_as_array
        return diseases_df

    def add_time_related_columns_to_diseases_dataframe(self, diseases_df: "pd.DataFrame") -> "pd.DataFrame":
        """add clean isolation time columns data to diseases dataframe"""

        isolation_time_column = diseases_df.loc[:, 'tiempo_de_aislamiento']

        self.save_isolation_time_data(isolation_time_column=isolation_time_column)

        diseases_df["isolation_time"] = self.isolation_time_clean_column
        diseases_df["isolation_unit"] = self.units_of_time

        diseases_df = self.replace_npnan_by_none(diseases_df)

        return diseases_df
    
    def add_atb_column_to_diseases_dataframe(self, diseases_df: "pd.DataFrame") -> "pd.DataFrame":
        """add atb column to diseases dataframe"""
        isolation_time_column = diseases_df.loc[:, 'tiempo_de_aislamiento']
        self.save_with_atb_param(isolation_time_column=isolation_time_column)
        diseases_df["with_atb"] = self.with_atb
        return diseases_df

    def save_isolation_time_data(self, isolation_time_column: "pd.Series") -> None:
        """separate time units to a different column"""

        terms_to_lookup = ["ano", "meses", "semanas", "dias", "alta medica", "muerte"]
        terms_to_replace = ["years", "months", "weeks", "days", "medical_discharge", "death"]

        for cell in isolation_time_column:
            if cell is not None:
                clean_cell = self.clean_cell_content(cell)

                if self.has_time_unit(clean_cell):
                    for index, term in enumerate(terms_to_lookup):
                        if self.lookup_time_unit(clean_cell, term):
                            self.save_unit_of_time_value(cell, terms_to_replace[index])

                elif cell.find("no") != self.not_found and cell.find("ano") == self.not_found:
                    self.save_unit_of_time_value(cell, "no")

                else:
                    self.isolation_time_clean_column.append(None)
                    self.units_of_time.append(None)
            else:
                self.isolation_time_clean_column.append(None)
                self.units_of_time.append(None)

    def clean_cell_content(self, cell_content):
        """clean cell content by using clean text rhoni funcion """
        if isinstance(cell_content, str):
            clean_cell = clean_text(cell_content)
            return clean_cell
        return cell_content
    
    def has_time_unit(self, cell):
        """Assert if any time unit is present in cell content"""
        terms_to_lookup = ["ano", "meses", "semanas", "dias", "alta medica", "muerte"]

        are_founded = []
        for term in terms_to_lookup:
            if cell.find(term) != self.not_found:
                are_founded.append(True)
            else:
                are_founded.append(False)
        return any(are_founded)

    def lookup_time_unit(self, cell, time_to_lookup: str) -> "bool":
        """Lookup if a given time unit is present in a cell"""
        if cell.find(time_to_lookup) != self.not_found:
            return True
        return False

    def save_unit_of_time_value(self, cell, unit_of_time: str) -> None:
        """Save the values of time unit and time value in the corresponding list"""
        value = [int(s) for s in cell.split() if s.isdigit()]
        if value:
            value = value[0]
            self.isolation_time_clean_column.append(value)
        else:
            self.isolation_time_clean_column.append(None)
        self.units_of_time.append(unit_of_time)

    def save_with_atb_param(self, isolation_time_column: "pd.Series") -> None:
        """Save if atb param is present in isolation time column"""
        for cell in isolation_time_column:

            if cell is not None:
                clean_cell = self.clean_cell_content(cell)

                if clean_cell.find("atb") != self.not_found:
                    self.with_atb.append(True)
                else:
                    self.with_atb.append(False)
            else:
                self.with_atb.append(None)

