import pytest
from dotenv import dotenv_values
from app.config import settings

@pytest.fixture
def settings_variables():
    """
    Returns a dictionary of settings variables.
    """
    return settings.model_dump()

@pytest.fixture
def environment_variables():
    """
    Returns a dictionary of environment variables.
    """
    variables = dotenv_values()
    variables = {key.lower(): value for key, value in variables.items()}
    return variables


def test_config(settings_variables, environment_variables):
    assert settings_variables == environment_variables