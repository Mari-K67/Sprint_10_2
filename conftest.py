import pytest
import api_requests


@pytest.fixture
def created_ad_fixture():
    response, ad_id, headers = api_requests.create_ad()

    yield response, ad_id, headers

    api_requests.delete_ad(ad_id, headers)