map_original_column_names = {
    "Tipo": "tipo_de_enfermedad",
    "Enfermedad": "enfermedad",
    "Tipo de aislamiento": "tipo_de_aislamiento",
    "tipo_de_precaucion": "tipo_de_precaucion",
    "Modo de limpieza": "modo_de_limpieza",
    "Observación (Modo de limp QX)": "observacion_qx",
    "Tiempo de aislamiento": "tiempo_de_aislamiento",
    "declaración obligatoria": "declaracion_obligatoria",
    "Comparte habitación": "comparte_habitacion",
    "Advertencia": "advertencia",
}

processed_disease_column_names = [
    "tipo_de_enfermedad",
    "enfermedad",
    "tipo_de_aislamiento",
    "tipo_de_precaucion",
    "modo_de_limpieza",
    "observacion_qx",
    "tiempo_de_aislamiento",
    "declaracion_obligatoria",
    "comparte_habitacion",
    "advertencia",
    "isolation_time",
    "isolation_unit",
    "with_atb",
]


def replace_original_column_names(df_data):
    """replace the original and complex csv column names with its simplified ones"""
    df_data.rename(columns=map_original_column_names, inplace=True)
    return df_data
