import pytest

from src.utils.validation import validate_positive, validate_temperature, validate_timestep, validate_duration


def test_invalid_temperature():
    with pytest.raises(ValueError):
        validate_temperature(float("nan"), "temperature")


def test_invalid_coefficient():
    with pytest.raises(ValueError):
        validate_positive("heat transfer coefficient", -1.0)


def test_invalid_timestep():
    with pytest.raises(ValueError):
        validate_timestep(0.0)


def test_invalid_duration():
    with pytest.raises(ValueError):
        validate_duration(-5.0)
