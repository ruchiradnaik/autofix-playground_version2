def calculate_complex_average(numbers):
    total_inverse = 0
    count = 0
    
    for num in numbers:
        if num == 0:
            continue  # Skip the zero to avoid division by zero
        inverse = 100 / num  
        total_inverse += inverse
        count += 1  # Count only valid numbers
        
    return total_inverse / count if count > 0 else 0  # Avoid division by zero

# CodeSentinal: created for you by RuchirAdnaik.