import pytest
from .models import Category


# @pytest.fixture(autouse=True)
# def enable_db_access_for_all_tests(db):
#     pass


@pytest.mark.django_db
def test_str():
    category = Category.objects.create(name="foo")
    assert 'foo' == str(category)
