import pytest
from main import UQCSTalk

INITIAL_DURATION = 1

'''
Defining the talk object to use for all of my tests
'''
@pytest.fixture
def talk():
    return UQCSTalk("An Introduction to the CI/CD Workflow with Paul Clarke", INITIAL_DURATION)

def test_add_hour(talk: UQCSTalk):
    talk.add_hour()
    assert talk.get_hours() == "I can code HTML and CSS!"