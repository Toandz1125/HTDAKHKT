import requests
from datetime import datetime
from unittest.mock import patch, MagicMock

# --- Các hàm logic ---
def calculate_tax(income):
    if income < 5000:
        return 0
    elif income < 10000:
        return income * 0.1
    else:
        return income * 0.2

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

class User:
    def __init__(self, username):
        self.username = username
    def is_admin(self):
        return self.username == "admin"

def send_welcome_email(email):
    print(f"Sending email to {email}")

def fetch_user():
    response = requests.get("https://api.example.com/user")
    return response.json()

def is_weekend():
    today = datetime.now().weekday()
    return today >= 5

def is_strong(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)

def clean_input(s):
    return s.strip().lower().replace(" ", "_")

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

# --- Các hàm UNIT TEST (Bắt đầu bằng test_ để pytest tự chạy) ---

def test_bai1():
    assert calculate_tax(4000) == 0
    assert calculate_tax(7000) == 700.0
    assert calculate_tax(15000) == 3000.0

def test_bai2():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(18) == False

def test_bai3():
    assert User("admin").is_admin() == True
    assert User("guest").is_admin() == False

def test_bai4():
    with patch('builtins.print') as mock_print:
        send_welcome_email("test@example.com")
        mock_print.assert_called_with("Sending email to test@example.com")

def test_bai5():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"name": "Alice", "age": 30}
        user = fetch_user()
        assert user == {"name": "Alice", "age": 30}

def test_bai6():
    with patch('datetime.datetime') as mock_datetime:
        # Giả lập Thứ 6 (4)
        mock_datetime.now.return_value.weekday.return_value = 4
        assert is_weekend() == False
        # Giả lập Thứ 7 (5)
        mock_datetime.now.return_value.weekday.return_value = 5
        assert is_weekend() == True

def test_bai7():
    assert is_strong("Password123") == True
    assert is_strong("short1") == False

def test_bai8():
    assert clean_input("  Python Core  ") == "python_core"
    # Sửa lỗi logic: 1 dấu cách giữa Hello và World
    assert clean_input("  Hello World  ") == "hello_world" 

def test_bai9():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == None

'''
name: Run Pytest

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install pytest
      - run: pytest
'''
