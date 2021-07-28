import requests

ob_schema = {'a_dict': {'type': 'dict', 'schema': {'id': {'type': 'integer', 'required': True},
             'obdb_id': {'type': 'string', 'required': True},
             'name': {'type': 'string', 'required': True},
             'brewery_type': {'type': 'string', 'nullable': True},
             'street': {'type': 'string', 'nullable': True},
             'address_2': {'type': 'string', 'nullable': True},
             'address_3': {'type': 'string', 'nullable': True},
             'city': {'type': 'string', 'nullable': True},
             'state': {'type': 'string', 'nullable': True},
             'postal_code': {'type': 'string', 'nullable': True},
             'country': {'type': 'string', 'nullable': True},
             'longitude': {'type': 'string', 'nullable': True},
             'latitude': {'type': 'string', 'nullable': True},
             'phone': {'type': 'string', 'nullable': True},
             'website_url': {'type': 'string', 'nullable': True},
             'updated_at': {'type': 'string', 'nullable': True},
             'created_at': {'type': 'string', 'nullable': True}
             }}}



response = requests.request('get', 'https://api.openbrewerydb.org/breweries').json()
print(response)

response2 = requests.request('get', 'https://dog.ceo/api/breeds/list/all').json()
print(response2)