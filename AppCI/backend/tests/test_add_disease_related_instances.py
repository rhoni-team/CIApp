"""module with test class for adding diseases data"""
import pandas as pd
from django.apps import apps
from django.test.testcases import TestCase
from backend.data_loading.add_disease_related_instances import AddDiseasesData


test_df = pd.read_csv(
    './backend/data_loading/data/test_csv.csv')

mocked_row = {
    'tipo_de_enfermedad': None,
    'enfermedad': 'Escabiosis',
    'tipo_de_aislamiento': 'Contacto',
    'tipo_de_precaucion': 'Contacto',
    'modo_de_limpieza': ['Monopersulfato de potasio 20%'],
    'observacion_qx': None,
    'tiempo_de_aislamiento': None,
    'declaracion_obligatoria': "si",
    'comparte_habitacion': None,
    'advertencia': None,
    'isolation_time': None,
    'isolation_unit': None,
    'with_atb': None
}


class AddDiseasesDataTest(TestCase):
    """test to know that column names are being cleaned ok"""

    @classmethod
    def setUpTestData(cls) -> None:
        """ class methods and variables """
        cls.test_df = test_df
        cls.mocked_row = mocked_row

    def test_add_si_no_boolean(self):
        """test if function replace si, no or None by bool value"""
        utils_add_data = AddDiseasesData(apps=apps, row_data=mocked_row)

        utils_add_data.add_si_no_boolean(field_name_row="declaracion_obligatoria",
                                         field_name_disease_table="mandatory_declaration")

        self.assertTrue(utils_add_data.disease_instance_data.get("mandatory_declaration"))

        # mocked data with no

        self.mocked_row["declaracion_obligatoria"] = "no"

        utils_add_data = AddDiseasesData(apps=apps, row_data=self.mocked_row)

        utils_add_data.add_si_no_boolean(field_name_row="declaracion_obligatoria",
                                         field_name_disease_table="mandatory_declaration")

        self.assertFalse(utils_add_data.disease_instance_data.get("mandatory_declaration"))

        utils_add_data.add_si_no_boolean(field_name_row="comparte_habitacion",
                                         field_name_disease_table="room_sharing")

        self.assertIsNone(utils_add_data.disease_instance_data.get("room_sharing"))
