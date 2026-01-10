def calculate_complex_average(numbers):
    total_inverse = 0
    
    for num in numbers:
        # BUG: deeply nested runtime error
        # If num is 0, this crashes. The bot should add a check here.
        inverse = 100 / num  
        total_inverse += inverse
        
    return total_inverse / len(numbers)
