"""module with auxiliary functions to add instances in disease model"""
from clean_text_rhoni import clean_text_snake_case, clean_text


class AddDiseasesData:
    """class to add data to a disease instance dictionary"""

    def __init__(self, apps, row_data: dict) -> "dict":
        self.apps = apps
        self.row_data = row_data
        self.disease_instance_data = {}
        self.cleaning_type_instances = []

    def add_all_data_to_disease_data(self):
        """run all auxiliary functions to save all data"""
        self.add_name_and_label_to_instance_data()
        self.add_disease_type_to_instance_data()
        self.add_precaution_type_to_instance_data()
        self.add_isolation_time_to_instance_data()
        self.add_isolation_unit_to_instance_data()
        self.add_with_atb_to_instance_data()
        self.add_other_isolation_to_instance_data()
        self.add_mandatory_declaration_to_instance_data()
        self.add_room_sharing_to_instance_data()
        self.add_warning_to_instance_data()

    def add_cleaning_types_to_instance_data(self):
        """add cleaning type instances. It is a many to many related model"""
        cleaning_type_model = self.apps.get_model('backend', 'CleaningType')
        cleaning_type_content = self.row_data["modo_de_limpieza"]
        if cleaning_type_content is not None:
            try:
                for cleaning_type in cleaning_type_content:
                    cleaning_type = clean_text_snake_case(cleaning_type)
                    ct_instance = cleaning_type_model.objects.get(name=cleaning_type)
                    self.cleaning_type_instances.append(ct_instance)
            except BaseException:
                self.cleaning_type_instances = None
        return self.cleaning_type_instances

    def add_name_and_label_to_instance_data(self):
        """add disease.name and disease.label to instance dictionary"""
        label = self.row_data.get('enfermedad')
        self.disease_instance_data["label"] = label
        self.disease_instance_data["name"] = clean_text_snake_case(label)

    def add_disease_type_to_instance_data(self):
        """add disease type to instance data dictionary"""
        disease_type = self.get_related_instance(
            cell_content=self.row_data["tipo_de_enfermedad"],
            model_name="DiseaseType")
        self.disease_instance_data["disease_type"] = disease_type

    def add_precaution_type_to_instance_data(self):
        """add precaution type to instance data dictionary"""
        precaution_type = self.get_related_instance(
            cell_content=self.row_data["tipo_de_precaucion"],
            model_name="PrecautionType")
        self.disease_instance_data["precaution_type"] = precaution_type

    def add_isolation_time_to_instance_data(self):
        """add isolation time to instance data"""
        isolation_time = self.row_data.get('isolation_time')
        self.disease_instance_data["isolation_time"] = isolation_time

    def add_isolation_unit_to_instance_data(self):
        """add isolation unit FK to instance data"""
        isolation_unit = self.get_related_instance(
            cell_content=self.row_data["isolation_unit"],
            model_name="UnitsOfTime")
        self.disease_instance_data["isolation_unit"] = isolation_unit

    def add_warning_to_instance_data(self):
        """add warning to instance data dictionary"""
        isolation_warning = self.get_related_instance(
            cell_content=self.row_data["advertencia"],
            model_name="IsolationWarnings")
        self.disease_instance_data["isolation_warnings"] = isolation_warning

    def get_related_instance(self, cell_content: str, model_name: str) -> "model":
        """get the related disease FK instance from cell content"""
        related_instance = None
        related_model = self.apps.get_model('backend', model_name)

        if cell_content is not None:
            cell_content = clean_text_snake_case(cell_content)
            try:
                related_instance = related_model.objects.get(name=cell_content)
            except BaseException:
                related_instance = None
        return related_instance

    def add_with_atb_to_instance_data(self):
        """add with atb boolean value to instance"""
        with_atb = self.row_data.get('with_atb')
        self.disease_instance_data["with_atb"] = with_atb

    def add_other_isolation_to_instance_data(self):
        """add isolation special cases to instance data"""
        special_cases_model = self.apps.get_model('backend', "SpecialCasesIsolationTime")
        disease_name = self.disease_instance_data.get("name")

        try:
            special_case_instance = special_cases_model.objects.get(disease_name=disease_name)
            self.disease_instance_data["other_isolation"] = special_case_instance
        except special_cases_model.DoesNotExist:
            self.disease_instance_data["other_isolation"] = None

    def add_mandatory_declaration_to_instance_data(self):
        """add mandatory declaration bool value to instance data"""
        self.add_si_no_boolean(field_name_row="declaracion_obligatoria",
                               field_name_disease_table="mandatory_declaration")

    def add_room_sharing_to_instance_data(self):
        """add mandatory declaration bool value to instance data"""
        self.add_si_no_boolean(field_name_row="comparte_habitacion",
                               field_name_disease_table="room_sharing")

    def add_si_no_boolean(self, field_name_row, field_name_disease_table):
        """transform si no data to boolean value and save it in instance"""
        cell_content = self.row_data.get(field_name_row)

        if cell_content is not None:
            cell_content = clean_text(cell_content)
            if cell_content == "si":
                self.disease_instance_data[field_name_disease_table] = True
            elif cell_content == "no":
                self.disease_instance_data[field_name_disease_table] = False
            else:
                self.disease_instance_data[field_name_disease_table] = None
        else:
            self.disease_instance_data[field_name_disease_table] = None

    def add_observation_qx_to_instance_data(self):
        """add observation qx content to disease instance dictionary"""
        cell_content = self.row_data.get("observacion_qx")
        self.disease_instance_data["qx_observation"] = cell_content
