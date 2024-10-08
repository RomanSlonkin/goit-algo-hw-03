from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> int:
    if min < 1 or max > 1000 or quantity > len(range(min, max)) or min>max:
        while True:
            print("Please, use valid values")
            break
    else:
        return (sorted(sample(range(min, max), quantity)))

lottery_numbers = get_numbers_ticket(15, 1000, 30)
print("Ваші лотерейні числа:", lottery_numbers)

