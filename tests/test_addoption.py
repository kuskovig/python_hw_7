import requests


def test_addoption_url(addoption_base_url, addoption_status_code):
    assert requests.request('get', addoption_base_url).status_code == int(addoption_status_code)
