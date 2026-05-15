def calculate_delivery_score(path):
    return max(
        10,
        30 - len(path)
    )


def wrong_shop_penalty():
    return 5