# business_logic.py
from data_access import DataAccess

class BusinessLogic:
    def __init__(self, data_access):
        self.data_access = data_access

    def process_data(self, item):
        processed_item = item.upper()  # Ejemplo de procesamiento
        self.data_access.save_data(processed_item)