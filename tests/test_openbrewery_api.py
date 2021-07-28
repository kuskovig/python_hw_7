import pytest
import requests
import cerberus
from test_data.openbrewery_schema import ob_schema


def test_get_breweries_schema(brewery_get_breweries_url):
    schema = ob_schema
    response = requests.request('get', brewery_get_breweries_url).json()

    v = cerberus.Validator(schema, ignore_none_values=True)

    assert v.validate(response)


