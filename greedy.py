def find_coins_greedy(amount: int, coins: list):
    coins.sort(reverse=True)  # Sort the coins in descending order
    result = {}
    # Iterate through each coin in sorted order
    for coin in coins:
        count = 0
        # Use the current coin as long as it fits into the remaining amount
        while amount >= coin:
            amount -= coin
            count += 1
            result[coin] = count
    return result


if __name__ == '__main__':
    coins = [50, 25, 10, 5, 2, 1]
    result_dict = find_coins_greedy(101, coins)
    print(result_dict)
