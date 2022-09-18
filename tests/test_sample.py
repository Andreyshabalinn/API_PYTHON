import pytest

@pytest.fixture()
def test_sample_1():
    print("TestKEK")

def test_sample_2(test_sample_1):
    print("Sample2")


def test_sample_3(test_sample_1):
    print("Sample3")