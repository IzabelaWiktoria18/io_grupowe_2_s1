import random
import time
from unittest.mock import patch

# Importuj funkcję do przetestowania
from main import wyslij_sowe

@patch('builtins.input', side_effect=['TestAdresat', 'TestTresc'])
@patch('time.sleep', return_value=None)
@patch('random.random', return_value=0.05)
def test_wyslij_sowe_success(mock_input, mock_sleep, mock_random):
    result = wyslij_sowe()
    assert result == True, f"Expected True but got {result}"

@patch('builtins.input', side_effect=['TestAdresat', 'TestTresc'])
@patch('time.sleep', return_value=None)
@patch('random.random', return_value=0.95)
def test_wyslij_sowe_failure(mock_input, mock_sleep, mock_random):
    result = wyslij_sowe()
    assert result == False, f"Expected False but got {result}"

if __name__ == "__main__":
    test_wyslij_sowe_success()
    test_wyslij_sowe_failure()
    print("All tests passed.")
