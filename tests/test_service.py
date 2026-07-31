import pytest
import source.service as service

#another testing library, unittest is under python default
import unittest.mock as mock
# can be used with pytest

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"
    