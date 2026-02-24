import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from bmi_calculator import calculate_bmi
from password_generator import generate_password, password_strength
from unit_converter import convert_length, convert_weight, convert_temperature


# BMI tests
def test_bmi_normal():
    bmi = 70 / (1.75 ** 2)
    assert 18.5 <= bmi < 25

def test_bmi_underweight():
    bmi = 40 / (1.75 ** 2)
    assert bmi < 18.5

def test_bmi_overweight():
    bmi = 90 / (1.75 ** 2)
    assert bmi >= 25


# Password generator tests
def test_password_length():
    pwd = generate_password(12, True, True, True)
    assert len(pwd) == 12

def test_password_strength_weak():
    assert password_strength("abc") == "Weak"

def test_password_strength_strong():
    assert password_strength("Abcdef123!@#") in ["Strong", "Very Strong"]


# Unit converter tests
def test_km_to_miles():
    result = 1 * 0.621371
    assert round(result, 4) == 0.6214

def test_kg_to_lbs():
    result = 1 * 2.20462
    assert round(result, 4) == 2.2046

def test_celsius_to_fahrenheit():
    result = (100 * 9 / 5) + 32
    assert result == 212.0

def test_celsius_to_kelvin():
    result = 0 + 273.15
    assert result == 273.15
