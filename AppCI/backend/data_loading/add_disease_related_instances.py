"""module with auxiliary functions to add instances in disease model"""
from clean_text_rhoni import clean_text_snake_case


class AddDiseasesData:
    """class to add data to a disease instance dictionary"""

    def __init__(self, apps, row_data: dict) -> "dict":
        self.apps = apps
        self.row_data = row_data
        self.disease_instance_data = {}
        self.cleaning_type_instances = []

    def add_all_data_to_disease_data(self):
        """run all auxiliary functions to save all data"""
        print("ENTRA")
        self.add_name_and_label_to_instance_data()
        self.add_disease_type_to_instance_data()
        self.add_precaution_type_to_instance_data()
        self.add_isolation_time_to_instance_data()
        self.add_isolation_unit_to_instance_data()

    def add_name_and_label_to_instance_data(self):
        """add disease.name and disease.label to instance dictionary"""
        label = self.row_data.get('enfermedad')
        print(label)
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
            except:
                self.cleaning_type_instances = None
        return self.cleaning_type_instances

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

    def get_related_instance(self, cell_content: str, model_name: str) -> "model":
        """get the related disease FK instance from cell content"""
        related_instance = None
        related_model = self.apps.get_model('backend', model_name)

        if cell_content is not None:
            cell_content = clean_text_snake_case(cell_content)
            try:
                related_instance = related_model.objects.get(name=cell_content)
            except:
                related_instance = None
        return related_instance
