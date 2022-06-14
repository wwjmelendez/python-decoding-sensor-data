class HouseInfo:
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []

        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])

            elif rec_area == int(record['area']):
                field_data.append(record['area'])

        return field_data

    


