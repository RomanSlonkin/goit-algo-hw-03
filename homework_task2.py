""" Module providing a function to get unique random values """
from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> int:
    """ function to get unique values from range """
    if min < 1 or max > 1000 or quantity > len(range(min, max)):
        while True:
            return []
    else:
        return (sorted(sample(range(min, max), quantity)))

lottery_numbers = get_numbers_ticket(100, 15, 10) #test
print("Ваші лотерейні числа:", lottery_numbers) #test
# End-of-file (EOF)