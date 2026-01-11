# CodeSentinal: created for you by RuchirAdnaik.

def calculate_complex_average(numbers):
    total_inverse = 0
    
    for num in numbers:
        # Check to prevent division by zero
        if num == 0:
            continue  # Skip this number or handle it as needed
        inverse = 100 / num  
        total_inverse += inverse
        
    # Check to prevent division by zero if numbers list is empty or all numbers are zero
    if total_inverse == 0:
        return 0
    
    return total_inverse / len(numbers)