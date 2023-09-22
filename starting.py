denominations = {
    'pennies': 0.01,
    'nickels': 0.05,
    'dimes': 0.10,
    'quarters': 0.25,
    'singles': 1.00,
    'fives': 5.00,
    'tens': 10.00,
    'twenties': 20.00
}

def get_cash_input():
    cash_array = {}
    total = 0
    for denom, value in denominations.items():
        count = int(input(f"How many {denom} do you have? "))
        cash_array[denom] = count
        total += count * value
    cash_array['total'] = total
    return cash_array

def main():
    starting_cash_array = get_cash_input()
    print(starting_cash_array)
    with open('start.txt', 'w') as f:
        f.write(str(starting_cash_array))
    
if __name__ == "__main__":
    main()
