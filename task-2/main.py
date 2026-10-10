import random

def get_numbers_ticket(min, max, quantity):



    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):
        return []

    else:

        lottery_ticket = random.sample(range(min, max + 1), quantity)
        lottery_ticket.sort()
        return lottery_ticket

if __name__ == '__main__':
    result = get_numbers_ticket(1, 49, 6)
    print(f"Your lottery ticket: \n{result}")