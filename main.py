import sys
from math_utils import calculate_complex_average
from config import APP_NAME

def run_app():
    print(f"--- Starting {APP_NAME} ---")
    
    # We are passing a list that contains a zero, which will trigger the bug
    # deep inside the dependency, NOT here in main.
    data_stream = [10, 20, 50, 0, 100]
    
    # Check for zero in the data_stream to prevent potential errors in calculation
    if 0 in data_stream:
        print("Error: Data stream contains zero, which may cause issues in calculation.")
        return
    
    try:
        result = calculate_complex_average(data_stream)
        print(f"Calculation Result: {result}")
    except Exception as e:
        # We re-raise to ensure the bot sees the traceback
        raise e

if __name__ == "__main__":
    run_app()
# CodeSentinal: created for you by RuchirAdnaik.