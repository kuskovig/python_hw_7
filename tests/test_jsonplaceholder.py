import pytest
import cerberus
import requests
import random


# testing schema for comments api with random comment id
@pytest.mark.parametrize('resourceid', [str(random.randint(1, 500)) for _ in range(5)])
def test_schema_get_comment(jp_base_url, resourceid):
    schema = {'postId': {'type': 'integer', 'required': True},
              'id': {'type': 'integer', 'required': True, 'allowed': [int(resourceid)]},
              'name': {'type': 'string', 'required': True},
              'email': {'type': 'string', 'required': True},
              'body': {'type': 'string', 'required': True},
              }

    v = cerberus.Validator(schema)
    response = requests.request('get', jp_base_url + 'comments/' + resourceid).json()

    assert v.validate(response)


# testing post method correctly creates todoitems
@pytest.mark.parametrize('user_id,', [(random.randint(1, 10)) for _ in range(5)])
def test_create_todo(jp_base_url, user_id):
    jp_payload = {
        "userId": user_id,
        "title": "this is random text yup",
        "completed": False
    }
    schema = {
        "userId": {'type': 'integer', 'required': True, 'allowed': [user_id]},
        "title": {'type': 'string', 'required': True},
        "completed": {'type': 'boolean', 'required': True},
        "id": {'type': 'integer', 'required': True}
    }
    response = requests.request('post', jp_base_url + 'todos', json=jp_payload).json()
    v = cerberus.Validator(schema)

    assert v.validate(response)


# testing method correctly returns user info by id
@pytest.mark.parametrize('user_id, expected_status',
                         [(0, 404), (1, 200), (5, 200), (10, 200), (11, 404)],
                         ids=['below minimum', 'minimum', 'in valid range', 'maximum', 'above maximum'])
def test_get_users_by_id(user_id, expected_status, jp_base_url):
    assert requests.request('get', jp_base_url + 'users/' + str(user_id)).status_code == expected_status


# testing method return valid photo url
@pytest.mark.parametrize('photo_id', [(random.randint(1, 5000)) for _ in range(5)])
def test_photos_returns_valid_image(jp_base_url, photo_id):
    response_photo_url = requests.request('get', jp_base_url + 'photos/' + str(photo_id)).json()["url"]
    photo = requests.request('get', response_photo_url)

    assert photo.headers['Content-Type'] == 'image/png'
    assert photo.status_code == 200


# testing correct filtering comments by postId
@pytest.mark.parametrize('post_id', [(random.randint(1, 100)) for _ in range(5)])
def test_comments_correctly_filtered_by_postId(post_id, jp_base_url):
    response = requests.request('get', jp_base_url + 'comments', params={'postId': post_id}).json()
    for i in response:
        assert i["postId"] == post_id
