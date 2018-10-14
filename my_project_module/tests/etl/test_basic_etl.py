import pytest

from my_project_module.etl.basic_etl import BasicEtl


@pytest.fixture
def basic_etl():
    return BasicEtl()


@pytest.fixture
def dummy_data():
    return [1]


class TestBasicEtl:
    @staticmethod
    def test_running_etl(basic_etl, dummy_data):
        assert basic_etl.run_etl(dummy_data) == 1
