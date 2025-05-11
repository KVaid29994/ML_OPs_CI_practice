import pytest

def calculate_bmi(weight, height_cm):
    return weight / ((height_cm / 100) ** 2)

@pytest.mark.parametrize("weight, height_cm, expected_bmi", [
    (70, 170, 24.22),
    (50, 160, 19.53),
    (90, 180, 27.78)
])

def test_bmi_calculation(weight, height_cm, expected_bmi):
    result = calculate_bmi(weight, height_cm)
    assert round(result, 2) == expected_bmi