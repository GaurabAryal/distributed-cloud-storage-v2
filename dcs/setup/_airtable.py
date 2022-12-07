from airtable import Airtable

class _Airtable():
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_id = 'app0AZSs93ADlnziK'
        self.table_name = 'main'
        self.at = Airtable(self.base_id, self.table_name, self.api_key)
        records = self.at.get_all()
        print(records)
    
    def create(self):
        self.at.insert({'id':1, 'location':1})
        self.get_file_location(0)
    
    def get_file_location(self, id):
        record = self.at.search('id', id)
        return record[0]['fields']['location']

