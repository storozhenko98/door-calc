def load_starting_cash():
    with open('start.txt', 'r') as f:
        starting_cash_array = eval(f.read())
    return starting_cash_array

from starting import get_cash_input, denominations

def main():
    starting_cash_array = load_starting_cash()
    ending_cash_array = get_cash_input()
    print(ending_cash_array)
    
    cash_difference = ending_cash_array['total'] - starting_cash_array['total']
    house_cut = cash_difference * 0.20
    player_cut = cash_difference * 0.80
    
    print(f"Cash Difference: {cash_difference}")
    print(f"House Cut: {house_cut}")
    print(f"Player Cut: {player_cut}")
    
    with open('end.txt', 'w') as f:
        f.write(f"Starting Cash: {starting_cash_array}\n")
        f.write(f"Ending Cash: {ending_cash_array}\n")
        f.write(f"Cash Difference: {cash_difference}\n")
        f.write(f"House Cut: {house_cut}\n")
        f.write(f"Player Cut: {player_cut}\n")

if __name__ == "__main__":
    main()
