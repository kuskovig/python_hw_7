import csv

ob_schema = {'id': {'type': 'integer', 'required': True},
             'obdb_id': {'type': 'string', 'required': True},
             'name': {'type': 'string', 'required': True},
             'brewery_type': {'type': 'string', 'nullable': True, 'required': True},
             'street': {'type': 'string', 'nullable': True, 'required': True},
             'address_2': {'type': 'string', 'nullable': True, 'required': True},
             'address_3': {'type': 'string', 'nullable': True, 'required': True},
             'city': {'type': 'string', 'nullable': True, 'required': True},
             'state': {'type': 'string', 'nullable': True, 'required': True},
             'county_province': {'type': 'string', 'nullable': True, 'required': True},
             'postal_code': {'type': 'string', 'nullable': True, 'required': True},
             'country': {'type': 'string', 'nullable': True, 'required': True},
             'longitude': {'type': 'string', 'nullable': True, 'required': True},
             'latitude': {'type': 'string', 'nullable': True, 'required': True},
             'phone': {'type': 'string', 'nullable': True, 'required': True},
             'website_url': {'type': 'string', 'nullable': True, 'required': True},
             'updated_at': {'type': 'string', 'nullable': True, 'required': True},
             'created_at': {'type': 'string', 'nullable': True, 'required': True}
             }


def get_amount_per_page_param():
    with open('test_data/openbrewery_amount_param.csv') as file:
        reader = csv.reader(file)
        next(reader)

        for amount in reader:
            yield amount


def get_http_methods():
    with open('test_data/openbrewery_methods.csv') as file:
        reader = csv.reader(file)
        next(reader)

        for method in reader:
            yield method


brewery_amount_per_page = get_amount_per_page_param()
brewery_http_methods = get_http_methods()
