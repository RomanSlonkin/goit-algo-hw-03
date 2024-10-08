from random import sample

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > quantity > max or min>max:
        print("Please, use valid values")
    return (sorted(sample(range(min, max), quantity)))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

