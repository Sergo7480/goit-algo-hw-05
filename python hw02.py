import re

def generator_numbers(text):
    numbers = re.findall(r"(?P<num>\d+\.\d+)", text)
    
    for num in numbers:
        yield float(num)
        
def sum_profit(text, func):
    return sum(func(text))
    
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
