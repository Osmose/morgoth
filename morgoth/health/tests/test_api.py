from django.db import connection
from django.test.utils import CaptureQueriesContext

import pytest


@pytest.mark.django_db
def test_version(client, mocker):
    get_commit = mocker.patch('morgoth.health.api.views.get_commit')
    get_commit.return_value = '<git hash>'

    res = client.get('/__version__')
    assert res.status_code == 200
    assert res.data == {
        'source': 'https://github.com/mozilla/morgoth',
        'commit': '<git hash>',
        'commit_link': 'https://github.com/mozilla/morgoth/commit/<git hash>',
    }


@pytest.mark.django_db
def test_lbheartbeat_makes_no_db_queries(client):
    queries = CaptureQueriesContext(connection)
    with queries:
        res = client.get('/__lbheartbeat__')
        assert res.status_code == 200
    assert len(queries) == 0
