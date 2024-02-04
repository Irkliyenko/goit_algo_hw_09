import timeit

from dynamic import find_min_coins
from greedy import find_coins_greedy


def main():
    coins = [50, 25, 10, 5, 2, 1]

    # Measure the time taken by dynamic programming for various amounts
    dynamic_100 = timeit.timeit(
        lambda: find_min_coins(100, coins), number=1000)
    dynamic_325 = timeit.timeit(
        lambda: find_min_coins(325, coins), number=1000)
    dynamic_769 = timeit.timeit(
        lambda: find_min_coins(769, coins), number=1000)
    dynamic_1428 = timeit.timeit(
        lambda: find_min_coins(1428, coins), number=1000)
    # Measure the time taken by the greedy algorithm for various amount
    greedy_100 = timeit.timeit(
        lambda: find_coins_greedy(100, coins), number=1000)
    greedy_325 = timeit.timeit(
        lambda: find_coins_greedy(325, coins), number=1000)
    greedy_769 = timeit.timeit(
        lambda: find_coins_greedy(769, coins), number=1000)
    greedy_1428 = timeit.timeit(
        lambda: find_coins_greedy(1428, coins), number=1000)

    # Function to format a dictionary for printing
    def format_dict_for_print(input_dict):
        return ' | '.join([f'{k}: {v}' for k, v in input_dict.items()])

    # Printing the first table with execution times
    print(f'| {"Algorithm":<10} | {"Amount: 100":^12} | {"Amount: 325":^12} | {"Amount: 769":^12} | {"Amount: 1428":^12} |')
    print(f'| {"-"*10} | {"-"*12} | {"-"*12} | {"-"*12} | {"-"*12} |')
    print(f'| {"Dynamic":<10} | {dynamic_100:^12.5f} | {dynamic_325:^12.5f} | {dynamic_769:^12.5f} | {dynamic_1428:^12.5f} |')
    print(f'| {"Greedy":<10} | {greedy_100:^12.5f} | {greedy_325:^12.5f} | {greedy_769:^12.5f} | {greedy_1428:^12.5f} |')
    print('\n')
    # Printing the second table with detailed results
    print(f'| {"Algorithm":<10} | {"Amount: 100":^30} | {"Amount: 325":^30} | {"Amount: 769":^30} | {"Amount: 1428":^30} |')
    print(f'| {"-"*10} | {"-"*30} | {"-"*30} | {"-"*30} | {"-"*30} |')
    print(f'| {"Dynamic":<10} | {format_dict_for_print(find_min_coins(100, coins)):^30} | {format_dict_for_print(find_min_coins(325, coins)):^30} | {format_dict_for_print(find_min_coins(769, coins)):^30} | {format_dict_for_print(find_min_coins(1428, coins)):^30} |')
    print(f'| {"Greedy":<10} | {format_dict_for_print(find_coins_greedy(100, coins)):^30} | {format_dict_for_print(find_coins_greedy(325, coins)):^30} | {format_dict_for_print(find_coins_greedy(769, coins)):^30} | {format_dict_for_print(find_coins_greedy(1428, coins)):^30} |')


if __name__ == '__main__':
    main()
