def find_min_coins(amount: int, coins: list):
    # Initialize a list to store the minimum number of coins required for each amount
    min_coins_required = [0] + [float("inf")] * amount
    # Initialize a list to keep track of the last coin used to achieve each amount
    last_coin_used = [0] * (amount + 1)

    # Iterate through each amount from 1 to the target amount
    for s in range(1, amount + 1):
        # Check each coin to find the minimum number of coins required for the current amount
        for coin in coins:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    # Reconstruct the result dictionary by backtracking through the last_coin_used list
    result = {}
    current_ammount = amount
    while current_ammount > 0:
        coin = last_coin_used[current_ammount]
        result[coin] = result.get(coin, 0) + 1
        current_ammount -= coin
    return result


if __name__ == '__main__':
    coins = [50, 25, 10, 5, 2, 1]
    result_dict = find_min_coins(101, coins)
    print(result_dict)
