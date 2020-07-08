import pytest


@pytest.yield_fixture()
def setUp():
    print("Running conftest demo1 method setUp")
    yield
    print("Running conftest demo1 method tearDown")



