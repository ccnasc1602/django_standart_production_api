import json, os
from pathlib import Path


PATH_DIR = Path(__file__).resolve().parent.parent

class Choices:
    def __init__(self):
        self.filename = os.path.join(PATH_DIR, 'workspace/json_files/auxiliary_tables.json')
        self.choices_data = self.get_choices_all()

    # Create a function that writes a .json file
    def add_choices(data):
        try:
            with open(self.filename, 'w', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))    
        except Exception as ex:
            return str(ex)
    
    def get_choices_all(self):
        try:
            with open(self.filename, encoding='utf8') as file:
                return json.load(file)
        except Exception as ex:
            return str(ex)

    def company_type(self):
        choices = []
        for k in self.choices_data['company_type'].keys():
            v = self.choices_data['company_type'][k]
            element = (k, v)
            choices.append(element)
        
        return tuple(choices)

    def company_size(self):
        choices = []
        for k in self.choices_data['company_size'].keys():
            v = self.choices_data['company_size'][k]
            element = (k, v)
            choices.append(element)
        
        return tuple(choices)

    def state(self):
        choices = []
        for k in self.choices_data['state'].keys():
            v = self.choices_data['state'][k]
            element = (k, v)
            choices.append(element)
        
        return tuple(choices)

    def gender(self):
        choices = []
        for k in self.choices_data['gender'].keys():
            v = self.choices_data['gender'][k]
            element = (k, v)
            choices.append(element)
        
        return tuple(choices)

    def marital_status(self):
        choices = []
        for k in self.choices_data['marital_status'].keys():
            v = self.choices_data['marital_status'][k]
            element = (k, v)
            choices.append(element)
        
        return tuple(choices)

    def legal_type(self):
        choices = []
        for k in self.choices_data['legal_type'].keys():
            v = self.choices_data['legal_type'][k]
            element = (k, v)
            choices.append(element)
        
        return tuple(choices)
