# data_access.py
class DataAccess:
    def __init__(self):
        self.data = []

    def save_data(self, item):
        self.data.append(item)
        print(f"Datos guardados: {item}")

    def get_data(self):
        return self.data
