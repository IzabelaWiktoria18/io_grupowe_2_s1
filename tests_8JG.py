import random
import time
from main import wyslij_sowe

def test_wyslij_sowe_success():
    # Mockowanie wejścia użytkownika i random.random
    random_value = 0.05
    original_input = input
    original_sleep = time.sleep
    original_random = random.random

    try:
        input_values = ['TestAdresat', 'TestTresc']
        def mock_input(prompt):
            return input_values.pop(0)
        time.sleep = lambda x: None
        random.random = lambda: random_value

        input = mock_input

        result = wyslij_sowe()
        assert result == True, f"Expected True but got {result}"

    finally:
        input = original_input
        time.sleep = original_sleep
        random.random = original_random

def test_wyslij_sowe_failure():
    # Mockowanie wejścia użytkownika i random.random
    random_value = 0.95
    original_input = input
    original_sleep = time.sleep
    original_random = random.random

    try:
        input_values = ['TestAdresat', 'TestTresc']
        def mock_input(prompt):
            return input_values.pop(0)
        time.sleep = lambda x: None
        random.random = lambda: random_value

        input = mock_input

        result = wyslij_sowe()
        assert result == False, f"Expected False but got {result}"

    finally:
        input = original_input
        time.sleep = original_sleep
        random.random = original_random

if __name__ == "__main__":
    test_wyslij_sowe_success()
    test_wyslij_sowe_failure()
    print("All tests passed.")
