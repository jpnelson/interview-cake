def best(prices):

    if len(prices) < 2:
        return 0

    best_start = 0
    best_end = 1
    best_start_price = prices[best_start]

    best_delta = prices[best_end] - prices[best_start]

    for i in range(0, len(prices)):
        if prices[i] < best_start_price:
            best_start_price = prices[i]

        this_delta = prices[i] - best_start_price

        if this_delta > best_delta:
            best_delta = this_delta

    if best_delta < 0:
        return 0

    return best_delta
