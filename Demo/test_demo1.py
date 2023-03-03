import pytest


@pytest.fixture()
def setup():
    print("Hello World !!!")
    yield
    print("This is the teardown")

def test_demo(setup):
    print("This is Test Demo")




