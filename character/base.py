import pandas as pd


class CVSCharacter(object):
    def __init__(self, csv_path):
        self.name = csv_path.split('/')[-1].split('.')[0]
        self.data = pd.read_csv(csv_path)

    def get_data(self):
        return self.data

    def get_name(self):
        return self.name
