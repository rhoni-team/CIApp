"""module with utils to reorder API data"""


class ReorderAPIData:
    """class to order the data from API to send to correct dictionary to frontend"""

    def __init__(self, disease_data: dict) -> None:
        self.disease_data = disease_data

    def reorder_data(self):
        """reorders data so it can be readed in fronted"""
        ordered_data = {}
        ordered_data["id"] = self.disease_data["id"]
        ordered_data["name"] = self.disease_data["label"]
        ordered_data = self.reorder_disease_type(ordered_data=ordered_data)
        ordered_data["cautions"] = self.reorder_cautions_object()
        ordered_data["cleaning"] = self.reorder_cleaning_object()
        ordered_data["isolation"] = self.reorder_isolation_object()
        ordered_data["mandatoryNotification"] = self.reorder_mandatory_notification()
        ordered_data["roomSharing"] = self.reorder_room_sharing()
        ordered_data["withAtb"] = self.disease_data["with_atb"]
        ordered_data["other_isolation"] = self.disease_data["other_isolation"]
        ordered_data["warnings"] = self.reorder_warnings()
        ordered_data["info"] = []
        return ordered_data

    def reorder_disease_type(self, ordered_data):
        """reorder data values to get type object"""
        disease_type = self.disease_data["disease_type"]
        ordered_data["type"] = None
        if disease_type is not None:
            ordered_data["type"] = disease_type["name"]
        return ordered_data

    def reorder_cautions_object(self):
        """reorder data values to get cautions object"""
        cautions = {}
        precautions = self.disease_data["precaution_type"]
        precautions_label = precautions["label"]
        cautions["precautions"] = precautions
        cautions["list"] = precautions_label
        cautions = self.add_empty_info_files_to_object(cautions)
        return cautions

    def reorder_cleaning_object(self):
        """reorder data values to get cleaning object"""
        cleaning = {}
        cleaning_data = self.disease_data["cleaning_type"]
        cleaning_labels = [x["label"] for x in cleaning_data]
        cleaning["cleaning_type"] = cleaning_data
        cleaning["list"] = cleaning_labels
        cleaning = self.add_empty_info_files_to_object(cleaning)
        return cleaning

    def reorder_isolation_object(self):
        """reorder data values to get isolation object"""
        isolation = {}
        isolation_time = self.disease_data["isolation_time"]
        isolation_period = self.disease_data["isolation_unit"]
        if isolation_period:
            isolation_period = isolation_period["label"]
        isolation["isolationTime"] = isolation_time
        isolation["isolationPeriod"] = isolation_period
        isolation = self.add_empty_info_files_to_object(isolation)
        return isolation

    def reorder_mandatory_notification(self):
        """reorder data values to get mandatory notification object"""
        mandatory_notification = {}
        mandatory_notification["notify"] = self.disease_data["mandatory_declaration"]
        mandatory_notification = self.add_empty_info_files_to_object(mandatory_notification)
        return mandatory_notification

    def reorder_room_sharing(self):
        """reorder data values to get room sharing object"""
        room_sharing = {}
        room_sharing["shareable"] = self.disease_data["room_sharing"]
        room_sharing = self.add_empty_info_files_to_object(room_sharing)
        return room_sharing

    def reorder_warnings(self):
        """reorder data values to get room sharing object"""
        warnings = []
        if self.disease_data["isolation_warnings"] is not None:
            warnings.append(self.disease_data["isolation_warnings"])
        return warnings

    def add_empty_info_files_to_object(self, dict_object: dict) -> dict:
        """add keys of info and files with empty values to dictionary"""
        dict_object["info"] = []
        dict_object["files"] = []
        return dict_object
